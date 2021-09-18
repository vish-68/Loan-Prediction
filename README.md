
# Lending Club – Loan Default Prediction

In general, whenever an individual/corporation applies for a loan 
from a bank (or any loan issuer), their credit history undergoes 
a rigorous check to ensure that whether they are capable enough 
to pay off the loan (in this industry it is referred to as 
credit-worthiness). 

The issuers have a set of models and rules in place which take 
information regarding their current financial standing, previous 
credit history and some other variables as input and output a 
metric which gives a measure of the risk that the issuer will 
potentially take on issuing the loan. The measure is generally 
in the form of a probability and is the risk that the person will 
default on their loan (called the probability of default) in the 
future.

Based on the amount of risk that the issuer is willing to take 
(plus some other factors) they decide on a cutoff of that score 
and use it to take a decision regarding whether to pass the loan 
or not. This is a way of managing credit risk. The whole process 
collectively is referred to as underwriting.

## Data Analysis

In Lending Club – Loan Default Prediction dataset we are provided 73 features(including target 
variable) and 855969 records.

* addr_state : The state provided by the borrower in the loan application
* annual_inc : The self-reported annual income provided by the borrower during registration.
* annual_inc_joint : The combined self-reported annual income provided by the co-borrowers during registration
* application_type : Indicates whether the loan is an individual application or a joint application with two co-borrowers
* collection_recovery_fee : post charge off collection fee
* collections_12_mths_ex_med : Number of collections in 12 months excluding medical collections
* delinq_2yrs : The number of 30+ days past-due incidences of delinquency in the borrower's credit file for the past 2 years
* desc : Loan description provided by the borrower
* dti : A ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested loan, divided by the borrower’s self-reported monthly income.
* dti_joint : A ratio calculated using the co-borrowers' total monthly payments on the total debt obligations, excluding mortgages and the requested loan, divided by the co-borrowers' combined self-reported monthly income
* earliest_cr_line : The month the borrower's earliest reported credit line was opened
* emp_length : Employment length in years. Possible values are between 0 and 10 where 0 means less than one year and 10 means ten or more years. 
* emp_title : The job title supplied by the Borrower when applying for the loan.
* funded_amnt : The total amount committed to that loan at that point in time.
* funded_amnt_inv : The total amount committed by investors for that loan at that point in time.
* grade : XYZ corp. assigned loan grade
* home_ownership : The home ownership status provided by the borrower during registration. Our values are: RENT, OWN, MORTGAGE, OTHER.
* id : A unique assigned ID for the loan listing.
* initial_list_status : The initial listing status of the loan. Possible values are – W, F
* inq_last_6mths : The number of inquiries in past 6 months (excluding auto and mortgage inquiries)
* installment : The monthly payment owed by the borrower if the loan originates.
* int_rate : Interest Rate on the loan
* issue_d : The month which the loan was funded
* last_credit_pull_d : The most recent month XYZ corp. pulled credit for this loan
* last_pymnt_amnt : Last total payment amount received
* last_pymnt_d : Last month payment was received
* loan_amnt : The listed amount of the loan applied for by the borrower. If at some point in time, the credit department reduces the loan amount, then it will be reflected in this value.
* loan_status : Current status of the loan
* member_id : A unique Id for the borrower member.
* mths_since_last_delinq : The number of months since the borrower's last delinquency.
* mths_since_last_major_derog : Months since most recent 90-day or worse rating
* mths_since_last_record : The number of months since the last public record.
* next_pymnt_d : Next scheduled payment date
* open_acc : The number of open credit lines in the borrower's credit file.
* out_prncp : Remaining outstanding principal for total amount funded
* out_prncp_inv : Remaining outstanding principal for portion of total amount funded by investors
* policy_code : "publicly available policy_code=1
  new products not publicly available policy_code=2"
