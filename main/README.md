# SYSC3010_L3_T_3
# **Covid 19 Laboratory Monitoring System**
This project concerns a system to monitor, record and analize temperature and pressure readings from a **COVID** vaccine Lab as well as temperature and Patient information form a **COVID** Patient Lab.

## **Motivation**
The motivation for the creation and existence of this proiject is the existence of the COVID virus and the need for proper vaccine production and the study of its effects on humans

### **Tests**
All test are under Test directory, tests are written using python unittest and are run: `python test.py`

## **How to use?**

### Installing Android device emulator on virtualbox for running Android appliction
1. The link below is to download the Android patch to run on Virtual Box 
`https://www.android-x86.org/ `

2. Click on the 3rd link shown below to begin installing 
![alt text](readme.png?raw=true)

3. The link below is for downloading Virtual Box  
`https://www.virtualbox.org/ `

4. Then, follow the steps provided in the link below to setup Android version that you just downloaded on Virtual Box. 
`https://www.howtogeek.com/164570/how-to-install-android-in-virtualbox/`
Additonal Info: The steps shown in the link in step 4 doesn’t go over everything to complete the setup. The following steps are after you complete all the steps in step 4
-In settings for virtual box anddroid device:
    -select Network and change "Attached to:" to bridged adapter
    -select Storage and set Controller: IDE to empty

5. Finally, the youtube video below covers the final steps involved, Start video at - 4:27 
`https://www.youtube.com/watch?v=oFdnE74qqIs&ab_channel=NewTechnicalTricks `

6. Clone App code from Master branch in he repository, this contains code for Android Studio Project

### Starting the System
1. Edit config.txt file changing parameters to match current node

2. In terminal Run: `python main.py`

3. Run `python cleanup.py` to cleanup and delete created files

## **Contribute**
-clone repository: `git clone https://github.com/IfiokUdohTeams/SYSC3010_L3_T_3.git`
-Make new branch: 
-Make dev changes
-submit code for peer review
any questions feel free to email ifiok at `ifiokudoh@cmail.carleton.ca`

## **Credit**
People who contributed to this project are:
Harshil Verma, Linpu Liu, Zoya Mushtaq and Ifiok Udoh

