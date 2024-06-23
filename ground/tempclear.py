import os
tempfilepath="C:\\Users\\Yogesh\\AppData\\Local\\Temp"
print("welcome to automatic temp file clear program")
templist=os.listdir(tempfilepath)
deletedfile=0
notdeleted=0

for iterm in templist:
    iterm_path=os.path.join(tempfilepath,iterm)
    if os.path.isfile(iterm_path):
        try:
            os.remove(iterm_path)
            print("file deleted :",iterm_path)
            deletedfile+=1
        except OSError as e:
           # print("error :",e)
            notdeleted+=1
            continue
print("all process done...")
print("Total no of deleted file :",deletedfile)
print("Total no of error or skiped file :",notdeleted)
print("(skipped file are system using file)")