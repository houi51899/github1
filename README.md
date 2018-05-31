==============================================================================================
# Openjtalk alarm

This is a exam project using openjtalk to develop a alarm and share it in Github. (speech synthesis)

The manual consists of two parts. In the first part, I will share the experience of developing the alarm with speech synthesis engine. In the second part, I want to share the experience of how to connect Visual Studio Code with Github to manage the version of the project.
Beware that all the opration is done in ubuntu18.04LTS

##Part 1

Preperation for openjtalk coding.
Before the coding, we need to install some SDK. 

- install the engine (open-jtalk):

$sudo apt-get install open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001

- download the voice file(zip):

$wget https://sourceforge.net/projects/mmdagent/files/MMDAgent_Example/MMDAgent_Example-1.6/MMDAgent_Example-1.6.zip/download -O MMDAgent_Example-1.6.zip

- unzip the voice file:

$unzip MMDAgent_Example-1.6.zip MMDAgent_Example-1.6/Voice/*

$sudo cp -r MMDAgent_Example-1.6/Voice/mei/ /usr/share/hts-voice

with the SDK above you have enough material to build a simple speech synthesis program.
As for the code sourse, please check the file "test.py" in the same folder. 

--------------------------------------------------------------------------------------------
## Part 2

 Simple manual for the setup for VScode to Github.

 In the beginning,let's "cd" to get in the directory where the files there you want to upload and update

- initiate a git in this folder.
$git init

- address this folder to the project in Github(replace the address with your address in github)

$git remote add origin https://github.com/......../....git


 When upload,go into the same folder

- select all the files in this folder
$git add .  

or use $git add "filename" to select a single file  
when use "visual studio code"'s git, press the "+"button to add/select the file, and do not! not! not! use the commit button function in VScode )

- commit the selected file(do input this command in console)
$git commit -m "comment"  

- upload the files to the git
$git push origin master 

# Option

$git pull origin master (update the current files from your github)  

$git status (confirm the current status)

=======================================================================================

## Acknowledge

I want thank Mr.honma for the help in connecting the VScode to Github.
And thank your for finishing the reading and for the overlooking of my poor grammar lol.

## References
- [ch1. OpenJtalk+python(in Japanese)](https://qiita.com/kkoba84/items/b828229c374a249965a9)