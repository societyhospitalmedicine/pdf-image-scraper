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

## end program
# (stdoutdata, stderrdata) = p.communicate()
for line in p.stdout:
    image = open(line, "wb")
    print image

#### loop through all created files in temp directory
# print 'dfdf'
# for root, dirs, files in os.walk(pdf_path):
#     print'df'
#     for file in files:
#         if file.endswith(".png"):
#             image = os.path.join(root,file)
#             out_file = open("out-file", "wb") # open for [w]riting as [b]inary
#             # out_file.write(data)
#             print out_file
#             out_file.close()
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



####################################################################
################# SAVE IMAGE FILE ##################################
####################################################################
# from django.core.files import File  # you need this somewhere
# import urllib


# # The following actually resides in a method of my model

# result = urllib.urlretrieve(image_url) # image_url is a URL to an image

# # self.photo is the ImageField
# self.photo.save(
#     os.path.basename(self.url),
#     File(open(result[0]))
#     )

# self.save()