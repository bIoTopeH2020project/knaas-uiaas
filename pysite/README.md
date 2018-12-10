# Web Based Python IDE Documentation

## Introduction
Through this project, we are adding a web based Python IDE that allows users to write their python code, load files that they have already created, check that their code works, as it should, by using (a) an interactive screen, (b) a debugger or (c) running directly their code and showing its output, and last but not least, letting them save the code and import it directly to Node-Red. 

The web based Python IDE's implementation is based on [Skulpt](https://github.com/skulpt/skulpt) but goes one step further by adding new capabilities, such as loading/storing files, providing a common Web-based IDE, and many more.

## Technologies used in the Web based Python IDE
We provide below a brief description of the technologies that we used and how these interact, so as to improve the user experience and how we can integrate this work with the Node Red environment.

### Skulpt
Skulpt is a tool that allows to write and run python code in the browser. We took advantage of this opportunity but trying to adapt the  web better to our neeeds:

* Changing the interface by reorganazing the screens in columns.
* Letting the output screen to show also the errors that appeared when the code is executed.
* Adding a new iframe that allows users to search for more information
* Removing the previous output when the code is newly executed.
* Creating new buttons and functions to gain new functionalities.

### Node.js Added Modules
We have created different buttons to get new functionalities in our site. For example using the button Initial Page of the iframe, the user can go directly to the google search from wherever he might have gone.
However, there are two functions that deserve to be studied with more detail. These are the ones related with the inputs and buttons of **"Save text to File"** and **"Load"**.

#### Save Text to File
When you press this botton, the next steps are processed internally:

First, the text that is written in the editor  screen is read using **editor.getValue()**. The text that is written in the input box is also read using **document.getElementById(id)**. Then two separate processes start simultaneously.

One of them, just initializes a download with the name of the input box and with the code that was written in the editor screen. This is okay because we can get the text in a file in the downloads directory, however it is nos accesible for Node-Red.

The second and most important one, sends the data to one url that we have specified, being  data.body.filename the text written in the input box and data.body.content the text of the editor screen. 

#### Load
The Load button runs a javascript function that basically removes the text that was written in the editor screen, reads the input box and sends its contents to the url that we have specified. After that it stays listening to the url to see if it receives something.

If it does, it directly writes in the editor screen the contents that it has received using **editor.setValue(contents)**.

## Miscellaneous

In order to gain speed and improve our experience, we have created one python file located in the directory *knaas-uiaas/misc* called commands.py with some automated functions that may be run as follows:

```
- python -c 'from commands import run; run()' (initializes the swarm and run our service)
- python -c 'from commands import stopall; stopall()' (to leave the swarm and stop all the containers)
- python -c 'from commands import stop; stop("x")' (stop a container)
- python -c 'from commands import modi; modi("x")' (builds automatically one image and makes it run)
```
  Where x refers to the name of the image we want to work with, in our case firstimage (web), nodeimage (nodesjs), node-red (Node RED), o-mi-node (dataLyon), mongo (mongodb).
          
## Future Improvements
- Further extension of Skulpt with new modules.
- Adding auto-completion
- Further testing 
