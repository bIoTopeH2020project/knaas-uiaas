# bIoTope's KnaaS(A Knowledge as a Service Framework in the IoT Era) and UIaaS(User Interface as a Service)

## KnaaS
KnaaS aims at providing a conceptual reference architecture for the knowledge discovery and sensor fusion in the future IoT. To do so, KnaaS in its current state of implementation makes use of Node-RED's flow-based programming interface along with advanced scientific computing and data science libraries. To enable the execution of these knowledge discovery libraries from the Node-RED's visual programming interface a Python Function Node was added. As a result, most of the scientific computing and data science libraries that offer a Python API become accessible in a unified manner inside the KnaaS framework.

## UIaaS
UIaaS aims at providing service composition and rdf integration framework and also user friendly end user dashboards.

## Project Status

The project is currently in early alpha state. It has not yet been extensively tested and automated tests are missing. However, the core functionality, i.e., 
[O-MI](https://github.com/skubler/Node-Red-OMI) and [O-DF](https://github.com/skubler/Node-Red-ODF) interfaces were created, the linkage between main knowledge discovery and data maning libraries, such as: [SciPy](https://www.scipy.org/), [scikit-learn](http://scikit-learn.org/stable/) is already enstablished and, finally, special consideration was given to provide a storage mechanism. For this purpose, a [MongoDB](https://www.mongodb.com) is being used.

## Building the project

Go to a command prompt and move to the ```~/knaas``` directory and run the command

```
docker-compose up
```

This will locally bring up a preconfigured KnaaS framework exposed through a browser-based flow editing Node-RED environment and a MongoDB server. If everything worked well, you will be able to point your browser to:

* ```http://localhost:1880/```, which is the local Node-RED installation, and
* ```http://localhost:27017/```, which is the local MongoDB server for storing data and/or knowledge created by the KnaaS framework.
* ```http://localhost:8080/```, which is the local O-MI Node that provides KnaaS worflow

## Application to Lyon’s Heat Wave Mitigation Pilot Use Case

The case study examined in Deliverable D4.4: Framework for Knowledge Extraction from IoT Data Sources is implemented under the folders: [flows](flows/) and [modules](modules/). With regard to the ```~/knaas/modules``` folder, it hosts a python module which provides some abstractions that permit  the data cleaning and the querying of the MongoDB server to be performed in an easier way. The ```~/knaas/flows``` folder host four flows, which can be imported to the Node-RED environment following the instruction described in the follow [link](https://nodered.org/docs/getting-started/first-flow).

In order to be able to deploy the flows, the needed credentials should be added inside the [modules](modules/config.yml) yaml configuration file.

## Future Work

Our immediate next steps will be to

* Implement automated tests
* Provide interactions between KnaaS and the [OORI](https://github.com/cmader/OORI) in a more uniform manner, through the adaptation of the already implemented mechanisms for performing SPARQL queries inside the KnaaS framework
* Extending further the reasoning and fusing mechanisms of the Knowledge Extraction framework
* Efficient handling of the semantic annotations within the O-DF messages

## Authors

* **Prodromos Kolyvakis** - *Initial design and implementation*

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This work was funded by the [bIoTope project](http://www.biotope-project.eu).
