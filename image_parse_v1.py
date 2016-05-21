##############################################################################################################################################################
##############################################################################################################################################################

## Script below goes through pdfbox-app and retrieves all the images from given pdf file
## COMMAND  python image_parse.py ~/workspace/search/reports/SoHM_2014/SoHM_2014_Report.pdf 
## FOR OBTAINING IMAGE ATTRIBUTES: http://stackoverflow.com/questions/15800704/python-get-image-size-without-loading-image-into-memory

###############################################################################################################################################################
###############################################################################################################################################################

import sys
import subprocess

argList=['-jar','./pdfbox-app-2.0.1.jar','ExtractImages',sys.argv[1]]
p = subprocess.Popen(['java'] +argList, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
(stdoutdata, stderrdata) = p.communicate()
p.stdin.close()
p.stdout.close()



# 