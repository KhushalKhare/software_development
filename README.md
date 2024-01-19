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
#### 1.1 Loading and Preprocessing of Data:
- **Requirement 1.1.1:** The system must be able to load a dataset from the specified CSV file.
- **Requirement 1.1.2:** The system must handle missing or incorrect values ​​in the dataset appropriately.
- **Requirement 1.1.3:** The system must convert both date and #039; column to datetime format.
-
-  - **Requirement 1.1.4:** Irrelevant columns like and#039;midand#039; and#039;local and#039; and#039;batsman and#039; and#039;bowleand#039; , and#039;strikerand#039; and and#039;non-attacker#039; must be removed.

#### 1.2 Research and Data Analysis:
- **Requirement 1.2.1:** The system must generate descriptive statistics from the uploaded data set.
- **Requirement 1.2.2:** The system must visualize the distribution of walks and runs using appropriate graphs.
- **Condition 1.2.3:** Only include matches with even teams (as defined in the code).

#### 1.3 Data Cleanup:
- **Condition 1.3.1:** Inconsistent teams must be removed from the dataset.
- **Condition 1.3.2:** Matches with less than 5 transitions should be removed from dataset.

#### 1.4 Machine Learning Model:
- **Requirement 1.4.1:** The system must be able to train and evaluate decision tree, linear regression, and random forest regression models.
- **Requirement 1.4.2:** Evaluation metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE) and RMSE (Root Mean Squared Error) must be calculated.
- ** Requirement 1.4.3:** Trained models must be able to predict.
-
-  #### 1.5 Prediction Function:
- **Requirement 1.5.1:** The system must have a function to predict results based on given input parameters like batting team, bowling team, innings, runs, score, runs_last_5 and wickets_last_5.

### 2. Non-functional requirements:

#### 2.1 Usability:
- ** Requirement 2.1.1:** The system must provide clear and concise documentation of the use of the prediction function.
- ** Requirement 2.1.2:** The user interface (if present) must be user-friendly.

#### 2.2 Performance:
- **Requirement 2.2.1:** The system must efficiently handle large data sets.
- ** Requirement 2.2.2:** Predictive response time must be reasonable for a given set of input parameters.

#### 2.3 Reliability:
- **Requirement 2.3.1:** The system must handle errors gracefully and provide informative error messages.
- **Requirement 2.3.2:** The prediction function must be reliable and consistent.

#### 2.4 Extensibility:
- **Requirement 2.4.1:** The system must allow easy addition of new functions or models.
- ** Requirement 2.4.2:** Code must be modular and well organized for easy maintenance.

### 3. Documentation:

#### 3.1 Code Documentation:
- **Condition 3.1.1:** All code must be properly documented and explain the purpose and functionality of each item.
- **Requirement 3.1.2:** Include inline comments for complex logic or unusual approaches.

#### 3.2 User Documentation:
- **Requirement 3.2.1:** Provide a user manual that explains how to run the code and use the prediction function.
- **Requirement 3.2.2:** Add examples to illustrate the predict function and its usage.

### 4. Testing:

#### 4.1 Hardware Testing:
- ** Requirement 4.1.1:** Carry out hardware tests to verify the correctness of individual functions and components.
- **Requirement 4.1.2:** Ensure machine learning models produce expected results.

#### 4.2 Integration testing:
- ** Requirement 4.2.1:** Perform integration tests to ensure that the various components of the system work well together.

### 5. Security:

#### 5.1 Privacy:
- **Condition 5.1.1:** Ensure that all sensitive or personal information is handled securely.
- **Condition 5.1.2:** Enable data anonymization if necessary.

### 6. Deployment:

#### 6.1 Deployment Script:
- **Requirement 6.1.1:** Provide a script or instructions for deploying the system to various environments.
-  [Trello](https://trello.com/b/EDFAf9j3/ipl-score-card)


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


![DDD](https://github.com/KhushalKhare/software_development/assets/148461152/b91b562a-9e3b-46d4-9692-395944cc9e78)

## Metrics

Screenshot for above

![Screenshot 2024-01-19 151725](https://github.com/KhushalKhare/software_development/assets/148461152/346f25ef-5d54-4fd7-a152-5a5988f0c39c)


[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=KhushalKhare_Test1&metric=bugs)](https://sonarcloud.io/summary/new_code?id=KhushalKhare_Test1) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=KhushalKhare_Test1&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=KhushalKhare_Test1) [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=KhushalKhare_Test1&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=KhushalKhare_Test1) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=KhushalKhare_Test1&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=KhushalKhare_Test1)

## Clean Code Development

Clean code advancement alludes to composing code that is not difficult to peruse, straightforward, and simple to keep up with. The objective is to deliver code that capabilities accurately as well as efficient, productive, and follows best practices. Clean code resembles an efficient and indisputable recipe; it's simple for anybody to follow and comprehend. 

Here is my PDF that states why my code is clean [Clean Code Development.pdf](https://github.com/KhushalKhare/software_development/blob/main/Clean%20Code%20Development%20(2).pdf)











