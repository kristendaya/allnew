#STEP1
FROM python:3.9

#STEP2 : Package install
RUN apt -y update $$ apt -y upgrade && apt -y install git net-tools vim

#STEP3: Sepcify a working directory
WORKDIR '/root'

#STEP4 Config file copy
COPY .bashrc .
COPY .exrc .

#STEP5 open port
EXPOSE 8000



