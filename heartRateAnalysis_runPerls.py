  ###############################################################
 ###   h e a r t R a t e A n a l y s i s   r u n P e r l s   ###
###############################################################
import datetime
import os
import pickle
import sys
import time

startString="\n\n\n\n\n"
startString=startString+"     ############################################################################\n"
startString=startString+"    ###  starting python script heartRateAnalysis.py at "+time.strftime("%Y-%m-%d %H:%M:%S")+"  ###\n"
startString=startString+"   ############################################################################\n"
print startString



### subject vars
sbjList = []
#sbjList.append("EMQAAJ_T1")
sbjList.append("EMQAAJ_T2")
#sbjList.append("PAC3HV_T1")
#sbjList.append("PAC3HV_T2")


### analyses steps
analysesList = []
#analysesList.append("convertTimecourseData")
#analysesList.append("analyseTimecourseData")

#analysesList.append("addTimeColumn")
#analysesList.append("plotRawData")
#analysesList.append("invertData")
#analysesList.append("plotInvertedData")
#analysesList.append("subtractMovingAverage")
#analysesList.append("plotSubtractedMovingAverageData")
#analysesList.append("smoothWithMovingAverage")
#analysesList.append("plotSmoothedData")
#analysesList.append("normalizeData")
#analysesList.append("plotNormalizedData")
#analysesList.append("findRPeaks")
#analysesList.append("addPeaksToTimecourseData")
analysesList.append("plotPeakData")

#analysesList.append("cleanUp")
#analysesList.append("backup")

### navi vars
ask4SD          = 0
shutDown        = 0
dtbfsd          = ""
showImageSwitch = "0"
#dtbfsd   = "cd /media/iltis/rewEmpEda/scripts/1stLevel/; python ree1stLevel_00_all_too.py"


if (ask4SD == 1):
	print "\n\n                     shutdown when python has finished? ",
	input = sys.stdin.readline()
	input = input[:-1]
	if (input == "y"):
		print "                    okay, will shutdown after finishing."
		shutDown = 1		
	else:
		print "                    okay, won't shutdown.\n\n"
		shutDown = 0

if (dtbfsd != ""):
	print "\n\n                     do another script python has finished? ",
	input = sys.stdin.readline()
	input = input[:-1]
	if (input == "y"):
		print "                    okay, will do it."
		
	else:
		print "                    okay, won't do it.\n\n"
		dtbfsd = ""

if (shutDown == 1):
	showImageSwitch= "0"


### function: print in logfile
def printLog(text):
	output=open("heartRateAnalysis_log.txt", "a")
	output.write(text)
	output.write("\n\n")
	output.close()	
printLog(startString)




### function: run command und log times
def runCommandAndLogTimes(command):
	output=open("heartRateAnalysis_log.txt", "a")
	output.write(command+"\n")
	print "\n\nrunning command:\n"+command
	startTime = datetime.datetime.now()
	os.system(command)
	endTime = datetime.datetime.now()
	diffTime = endTime - startTime
	print "duration: "+str(diffTime.total_seconds())+"s"
	output.write("duration: "+str(diffTime.total_seconds())+"s\n\n")
	output.close()	








