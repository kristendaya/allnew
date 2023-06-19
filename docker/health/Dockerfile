#Step1 : Base Images
FROM ubuntu:latest

#Step2 : Install Packages
Run apt -y update && apt -y upgrade && apt -y install nginx && apt -y install curl
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf

#Step3 :
COPY index.html /usr/share/nginx/html

#Step4
HEALTHCHECK --interval=10s --timeout=3s CMD curl -f http://localhost/ || exit 1

#Step5
CMD ["nginx"
