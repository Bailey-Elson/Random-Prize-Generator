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
#### End Plan
#### End Diagrams
---
## Testing
---
## Development 
#### CI Pipeline 
---
## Evaluation 
---
## Future Implementations
---
