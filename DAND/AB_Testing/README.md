# A/B Testing using Linear Regression Model

This project is to predict whether the company has to launch the New updated page 
to all users based the conversion rate from one set of group. I crated the model with `converted` columns as 
response variable and `group` & `landing_page` columns as explanatory variables

>Please take a look on "**Analyze_ab_test_results_notebook.html**" file to know more about this project

Data used in this project is ab_data.csv & countries.csv provided by UDACITY.

For this project:

> I have import the required libraries and performed basic EDA to make the data error free

This Project is divide into 3 parts to better understand the process:

> **Part I** 
    >> Exploratory Data Analysis on the Data from `ab_data.csv` file
    >> Proportion of the converted rate for each page
	>> Probability of the New Page
	
> **Part II**
	>>  We described our Hypothesis 
	>> Simulated the transactions and conversion rate of New Page to get the preducted and difference
	>> Plotted the diference in a Nice Histogram chart
	>> Obtained the **p-value**
	>> Applied built in stats moded from numpy and obtained the **z-score** and **p-value**

>**Part III**
	>> Created a simple linear regression model with single explanatory variable and obtained **p-value**
	>>Created a  mulit linear regression model by merging the country from `countries.csv` file and obtained **p-value**
	
	
## Conclusion:

   Using the model we found that we were not able to reject the null hypothesis.
