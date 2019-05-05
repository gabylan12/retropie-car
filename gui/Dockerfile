ARG architecture
FROM $architecture/node:8.16.0-jessie
WORKDIR  /home/node/
RUN yarn --network-timeout 1000000
RUN set http_proxy=
RUN set https_proxy=
RUN yarn config delete proxy
RUN npm config rm proxy
RUN npm config rm https-proxy
RUN npx create-react-app app --network-timeout 100000
RUN npm i -S axios
COPY package.json /home/node/app
COPY public/ /home/node/app/public
COPY src /home/node/app/src

