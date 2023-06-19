# Step1: Base Images
FROM ubuntu

#Step2: Install Program
RUN apt -y update && apt -y install -q nginx && apt -y install vim

#step3: file copy
COPY index.html /var/www/html

#step4: start NGINX
CMD ["nginx","-g","daemon off;"]
