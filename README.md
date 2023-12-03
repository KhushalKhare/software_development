# IPL Score Prediction 
The IPL(Indian Premier League) Score Prediction Project aims to develop a data-driven methodology to predict the results of  matches using historical data and machine learning to provide insights to fans and participants during the IPL and predict the winner

# Features
1. Team Selection: Input the names of Team A and Team B that are playing against each other.
2. Current Score: Input what is the current runs made by team and current over and current wickets fallen and runs and wickets in the last 5 overs.
3. Predict Score: App will predict the score after 5 overs

# Prerequisites
Install Python on your computer or Download Python from [Python Link](https://www.python.org/)

# Code File: 
To access the code and check how I created this project the link is given Below
[IPL Score Predictor Link](https://github.com/KhushalKhare/software_development/blob/main/Python%20File/IPL_Score_Prediction%20(1).ipynb)

# Dataset
The dataset plays a pivotal role in the project's functionality, encompassing 76,000 rows and 15 columns. Access the dataset here: [DataSet Link](https://github.com/KhushalKhare/software_development/blob/main/Data%20Set/ipl_data.csv)

# Requirement Engineering 
For every project, whether building a Python project or making a pizza, there are some requirements. For example, in my project, there are the main requirements mentioned below.
1. Data: As we already have our data in CSV File and it contains historical IPL matches from 2008 to 2017.
2. Tools and Resources: We need Python Programming Language,Libraries such as
   * Pandas
   * Numpy
   * Matplotlib / Seaborn
3. Domain Knowledge: Familiarity with the Indian Premier League (IPL), its teams, players, and rules of the game.Understanding of factors that influence match outcomes.
   Knowledge of cricket analytics and how it is applied to predict match outcomes. Understanding of machine learning concepts,
   including regression, classification, and feature engineering.

4. Evaluation Metrics:
  * Mean Absolute Error (MAE)
  * Root Mean Squared Error (RMSE)
  * Mean Percentage Error (MPE)

5. Preparing Data for Machine Learning:
  * Library such as LabelEncoder from sklearn.preprocessing will convert categorical values into numerical values
  * Use ColumnEncoder on your columns'bat_team', 'bowl_team' using LabelEncoder and OneHotEncoder
  * train_test_split library is needed to split dataset into training and testing
6. Machine Learning
  * Will perform few algorithms such as Linear Regression,Random Forest Classifier, KNN Classifier to implement it we need libraries like
    from sklearn.linear_model import LinearRegression,from sklearn.ensemble import RandomForestRegressor and from sklearn.neighbors import KNeighborsClassifier
7. Deployment of ML Model in WebPage
  * HTML,CSS for creating a web page
  * TensorFlow will be used to deploy ML Model in the browser.
8. Further More Details Here is a link of Trello Software which timelines and how much progress is completed here is the link [Trello](https://trello.com/b/EDFAf9j3/ipl-score-card)


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







