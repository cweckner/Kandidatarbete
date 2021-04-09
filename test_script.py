import backend
import time
import commands
import sys
from datetime import datetime
from datetime import timedelta


def run_test(bc, mc):
  backendTest = backend.backend()
  transactionID = "00000000-0000-0000-0000-000000000000"
  currentcharge = 20
  wantedcharge = 80
  batterycapacity = float(bc)
  maxcurrent = float(mc)
  dep_time = ""
  outlet = 1
  ts = datetime.now()
  ts = ts + timedelta(seconds=60*60)
  cd = ts.strftime("%Y-%m-%d")
  ct = ts.strftime("%H:%M:%S")

  transactionID = commands.incrementTransactionID(transactionID)
  backendTest.chargingLoop( True, currentcharge, wantedcharge, batterycapacity, maxcurrent, cd + " " + ct, outlet, transactionID)


#stoppa in battery capacity och max current som parametrar  
run_test(sys.argv[1], sys.argv[2])