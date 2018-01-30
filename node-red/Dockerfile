FROM node:6
#FROM jupyter/datascience-notebook

# Home directory for Node-RED application source code.
RUN mkdir -p /usr/src/node-red

# User data directory, contains flows, config and nodes.
RUN mkdir /data

WORKDIR /usr/src/node-red

# Add node-red user so we aren't running as root.
RUN useradd --home-dir /usr/src/node-red --no-create-home node-red \
    && chown -R node-red:node-red /data \
    && chown -R node-red:node-red /usr/src/node-red

USER node-red

# package.json contains Node-RED NPM module and node dependencies
COPY package.json /usr/src/node-red/
RUN npm install

# python3 node
RUN npm install node-red-contrib-python3-function

# OMI Nodes
RUN npm install skubler/Node-Red-OMI
RUN npm install skubler/Node-Red-ODF
Run npm install jrobert-github/Node-Red-OMI-V9

#Sparql Nodes
RUN npm install prokolyvakis/node-red-contrib-sparql

#CoaaS Nodes
#RUN npm install ahas36/CoaaS-Node-Red

# dashboard-ui
RUN npm install node-red-dashboard

# web-worldmap
RUN npm install node-red-contrib-web-worldmap

# open weather map
RUN npm install node-red-node-openweathermap

# mongodb on node-red
RUN npm install node-red-contrib-mongodb2

# User configuration directory volume
EXPOSE 1880

# Environment variable holding file path for flows configuration
ENV FLOWS=flows.json

# install RDFlib (python RDF support)
USER root
RUN apt-get update
RUN apt-get -y install python-pip
RUN pip install sparqlwrapper
RUN pip install rdflib

# install NumPy (Numerical Computation module for Python)
RUN apt-get -y install build-essential python-dev
RUN apt-get -y install python-numpy

# install Scientific Libraries for Python
RUN apt-get -y install python-scipy python-matplotlib python-pandas python-sympy python-nose
#RUN apt-get -y install ipython ipython-notebook

# install Scikit-learn (Data Mining for Python)
RUN pip install -U scikit-learn

# install YAML (python YAML support)
RUN apt-get -y install python-yaml

# install PyMongo (python MongoDB support)
RUN python -m pip install pymongo

# install Requests (HTTP library for Python)
RUN pip install requests

# install statsmodels (statistical models Python Support)
USER root
RUN pip install statsmodels


USER node-red
CMD ["npm", "start", "--", "--userDir", "/data"]
