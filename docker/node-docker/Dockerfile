#STEP1
FROM node:16

#STEP2
WORKDIR /usr/src/app

#STEP3
COPY package*.json ./
RUN npm install

#STEP4
COPY server.js .

#STEP5
EXPOSE 8000

#STEP6
CMD ["node","server.js"]


