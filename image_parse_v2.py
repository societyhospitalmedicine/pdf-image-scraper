##############################################################################################################################################################
##############################################################################################################################################################

## Script below goes through pdfbox-app and retrieves all the images from given pdf file and saves images per page
## COMMAND  python image_parse.py ~/workspace/search/reports/SoHM_2014/SoHM_2014_Report.pdf 
## FOR OBTAINING IMAGE ATTRIBUTES: http://stackoverflow.com/questions/15800704/python-get-image-size-without-loading-image-into-memory

###############################################################################################################################################################
###############################################################################################################################################################

import sys
import subprocess
import os 

# first make directory from aws

# this includes temp and parent directory of pdf
pdf_path = sys.argv[1]
# this is parent directory of pdf
path_to_temp = sys.argv[2]
argList=['-jar','/home/ubuntu/.m2/repository/com/mycompany/ExtractImagesFromPDFPages/1.0-SNAPSHOT/ExtractImagesFromPDFPages-1.0-SNAPSHOT-jar-with-dependencies.jar',pdf_path]
p = subprocess.Popen(['java'] +argList, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
(stdoutdata, stderrdata) = p.communicate()
print stdoutdata
p.stdin.close()
p.stdout.close()

#### loop through all created files in temp directory
for root, dirs, files in os.walk(pdf_path):
    for file in files:
        if file.endswith(".png"):
            print os.path.join(root,file)

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