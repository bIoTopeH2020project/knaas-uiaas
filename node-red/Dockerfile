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

# O-MI/O-DF Node
RUN npm install xmldom
RUN npm install skubler/Node-Red-ODF
Run npm install RohanAsmat/Node-Red-OMI-V9

# Sparql Node
RUN npm install prokolyvakis/node-red-contrib-sparql

# dashboard-ui
RUN npm install node-red-dashboard

# web-worldmap
RUN npm install dceejay/RedMap

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

USER root
# install NumPy (Numerical Computation module for Python)
RUN apt-get -y install build-essential python-dev
RUN apt-get -y install python-numpy
#RUN python -m pip install -U numpy

USER root
# install Scientific Libraries for Python
RUN apt-get -y install python-scipy python-matplotlib python-pandas python-sympy python-nose
#RUN apt-get -y install ipython ipython-notebook

RUN apt-get install libblas-dev  liblapack-dev
RUN apt-get -y install gfortran

# install Scikit-learn (Data Mining for Python)
<<<<<<< HEAD
#RUN pip install -U scikit-learn
=======
RUN apt-get -y install python-sklearn
#RUN pip install -U scikit-learn[alldeps]

>>>>>>> 76521bec8ff366378f95323f0948af4fdb0461e5

# install YAML (python YAML support)
RUN apt-get -y install python-yaml

# install PyMongo (python MongoDB support)
RUN python -m pip install pymongo

# install Requests (HTTP library for Python)
RUN pip install requests

# install statsmodels (statistical models Python Support)
USER root
RUN pip install statsmodels

#install nano for text editing in node-red
USER root
RUN apt-get install nano 

#node red admin
RUN npm install -g node-red-admin

USER node-red
CMD ["npm", "start", "--", "--userDir", "/data"]
