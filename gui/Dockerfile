ARG architecture
FROM $architecture/node:8.16.0-jessie
RUN yarn install --network-timeout 1000000
RUN npm config set registry=https://registry.npmjs.com/
RUN npm config rm proxy
RUN npm config rm https-proxy
WORKDIR  /home/node/
RUN npx create-react-app app
RUN npm i -S axios
COPY package.json /home/node/app
COPY public/ /home/node/app/public
COPY src /home/node/app/src