### loop for each subject
for sbjName in sbjList:

	### create new pkl file for the global study vars
	sdyVarPyt= sbjName+"/heartRateAnalysis_vars_"+sbjName+".py" 
	sdyVarPkl= sbjName+"/heartRateAnalysis_vars_"+sbjName+".pkl"

	command = "python2 "+sdyVarPyt+" "+sdyVarPkl
	os.system(command)

	### load the global study vars
	sdyDtaImp = open(sdyVarPkl)
	sdyDta = pickle.load(sdyDtaImp)
	sdyDtaImp.close()


	for analysisStep in analysesList:

		if (analysisStep== "convertTimecourseData"):

			command = "perl 12_convertTimecourseData.pl "+sdyDta["sbjDir"]+sdyDta["orgFile"]+" "+sdyDta["sbjDir"]+sdyDta["convertedFile"]
			runCommandAndLogTimes(command)



		if (analysisStep== "analyseTimecourseData"):

			command = "perl 15_analyzeTimecourseData.pl "+sdyDta["sbjDir"]+sdyDta["convertedFile"]+" "+sdyDta["samplingRate"]
			runCommandAndLogTimes(command)


		if (analysisStep== "addTimeColumn"):

			command = "perl 21_addTimeColumn.pl "+sdyDta["sbjDir"]+sdyDta["convertedFile"]+" "+sdyDta["sbjDir"]+sdyDta["timeColumnFile"]+" "+sdyDta["samplingRate"]
			runCommandAndLogTimes(command)



		if (analysisStep== "plotRawData"):

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["timeColumnFile"]+" "+sdyDta["rawDataGraphMinimum"]+" "+sdyDta["rawDataGraphMaximum"]+" "+sdyDta["rawDataGraphDuration"]+" "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["timeColumnFile"]+" "+sdyDta["rawDataGraphMinimum"]+" "+sdyDta["rawDataGraphMaximum"]+" "+sdyDta["rawDataGraphDurationS"]+" "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["timeColumnFile"]+" "+sdyDta["rawDataGraphMinimum"]+" "+sdyDta["rawDataGraphMaximum"]+" "+sdyDta["rawDataGraphDurationXS"]+" "+showImageSwitch
			runCommandAndLogTimes(command)



		if (analysisStep== "invertData"):

			command = "perl 41_inverte_datapoints.pl "+sdyDta["sbjDir"]+sdyDta["timeColumnFile"]+" "+sdyDta["sbjDir"]+sdyDta["invertedFile"]+" "+sdyDta["invertFactor"]
			runCommandAndLogTimes(command)




		if (analysisStep== "plotInvertedData"):

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["invertedFile"]+" "+sdyDta["rawDataGraphMinimum"]+" "+sdyDta["rawDataGraphMaximum"]+" "+sdyDta["rawDataGraphDuration"]+" "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["invertedFile"]+" "+sdyDta["rawDataGraphMinimum"]+" "+sdyDta["rawDataGraphMaximum"]+" "+sdyDta["rawDataGraphDurationS"]+" "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["invertedFile"]+" "+sdyDta["rawDataGraphMinimum"]+" "+sdyDta["rawDataGraphMaximum"]+" "+sdyDta["rawDataGraphDurationXS"]+" "+showImageSwitch
			runCommandAndLogTimes(command)



		if (analysisStep== "subtractMovingAverage"):

			command = "perl 42_subtract_moving_average.pl "+sdyDta["sbjDir"]+sdyDta["invertedFile"]+" "+sdyDta["sbjDir"]+sdyDta["subtractedMovingAverageFile"]+" "+sdyDta["subtractMovingAverageRange"]
			runCommandAndLogTimes(command)



		if (analysisStep== "plotSubtractedMovingAverageData"):

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["subtractedMovingAverageFile"]+" "+sdyDta["subDataGraphMinimum"]+" "+sdyDta["subDataGraphMaximum"]+" "+sdyDta["rawDataGraphDuration"]+" "+showImageSwitch
			runCommandAndLogTimes(command)	

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["subtractedMovingAverageFile"]+" "+sdyDta["subDataGraphMinimum"]+" "+sdyDta["subDataGraphMaximum"]+" "+sdyDta["rawDataGraphDurationS"]+" "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["subtractedMovingAverageFile"]+" "+sdyDta["subDataGraphMinimum"]+" "+sdyDta["subDataGraphMaximum"]+" "+sdyDta["rawDataGraphDurationXS"]+" "+showImageSwitch
			runCommandAndLogTimes(command)



		if (analysisStep== "smoothWithMovingAverage"):

			command = "perl 44_smooth_using_moving_average.pl "+sdyDta["sbjDir"]+sdyDta["subtractedMovingAverageFile"]+" "+sdyDta["sbjDir"]+sdyDta["smoothedFile"]+" "+sdyDta["smoothMovingAverageRange"]
			runCommandAndLogTimes(command)



		if (analysisStep== "plotSmoothedData"):

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["smoothedFile"]+" "+sdyDta["subDataGraphMinimum"]+" "+sdyDta["subDataGraphMaximum"]+" "+sdyDta["rawDataGraphDuration"]+" "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["smoothedFile"]+" "+sdyDta["subDataGraphMinimum"]+" "+sdyDta["subDataGraphMaximum"]+" "+sdyDta["rawDataGraphDurationS"]+" "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["smoothedFile"]+" "+sdyDta["subDataGraphMinimum"]+" "+sdyDta["subDataGraphMaximum"]+" "+sdyDta["rawDataGraphDurationXS"]+" "+showImageSwitch
			runCommandAndLogTimes(command)



		if (analysisStep== "normalizeData"):

			command = "perl 45_normalizeTimecourse.pl "+sdyDta["sbjDir"]+sdyDta["smoothedFile"]+" "+sdyDta["sbjDir"]+sdyDta["normalizedFile"]
			runCommandAndLogTimes(command)



		if (analysisStep== "plotNormalizedData"):

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["normalizedFile"]+" "+sdyDta["normDataGraphMinimum"]+" "+sdyDta["normDataGraphMaximum"]+" "+sdyDta["rawDataGraphDuration"]+" "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["normalizedFile"]+" "+sdyDta["normDataGraphMinimum"]+" "+sdyDta["normDataGraphMaximum"]+" "+sdyDta["rawDataGraphDurationS"]+" "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 31_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["normalizedFile"]+" "+sdyDta["normDataGraphMinimum"]+" "+sdyDta["normDataGraphMaximum"]+" "+sdyDta["rawDataGraphDurationXS"]+" "+showImageSwitch
			runCommandAndLogTimes(command)



		if (analysisStep== "findRPeaks"):

			command = "perl 51_findRPeaks.pl "+sdyDta["sbjDir"]+sdyDta["normalizedFile"]+" "+sdyDta["sbjDir"]+sdyDta["rPeakFile"]
			runCommandAndLogTimes(command)



		if (analysisStep== "addPeaksToTimecourseData"):

			command = "perl 61_addPeaksToTimecourseData.pl "+sdyDta["sbjDir"]+sdyDta["normalizedFile"]+" "+sdyDta["sbjDir"]+sdyDta["rPeakFile"]+" "+sdyDta["sbjDir"]+sdyDta["timecoursePeaksFile"]
			runCommandAndLogTimes(command)



		if (analysisStep== "plotPeakData"):

			command = "perl 62_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["timecoursePeaksFile"]+" "+sdyDta["normDataGraphMinimum"]+" "+sdyDta["normDataGraphMaximum"]+" 0 60 "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 62_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["timecoursePeaksFile"]+" "+sdyDta["normDataGraphMinimum"]+" "+sdyDta["normDataGraphMaximum"]+" 60 120 "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 62_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["timecoursePeaksFile"]+" "+sdyDta["normDataGraphMinimum"]+" "+sdyDta["normDataGraphMaximum"]+" 120 180 "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 62_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["timecoursePeaksFile"]+" "+sdyDta["normDataGraphMinimum"]+" "+sdyDta["normDataGraphMaximum"]+" 180 240 "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 62_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["timecoursePeaksFile"]+" "+sdyDta["normDataGraphMinimum"]+" "+sdyDta["normDataGraphMaximum"]+" 240 300 "+showImageSwitch
			runCommandAndLogTimes(command)

			command = "perl 62_visualizeDataWithR.pl "+sdyDta["sbjDir"]+sdyDta["timecoursePeaksFile"]+" "+sdyDta["normDataGraphMinimum"]+" "+sdyDta["normDataGraphMaximum"]+" 300 360 "+showImageSwitch
			runCommandAndLogTimes(command)



		if (analysisStep== "backup"):

			command = "java -jar jfs.jar backup_fabrice.jfs"
			runCommandAndLogTimes(command)





### play sound		
command = "play -q -v 0.9 "+sdyDta["soundFile"]+" >/dev/null 2>&1"; os.system(command)
print("\n\n### ending python script te1stLevelAll.py at "+time.strftime("%Y-%m-%d %H:%M:%S")+"\n\n")



### do additional script
if (dtbfsd != ""):
	os.system(dtbfsd)


### shutdown
if (shutDown == 1):
	os.system("mate-session-save --shutdown-dialog --gui")


### self backup
os.system("cp "+sys.argv[0]+" "+os.environ['HD']+"/pythons/")
