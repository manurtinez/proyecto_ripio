#FROM node:18-alpine
#
#ENV PATH /frontend/node_modules/.bin:$PATH
#
#WORKDIR /frontend
#COPY package.json yarn.lock ./frontend/
#RUN yarn install --frozen-lockfile
#
#COPY . ./frontend/

#EXPOSE 3000
FROM node:alpine
WORKDIR /frontend
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile
COPY . .
EXPOSE 3000
CMD ["yarn", "start"]