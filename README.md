# Assignment 7: Microservice Implementation (Milestone #2) + Publish Communication Contract to Partner

Please download all of the following packages in this repository.
There are two files you need to execute when implementing the microservice: CalcBudget.py and server.js

Instructions on how to REQUEST data from the microservice:

First, run server.js (on visual code). Enter 'npm install' in the terminal to download all the dependencies, then enter 'npm start' to run the program. This will have the server up listening on port 5000 for user input from the following step. Run CalcBudget.py (either on a separate terminal or using PyCharm). A window will pop up and prompt the user to enter the required input which will be submitted to the server as a URL request.

Instructions on how to RECEIVE data from the microservice:

The data is sent from CalcBudget.py via http protocol to the listening server. This URL request will create a JSON object on ther server's side. The JSON object will be displayed in the webpage that CalcBudget.py generated, in other words, received data through the webpage.

Here is the UML sequence diagram showing how the process works:

<img src="https://github.com/zhenjiam/cs361_microservice/blob/main/UML_Sequence_Diagram.png" width="600" height="700">

