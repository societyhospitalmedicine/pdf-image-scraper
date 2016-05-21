##############################################################################################################################################################
##############################################################################################################################################################

## Script below goes through pdfbox-app and retrieves all the images from given pdf file and saves images per page
## COMMAND  python image_parse.py ~/workspace/search/reports/SoHM_2014/SoHM_2014_Report.pdf 
## FOR OBTAINING IMAGE ATTRIBUTES: http://stackoverflow.com/questions/15800704/python-get-image-size-without-loading-image-into-memory

###############################################################################################################################################################
###############################################################################################################################################################

import sys
import subprocess

argList=['-jar','/home/ubuntu/.m2/repository/com/mycompany/ExtractImagesFromPDFPages/1.0-SNAPSHOT/ExtractImagesFromPDFPages-1.0-SNAPSHOT-jar-with-dependencies.jar',sys.argv[1]]
p = subprocess.Popen(['java'] +argList, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
(stdoutdata, stderrdata) = p.communicate()
p.stdin.close()
p.stdout.close()

### to modify java file ExtracImagesFromPDFPages
### install maven sudo apt-get install maven
### modify javasource file
### cd into folder with pom.xml
### mvn clean install (this installs this into the .m2 folder)

### To execute script in another computer
### 1. copy this python script
### 2. copy jar file located in /home/ubuntu/.m2/repository/com/mycompany/ExtractImagesFromPDFPages/1.0-SNAPSHOT/ExtractImagesFromPDFPages-1.0-SNAPSHOT-jar-with-dependencies.jar
### 3. fix path in python script to new path to jar file in step 2 and new path to pdf file
### 4. run script: python  image_parse_v2.py  ../../blah.pdf