# bIoTope's KnaaS & UIaaS

## Description

This repository contains the integrated codebase of [bIoTope](https://biotope-project.eu)'s KnaaS (Knowledge as a Service Framework) and UIaaS (User Interface as a Service) components.

* *KnaaS* aims at providing a conceptual reference architecture for the knowledge discovery and sensor fusion in the future IoT. To do so, KnaaS, in its current state of implementation, makes use of Node-RED's flow-based programming interface along with advanced scientific computing and data science libraries. To enable the execution of these knowledge discovery libraries from the Node-RED's visual programming interface a *Python Function Node* was added. As a result, most of the scientific computing and data science libraries that offer a Python API become accessible in a unified manner inside the KnaaS framework. At the same time, special consideration was given to the integration of Semantic Web Technologies. For that reason, a *SPARQL* Query Node was added that allows the direct extracting knowledge out of SPARQL endpoints.

* *UIaaS* aims at providing service composition and rdf integration framework and also user friendly end user dashboards.

### Getting Started

The project has successfully passed its early alpha state. The core functionality, i.e., 
[O-MI](https://github.com/skubler/Node-Red-OMI) and [O-DF](https://github.com/skubler/Node-Red-ODF) interfaces are created and tested to working, the linkage between main knowledge discovery and data maning libraries, such as: [SciPy](https://www.scipy.org/), [scikit-learn](http://scikit-learn.org/stable/), etc is enstablished and tested and, finally, special consideration was given to provide a storage mechanism. For this purpose, a [MongoDB](https://www.mongodb.com) database is being used.

### Prerequisites

Please install Docker following the installation guide for your platform: https://docs.docker.com/install/

### Building the project

Go to a command prompt and move to the ```~/knaas-uiaas``` directory and run the command

```
docker-compose up
```

This will locally bring up a preconfigured KnaaS framework exposed through a browser-based flow editing Node-RED environment and a MongoDB server. If everything worked well, you will be able to point your browser to:

* ```http://localhost:1880/```, which is the local Node-RED installation, and
* ```http://localhost:27017/```, which is the local MongoDB server for storing data and/or knowledge created by the KnaaS framework.
* ```http://localhost:8080/```, which is the local O-MI Node that provides KnaaS & UiaaS worflow.

### Deployment & Testing

We provide below a brief summary of the codebase's structure so as to easily deploy and test the bIoTope's KnaaS and UIaaS components in various use cases as described in the deliverables:

* [Deliverable D4.4](https://api.ning.com/files/2lCHlA6Jtw77ZCntCs4DT9FLTXkOdkxy93JbyYtn*z3Wgw2R6J754aJef1IqdjnAF6kQFeFtwIk6g3h1*rDOl4ZVjp6KsebE/D4.4.pdf) Framework for Knowledge Extraction from IoT Data Sources 
* Deliverable D4.8 Framework for Knowledge Extraction from IoT Data Sources v2
* [Deliverable D5.5](https://storage.ning.com/topology/rest/1.0/file/get/35619974?profile=original) Service Composition Framework v2

The various use cases are implemented under the folders: [flows](flows/) and [modules](modules/). With regard to the ```~/knaas-uiaas/modules``` folder, it hosts a python module which provides some abstractions that permit  the data cleaning and the querying of the MongoDB server to be performed in an easier way. The ```~/knaas-uiaas/flows``` folder host four flows, which can be imported to the Node-RED environment following the instruction described in the follow [link](https://nodered.org/docs/getting-started/first-flow).

Please not that in order to be able to deploy the flows, the needed credentials should be added inside the [modules](modules/config.yml) yaml configuration file.

### Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change. 

Please note we have a [code of conduct](CONTRIBUTING.md), please follow it in all your interactions with the project.



## Authors

* **Prodromos Kolyvakis** - *Initial design and implementation of KnaaS*
* **Christian Mader** - *Initial design and implementation of UIaaS*
* **Rohan Asmat** - *Initial design and implementation of UIaaS*

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project has been developed as part of the [bIoTope Project](http://www.biotope-project.eu), which has received funding from the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No. 688203.