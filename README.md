# IPL Score Prediction 
The IPL(Indian Premier League) Score Prediction Project aims to develop a data-driven methodology to predict the results of  matches using historical data and machine learning to provide insights to fans and participants during the IPL and predict the winner.

# Table Of Content
1. [Features of my project](https://github.com/KhushalKhare/software_development#features)
2. [Pre-Requisites](https://github.com/KhushalKhare/software_development#prerequisites)
3. [Code-File](https://github.com/KhushalKhare/software_development#code-file)
4. [Dataset](https://github.com/KhushalKhare/software_development#dataset)
5. [Requirements Engineering](https://github.com/KhushalKhare/software_development#requirement-engineering)
6. [UML](https://github.com/KhushalKhare/software_development#uml)
7. [DDD](https://github.com/KhushalKhare/software_development#DDD)
8. [Metrics](https://github.com/KhushalKhare/software_development/tree/main?tab=readme-ov-file#metrics)
9. [Clean Code Development](https://github.com/KhushalKhare/software_development?tab=readme-ov-file#clean-code-development)
10. [Unit Tests](https://github.com/KhushalKhare/software_development/blob/main/README.md#testing-and-test-units)
11. [Build Management](https://github.com/KhushalKhare/software_development/tree/main?tab=readme-ov-file#build-management)

# Features
1. Team Selection: Input the names of Team A and Team B that are playing against each other.
2. Current Score: Input what is the current runs made by team and current over and current wickets fallen and runs and wickets in the last 5 overs.
3. Predict Score: App will predict the score after 5 overs

# Prerequisites
Install Python on your computer or Download Python from [Python Link](https://www.python.org/)
Download Anacondas to acess jupyter notebook to write code in python here is the link [Anacondas](https://www.anaconda.com/download) or 
We can use Google Colab Notebooks [colab](https://colab.google/)

# Code File: 
To access the code and check how I created this project the link is given Below
[IPL Score Predictor Link](https://github.com/KhushalKhare/software_development/blob/main/Python%20File/IPL_Score_Prediction%20(2).ipynb)

# Dataset
The dataset plays a pivotal role in the project's functionality, encompassing 76,000 rows and 15 columns. Access the dataset here: [DataSet Link](https://github.com/KhushalKhare/software_development/blob/main/Data%20Set/ipl_data.csv)

# Requirement Engineering 
The process of gathering, documenting, and managing the requirements and expectations of stakeholders for a system or product is known as requirements engineering. The objective is to obviously characterize what the framework or item ought to do, guaranteeing that engineers get it and can meet those prerequisites.

For Professional Variant 
[Trello](https://trello.com/b/EDFAf9j3/ipl-score-card)
For Personal Variant
[Monday](https://khushalkhrs-team-company.monday.com/boards/1371201419)


# UML
For someone who is not familiar with coding,he or she can't understand how this project is working so for that we have UML which stands for Unified Modeling Language 
which describes the flow of project or how the project is working with the help of Flow Charts for example Class A then after excuting Class A it will go to Class B.
Since I have done only 50% of my code so till the part I have finished my code here the UML for this is here ![Screenshot 2023-11-30 224128](https://github.com/KhushalKhare/software_development/assets/148461152/a1c6787e-81c9-4e62-9bd2-9cb5695763d4)
UML for how our dataset is prepared for ML is here our step is to convert categorical values to numeric and here is the diagram![Screenshot 2023-12-03 154125](https://github.com/KhushalKhare/software_development/assets/148461152/3bb08b00-0343-48f0-b151-0359279b1ddc)

UML for ML Models which I will be using is here for understanding basically there are Three Models 
* Linear Regression

  ![Screenshot 2023-12-03 154804](https://github.com/KhushalKhare/software_development/assets/148461152/35c00314-428b-4782-b313-101685b88007)

* Random Forest
  
  ![Screenshot 2023-12-03 155002](https://github.com/KhushalKhare/software_development/assets/148461152/c56e3f4c-362b-4fbd-999a-a77bf8421ed1)


# DDD
DDD (Domain Driven Design) is very  similar to hosting a party or event. When understanding what you need for your domain, you can use real-world scenarios to help you understand. For example, I plan a party for my friends and think about what they need for the party: food, drinks, music, games, etc. Just like with software, you need to understand what you need from it 
features, libraries, etc. These are my domains which are the most important parts of the software or party. These are the requirements of the party or  the software and ultimately the requirements or needs 
we make plans. B. What food and drinks should be served at the party? Similarly, DDD creates a plan  for each piece of software, and groups may change the plan depending on the guest. Similarly, DDD changes the software plan  based on what the user needs and uses DDD's changes and adjustments to ensure that the software is useful and works well for the user.

**domain names for the code**:

**IPL Predictions**

**IPL Runs Predictor**

**IPL Match Prediction**

**IPL Analysis**

**IPL Insights**

**Cricket Analytics**

**IPL Machine Learning**

**IPL Data Science**

**IPL Sports Analytics**

**IPL Big Data**

Here is my relationship chart


Relational Diagram 

![Relational Diagram](https://github.com/KhushalKhare/software_development/assets/148461152/b91b562a-9e3b-46d4-9692-395944cc9e78)

Core Domain

![Core Domain](https://github.com/KhushalKhare/software_development/assets/148461152/6c240a36-566c-4a54-a4b8-0aedacb5d1cb)

Event Storming

![Event Storming](https://github.com/KhushalKhare/software_development/assets/148461152/bea2d12d-50bc-4bc7-8a78-732b5b192ff8)



## Metrics
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=KhushalKhare_Test1&metric=bugs)](https://sonarcloud.io/summary/new_code?id=KhushalKhare_Test1) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=KhushalKhare_Test1&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=KhushalKhare_Test1) [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=KhushalKhare_Test1&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=KhushalKhare_Test1) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=KhushalKhare_Test1&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=KhushalKhare_Test1)

Screenshot

The Badge screenshot if in the future the links for batch gets expired.
Screenshot for above

![Screenshot 2024-01-19 151725](https://github.com/KhushalKhare/software_development/assets/148461152/346f25ef-5d54-4fd7-a152-5a5988f0c39c)

## Clean Code Development

Clean Code Development refers to writing code that is easy to read, understand, and maintain. Delivering code that is correct, productive, efficient, and adheres to best practices is the goal. Clean code is easy for everyone to follow and understand; it's like an effective and unquestionable recipe. 

Here is my PDF that states why my code is clean 

[Clean Code Development.pdf](https://github.com/KhushalKhare/software_development/blob/main/Clean%20Code%20Development/Clean%20Code%20Development%20(4).pdf)


## Testing and Test Units

In computer programming, testing is a pivotal cycle to guarantee that a product application functions true to form and meets its necessities. It includes executing the product and noticing its way of behaving to track down any imperfections or issues. 

Here is my Test File [Testing File](https://github.com/KhushalKhare/software_development/blob/main/Testing/test_units%20(1).py) 

![Test Cases Run](https://github.com/KhushalKhare/software_development/assets/148461152/3d4b2c30-7301-4c58-b2b9-40d5032c4cb3)

## Build Management 

In software development, the process of assembling and compiling source code into an executable or deployable form is known as build management. It entails activities including managing dependencies, assembling source code, and producing the finished product that may be tested or given to customers. 

For my project, I used PyBuilder tool to check my build and build is sucessful here is the screenshot attached 
![Build Management](https://github.com/KhushalKhare/software_development/assets/148461152/ed5113e3-714a-48ff-8f67-6a7677e13e10)














