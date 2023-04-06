FROM nodered/node-red as fetch_img

FROM fetch_img as set_workdir

WORKDIR /usr/src/node-red

FROM set_workdir as dependencies

RUN npm install @mindconnect/node-red-contrib-mindconnect@latest && \ 
npm install node-red-dashboard && \
npm install node-red-node-random && \
npm install node-red-node-mysql && \
npm install node-red-node-smooth && \
npm install node-red-contrib-ui-led