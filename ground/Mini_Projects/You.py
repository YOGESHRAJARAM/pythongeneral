from pytube import YouTube

url=input("please past the url hear to downloade the video :")
processurl="'"+url+"'"
my_video=YouTube(processurl)
print("--------------Details-------------")
title = my_video.title
desc = my_video.description
print(title)
print(desc)
choise=str(input("enter (Y) to downloade the video :"))
choise_=choise.upper()
print(choise_)
if choise_ == "Y":
    print("Your video start downloading...")
    my_video = my_video.streams.get_highest_resolution()
    my_video.download()
    print(".....sucessfully downloaded.....")
else:
    print(".....thankyou.....")
    print("version1")
<<<<<<< HEAD
=======
    print("version3")
>>>>>>> 6d6858040b44aa97eb51a5308ec37dc7e0c97e8f
    