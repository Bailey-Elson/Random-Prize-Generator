# SFIA2

1. Brief 
    * Objective
    * Requirements
2. Project Plan
    * Kanban Board
    * Sprints
3. Risk Assesment 
4. My Soloution
    * Initial Plan
    * Initial Diagrams
    * End Plan
    * End Diagrams
5. Testing
6. Development
   * CI Pipeline
7. Evaluation 
8. Future Implementations 

---
## Brief

#### Objective
Architecture  
You are required to create a micro-service orientated architecture for your application, this application must be composed of at least 4 services that work together. 
Service #1 
The core service – this will render the Jinja2 templates you need to interact with your application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database. 
Service #2 + #3 
These will both generate a random “Object” 
Service #4 
This service will create an “Object” based upon the results of service #2 + #3

#### Requirements
   * Kanban Board with full expansion on tasks needed to complete the project
   * An Application fully integrated using the Feature-Branch model into a Version Control System
   * CI server with webhooks
   * Deployed to a cloud-based virtual machine
   * Follow the Micro Services architecture 
   * Deployed using containerisation and an orchestration tool
   * Create an Ansible Playbook that will provision the environment that your application needs to run
   
---
## Project Plan 
#### Kanban Board
#### Sprints
---
## Risk Assesment 
---
## My Soloution 
#### Initial Plan

A radnom prize generator 
Service #1:
   * Renders HTML and Jinja user interface
   * Calls service #4 to start the generation of prize
   * Stores the prize in a SQL database
   
Service #2:
   * Generates the typr of prize (good, average, bad)
   
Service #3:
   * Generates the prize from a list based on the prize type
   
Service #4:
   * Calls service #2 and #3 
   * Generates the output sentence based on service #2 and #3 return values

#### Initial Diagrams
###### Application flowchart 

![Imgur](https://i.imgur.com/HY5Uuab.png)

The flow chart above shows the initail plan for the layout of my application. With the flow chart split into the four different services. In the case of the above flowchart start refers to when the user interface(webpage) is loaded for the first time.

###### Database Diagram

![Imgur](https://i.imgur.com/TxSAPlV.png)

The above diagram shows my database layout. As you only need to to show the functiomnality of persisting some data into a SQL databse i have opted to keep my databse simple to begin with, with the option to expand on it later. To begin with I will only have onr table inside my database with only two coloumns. The first coloumn is ID which is the primary key and auto increments. The second coloumn is prize which stores the outputted sentence that the application generates.

###### User Interface Design

![Imgur](https://i.imgur.com/QSudWix.png)

The above image is my inital design for the user interface. As a complicated or aesthetically pleasing user interface is not required for this project i have decided to keep the user interface simple and streamlined only containing the bare necessities for the applicaion to run so that i can focus more on the parts of the project that are more important. I have the option to redesign the user interface at a late date if time permits.

#### End Plan
#### End Diagrams
###### Application Flowchart

![Imgur](https://imgur.com/mClk69s.png)

From my initial plan to my end plan the only significant change was within service 3. Instead of randomly selecting a prize from three different list variables, within python, based on the prize type, the application now accesses a csv file that contains three rows. The csv file will contain all the different prizes split by the prize type into three different rows. 

---
## Testing

My testing will be split into three main areas. These three sections are URL testing, database testing and finally CSV file testing. 

###### URL Testing

![Imgur](https://imgur.com/9vm4mhl.png)

Above is an example of one of the URL tests. Every URL test is done for both the manager and the worker node. These various different tests are checking the ability to access the ip address and checks if the connection was succesful or not.

###### Database Testing 

![Imgur](https://imgur.com/HX3tRCv.png)

Above is one example of a databse test. The various different datasbae tests are there to check the ability to connect to the databse succesfully and then has the ability to succesfully complete CRUD functions.

###### CSV File Testing 

![Imgur](https://imgur.com/SroYUKw.png)

Above is an example of a CSV file test. The CSV file tests are checking that the file can be succesfully accessed and then the tests are checking if its the correct file with the correct about of rows and coloumns.

---
## Development 
#### CI Pipeline 
---
## Evaluation 
---
## Future Implementations

###### User Iterface Redeisgn 

![Imgur](https://i.imgur.com/iOV6uuy.png)

The above image is a rough design for a new user interface. This new design is more aesthetically pleasing then then the old design while keeping all the applications functionality. 

###### Expanded Database

![Imgur](https://i.imgur.com/gtfJFhj.png)

The above diagram is a rough design for an expanded database. Firstly i have expanded the Prizes table so that the data is store in two different coloumns (PrizeType and Prize) instead of everything being stored in the single prize coloumn. Also two new tables have been added, firstly a Users table storing a users details. For the Users table to be added service #1 and the user interface would have to be editted for extra inputs (FirstName, LastName and UserName) to be entered every time a prize is generated or a log in feature added. The second table User_Prizes is a joining table between the two, with this table have a many to many relatioship with both the others.

---

