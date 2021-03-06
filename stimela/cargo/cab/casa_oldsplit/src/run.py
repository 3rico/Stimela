import os
import sys
import logging
import Crasa.Crasa as crasa

sys.path.append("/scratch/stimela")

utils = __import__('utils')

CONFIG = os.environ["CONFIG"]
INPUT = os.environ["INPUT"]
OUTPUT = os.environ["OUTPUT"]
MSDIR = os.environ["MSDIR"]

cab = utils.readJson(CONFIG)

args = {}
for param in cab['parameters']:
    name = param['name']
    value = param['value']

    if value is None:
        continue

    args[name] = value

os.chdir(MSDIR)
task = crasa.CasaTask(cab["binary"], **args)
task.run()
