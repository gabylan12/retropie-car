ARG architecture
FROM $architecture/node:8.16.0-jessie
RUN npm i -S axios
RUN npx create-react-app gui
RUN cp -R gui/node_modules /home/node/app
COPY package.json /home/node/app
COPY public /home/node/app/
COPY src /home/node/app/

