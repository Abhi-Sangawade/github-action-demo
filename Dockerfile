FROM node:20-alpine AS build

WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

FROM node:20-alpine AS runtime
WORKDIR /app
COPY package.json .
RUN npm install --production
COPY --from=build /app/dist ./dist
COPY server.js .
EXPOSE 5000
CMD ["node", "server.js"]
