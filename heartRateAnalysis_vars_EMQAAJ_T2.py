  ####################################################
 ###   heartRateAnalysis subject varialble file   ###
####################################################

import pickle
import os
import time
import sys

### study variables
sdyDta                                = {}
sdyDta["sbjName"]	      = "EMQAAJ"
sdyDta["timePoint"]	      = "T2"
sdyDta["invertFactor"]                = "-1"
sdyDta["samplingRate"]	      = "5000"
sdyDta["duration"]	      = "303.36"
sdyDta["rawDataDatapoints"]           = "1516800"
sdyDta["rawDataMinimum"]              = "-995.000"
sdyDta["rawDataMaximum"]              = "1254.200"

sdyDta["rawDataGraphMinimum"]         = "-1000"
sdyDta["rawDataGraphMaximum"]         = "1500"
sdyDta["subDataGraphMinimum"]         = "-1000"
sdyDta["subDataGraphMaximum"]         = "1000"
sdyDta["normDataGraphMinimum"]        = "-1"
sdyDta["normDataGraphMaximum"]        = "1"
sdyDta["rawDataGraphDuration"]        = "310"
sdyDta["rawDataGraphDurationS"]       = "20"
sdyDta["rawDataGraphDurationXS"]      = "2"
sdyDta["subtractMovingAverageRange"]  = "5000"
sdyDta["smoothMovingAverageRange"]    = "100"



sdyDta["sbjDir"]	      = sdyDta["sbjName"]+"_"+sdyDta["timePoint"]+"/"
sdyDta["orgFile"]	      = sdyDta["sbjName"]+"_"+sdyDta["timePoint"]+".dat"
sdyDta["convertedFile"]	      = sdyDta["orgFile"][0:-4]+"_converted.tab"
sdyDta["timeColumnFile"]	      = sdyDta["convertedFile"][0:-4]+"__timeColumnAdded.tab"
sdyDta["invertedFile"]                = sdyDta["timeColumnFile"][0:-4]+"__inverted.tab"
sdyDta["subtractedMovingAverageFile"] = sdyDta["invertedFile"][0:-4]+"__subtractedMovingAverage"+sdyDta["subtractMovingAverageRange"]+".tab"
sdyDta["smoothedFile"]                = sdyDta["subtractedMovingAverageFile"][0:-4]+"__smoothedMovingAverage"+sdyDta["smoothMovingAverageRange"]+".tab"
sdyDta["normalizedFile"]              = sdyDta["smoothedFile"][0:-4]+"__normalized.tab"
sdyDta["rPeakFile"]                   = sdyDta["normalizedFile"][0:-4]+"__r_peaks.tab"
sdyDta["timecoursePeaksFile"]         = sdyDta["normalizedFile"][0:-4]+"__peaksAdded.tab"

sdyDta["pklFle"]	      = sys.argv[1]
sdyDta["soundFile"]	      = "star_wars_r2d2_kurz_1.wav"
sdyDta["scriptsBackUpDir"]            = os.environ['HD']+"/pythons/"


### pickle.dump study variables
pkl = open(sdyDta["pklFle"], "w")
pickle.dump(sdyDta, pkl)
pkl.close()

print("\n\n ## created new pkl file with subject vars ("+sys.argv[0]+") at "+time.strftime("%Y-%m-%d %H:%M:%S"))

### self backup
os.system("cp "+sys.argv[0]+" "+sdyDta["scriptsBackUpDir"])
