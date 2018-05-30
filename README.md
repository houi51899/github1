   This is a exam project using openjtalk to develop a alarm. (speech synthesis)
--------------------------------------------------------------------
Simple manual for the setup of VScode to Github
In the beginning
in the directory where the files there you want to upload
1. 
$git init
 #make sure that initiate a git in the directory.
2.
$git remote add origin https://github.com/......../....git
#connect to the github(replace the address with your address in github)

When upload
in the directory where the files there you want to upload

1.
$git add .  
# select all the files here : 
#or use command: $git add "filename" 
# to select  a single file  
#PS.when use "visual studio code"'s git, press the "+"button to add/select the file, and do not! not! not! use the commit button function in VScode )
2.
$git commit -m "comment"  
# commit the selected file(do input this command in console)
3.
$git push origin master  # upload the files to the git

Option
######$git pull origin master #update the current files from your github  

######$git status #confirm the current status



