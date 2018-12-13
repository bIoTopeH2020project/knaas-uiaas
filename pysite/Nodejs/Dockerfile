FROM node:10-alpine

RUN mkdir -p /src/app/storage

WORKDIR /src/app

COPY package*.json ./src/app

RUN npm install
RUN npm install underscore
RUN npm install express
RUN npm install body-parser
COPY . /src/app

expose 8090
expose 5080

CMD node load.js & node storage.js