* pub_rec : Number of derogatory public records
* purpose : A category provided by the borrower for the loan request. 
* pymnt_plan : Indicates if a payment plan has been put in place for the loan
* recoveries : post charge off gross recovery
* revol_bal : Total credit revolving balance
* revol_util : Revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit.
* sub_grade : XYZ assigned assigned loan subgrade
* term : The number of payments on the loan. Values are in months and can be either 36 or 60.
* title : The loan title provided by the borrower
* total_acc : The total number of credit lines currently in the borrower's credit file
* total_pymnt : Payments received to date for total amount funded
* total_pymnt_inv : Payments received to date for portion of total amount funded by investors
* total_rec_int : Interest received to date
* total_rec_late_fee : Late fees received to date
* total_rec_prncp : Principal received to date
* verified_status_joint : Indicates if the co-borrowers' joint income was verified by XYZ corp., not verified, or if the income source was verified
* zip_code : The first 3 numbers of the zip code provided by the borrower in the loan application.
* open_acc_6m : Number of open trades in last 6 months
* open_il_6m : Number of currently active installment trades
* open_il_12m : Number of installment accounts opened in past 12 months
* open_il_24m : Number of installment accounts opened in past 24 months
* mths_since_rcnt_il : Months since most recent installment accounts opened
* total_bal_il : Total current balance of all installment accounts
* il_util : Ratio of total current balance to high credit/credit limit on all install acct
* open_rv_12m : Number of revolving trades opened in past 12 months
* open_rv_24m : Number of revolving trades opened in past 24 months
* max_bal_bc : Maximum current balance owed on all revolving accounts
* all_util : Balance to credit limit on all trades
* total_rev_hi_lim : Total revolving high credit/credit limit
* inq_fi : Number of personal finance inquiries
* total_cu_tl : Number of finance trades
* inq_last_12m : Number of credit inquiries in past 12 months
* acc_now_delinq : The number of accounts on which the borrower is now delinquent.
* tot_coll_amt : Total collection amounts ever owed
* tot_cur_bal : Total current balance of all accounts
* verification_status : Was the income source verified

## Approach

Our Main goal is to know that whether which applicant 
it belong to defaulter or non-defaulter.

* Data Exploration : Exploring dataset using pandas,numpy,matplotlib and seaborn.
* Data visualization : Use Tableau Data visualizationtools and also Ploted graphs to get insights about dependend and independed variables.
* Model Selection I : Tested all base models to check the base accuracy. Also ploted and calculate Performance Metrics to check whether a model is a good fit or not.
* Model Selection II : After testing all base if some of them are not working properly then we have to do model tunning
* Pickle File : Selected model as per best accuracy and created pickle file using pickle library.
* Webpage & deployment : Created a webform that takes all the necessary inputs from user and shows output. After that I have deployed project on Herokuapp 
## Technologies Used

* Jupyter notebook, Spyder, VScode Is Used For IDE.
* For Visualization Of The Plots Matplotlib , Seaborn Are Used.
* Herokuapp is Used For Model Deployment.
* Front End Deployment Is Done Using HTML, CSS, Bootstrap.
* Flask is for creating the application server and pages.
* Git Hub Is Used As A Version Control System.
* os is used for creating and deleting folders.
* csv is used for creating .csv format file.
* numpy is for arrays computations and mathematical operations
* pandas is for Manipulation and wrangling structured data
* scikit-learn is used for machine learning tool kit
* pickle is used for saving model
* Logistic Regression is used for LogisticRegression Implementation.
* Decision Tree is used for DecisionTreeClassifier Implementation.
* Random Forest is used for RandomForestClassifier Implementation.
* SGD is used for SGDClassifier Implementation.
  
## Deployment

**Herokuapp Link:** https://loan-prediction-webapplication.herokuapp.com/
  
## Deployment

To Clone this project run

```bash
git clone https://github.com/vish-68/Loan-Prediction
```
Go to Project directory
```bash
cd Loan-Prediction
```
Install dependencies
``` bash
pip install -r requirements.txt
```  
Run the app.py
```bash
python app.py
```
## Conclusion
We have developed Lending Club – Loan Default Predictive model 
which is capable for predicting wheater the applicant is Non-
Defaulter or Defaulter. In this dataset we have 73 features
(including target variable). First step is to check wheater the 
dataset contain missing values or not. We have drop those 
Features which has more than 50% of missing values. And one 
who is less than 50% those variable should be treated using fillna 
mode(for categorical variable) and mean(for numerical variable).
Second step is to do some data visualization to get some insight
from given data after handling missing values. We can plot 
Co-relation plot for auto-corelation and boxplot for outliers 
detection. By looking at co-relation plot some of the variable
having same values of the other, so in this case we have to delete
any one of them. After doing all this things Machine Learning
comes in the picture. As this dataset is Supervised Classification
Machine Learning. Before building ML model we have to convert 
categorical variable to numerical variable, after converting 
categorical to numerical we have to do scaling, we perform 
Standard Scalar(values lies between -3 to +3) and then we have 
to build ML model likes Logistic Regression, Decision Tree, 
Random Forest & SGD. Out of all of them Logistic Regression 
was working good because Accuracy achieved – 99.98%, 
Type 1 error – 0, Type 2 error – 64. and SGD achieved Accuracy 
achieved – 99.95%, Type 1 error – 48, Type 2 error – 68. So here 
we can say Logistic Regression model is working good as compared 
SGDClassifier. Last step is model Deployment using Flask Framework.
For model deployment we have to dump our model using pickle library
and can save our model in .pkl or .sav extension.
