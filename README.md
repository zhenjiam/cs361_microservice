# Assignment 7: Microservice Implementation (Milestone #2) + Publish Communication Contract to Partner

Please download all of the following packages in this repository.
There are two files you need to execute when implementing the microservice: CalcBudget.py and server.js

First run server.js (on visual code) by going to the directory containing this file and typing npm start in the terminal. This file is responsible for receiving the data from the microservice coded in CalcBudget.py and displaying it on localhost:5000.

Then run CalcBudget.py (either on a separate terminal or using PyCharm). A windo will pop up and request the user to input 2 data: (1) the remaining money they had after deducting the expenses, and (2) the time interval they want to set for their budget goal. Once the user clicks 'submit', the microservice will do the necessary calculations and the user should see the data received from the microservice on localhost:5000.

Here is the UML sequence diagram showing how the process works:
[UML Sequence Diagram](UML_seq_diagram.png)

