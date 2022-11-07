# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
The purpose of this project is to build a supervised learning model that will predict whether or not a loan would be approved. Eligibility is based on client details which were filled through an online application form. The details include the applicant's income, gender, marital status, education, number of dependents, and credit history.

## Hypothesis
-Applicants that have a good credit history are likely to get approved
-Applicants with higher applicant and coapplicant income
-Applicants with a higher level of education may earn more, and therefore more likely to be approved
-Number of dependents may affect eligibility due to less disposable income with more dependents
-Applicants who are not self-employed may have a more steady income

## EDA 
The amount of income that an applicant or coapplicant earns does not necessarily mean that the loan will be approved or denied. On average, applicants with higher education earn more and they are able to pay back a loan, yet they can still be denied. Other factors can also play a role in eligibility, such as, the number of dependents and credit history.

## Process
### Step 1
Hypothesis generation
### Step 2
Data exploration
### Step 3
Data cleaning
### Step 4 
Building a predictive model using pipeline
### Step 5
Model deployment

## Results/Demo
The model was built using logistci regression. The model accuracy score was 78%.

## Challanges 
Difficulty with deploying to AWS. Using pipeline with multiple different classifiers was also challenging, as it started to get disorganized with a few different pipelines, parameter grids, and grid searches.

## Future Goals
-develop more features
-play with hyperparameters