#Comments only on top of command because dockerfile didnt know about # on same line with command
#Docker cashed layers so we need to create architecture not mess
#We can create FROM python:${INAGE_TAG} and then inside docker run place this variable
FROM ubuntu:latest #Always starting FROM
#Cashed
RUN apt-get update && apt-get install -y python3
#Cashed that 3-rd command is Copy
COPY . /app
#Cashed that 4th is WORKDIR
WORKDIR /app #After workdir is set - everything under will be written innit
#And if youll put here another RUN - docker was forced to recreate all cash
ENV PYTHONUNBUFFERED=1
CMV ["pythin3", "app.py"]
#!!!!!!Put your mutable stuff DOWN - unmutable stuff UP
______
#But if you need to create it from scratch - here is command:
#FROM scratch
_____

#More complicated example:

#very light version alpine - on base of light python version
FROM python:3.7.2-alpine3.8
#Metadata for image - NOT LAYER - can contain info about creator of the image
LABEL maintainer="jeffmshale@gmail.com"
#Layer - setting for global image variable settings ADMIN
#This variables only a 'pass' after container creates we transfer into it
#from docker-compose.yml and .env
ENV ADMIN="jeff" PASSWODR="adasdas" MEDIA_PATH="/usr/bin/media"
#Get all indexes updated and upgraded before staritng
#apk add bash - added bash terminal if needed
#In case that i create image only on Python but i require to 
#get inside container from time to time
#we can use apk only on bash - so we need to understand
#which linux we are using currently and also we can use | && || >
RUN apk update && apk upgrade && apk add bash
#Copy all from . to the /app inside the container
COPY . ./app
#same as COPY but ADD also can unpack zip and rar and download 
#data from links BUT - BETTER - got and download with 'curl' and then you 
#can add it with COPY to safety.
#So mot of the time ADD used in case to unpack zip gzip etc.
#ADD <what> <where in cont>
ADD https://raw.githubusercontent.com/discdiver/pachy-vid/master/sample_vids/vid1.mp4 \
/my_app_directory
#This RUN is --exec so its massive with arguments
#There is no ability to work with | && || >
#No addiction to shell or sh - working right with core
#RUN ["command", ["argument for command"]] -- Same as first RUN
#but it depends if first RUN can go throught the bash - second RUN 
#can run on sh
RUN ["mkdir", "/a_directory"]
#This CMD starts on 'docker run' stage and this command will run
#in moment container is UP.
#RUN - execute at docker build stage. CMD - execute on docker UP stage.
CMD ["python", "./my_script.py"]
#Almoust same as CMD but this cannot be changed - 'unmutable' layer
ENTRYPOINT
#Standart expose ports from the container
EXPOSE
#Standart bind or mount for configs media etc
VOLUME
___________
#Example - creating from scratch
#1.Imgae Base - 
#	set base image - FROM
#	Set work directory - WORKDIR
#	Set environment variables - ENV
#	Set local variables - ARG
#2.Settings and dependencies
#	Update and Upgrade packages - RUN
#	Copy all from . to container - COPY
#3.Base of configuration
#	Expose the internal ports - EXPOSE
#	Creatin volumes - VOLUME
#4.Last commands - what should container do at the start
#	Using the - CMD and ENTRYPOINT - to create a command for 
#	container run from the start 

