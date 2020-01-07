import shutil
import os
import re

datePattern = re.compile(r'^(.*?)(\d\d).(\d\d).(\d{4}).*?(\..*)')

# for each file in the current directory
for filename in os.listdir('.'):
    #search the name of the filename with the regular expression
    date = datePattern.search(filename)
    #if the name does not contain what we are looking for
    if date == None:
        print('no files')
        continue

    before = date.group(1)
    month = date.group(2)
    day = date.group(3)
    year = date.group(4)
    extention = date.group(5)

    # add the groups in the desired order 
    newFile = day + '-' + month + '-' + year + '' + extention

    absWorkingDir = os.path.abspath('.')
    # join the location of the file with the file name
    oldfilename = os.path.join(absWorkingDir, filename)
    newfilename = os.path.join(absWorkingDir, newFile)

    #rename the file
    shutil.move(oldfilename, newfilename) 