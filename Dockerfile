FROM node:10.14.2

WORKDIR /app

CMD ["npm", "run", "start"]

ADD package.json package-lock.json ./

RUN npm install

ADD . .

RUN npm run build
