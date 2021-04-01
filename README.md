# Loan-Prediction
Project consist of classification Problem. In this project we are using Lending Club Dataset. Using this Dataset we have to predict that Person who is applying for loan is defaulter or non defaulter. Lending Club, a San Francisco-based fintech company.
The data consists of all loan transactions issued in a span of 8 years from 2007 to 2015
The shape of dataset is 855969 rows and 81 variables. Their were lot of missing value in many variable so drop those columns who contain above 50% missing values after dropping those columns we have to handle missing values, we can handle those values by doing one hot coding or by handling feature by feature. 
After that I splitted variable in two categories i.e. categorical and numerical, after this plot boxplot, distplot and histogram to see the any outliers is present or not skewness of data. I always done visualization using Tableau public.
After this I perform categorical values to numerical values. I have done label encoding, importing preprossing library.
So as it is Time Series Data, Splitted data on bases on Yers, Training data – June 2007 to May 2015 (598978 records), Testing data – June 2015 to December 2015 (256991 records).Futher divided into X_train, y_train, X_test, y_test.
I build 4 model Logistic regression, SGD classifier, Decision Tree and Random forest.Logistic model is best among all other model.
After Building Logistic model we will save this model using pickle library in pickle format.
Then I have done model deployment using flask framework.
# Web Application
In this Web app you can apply for Individual Loan or Joint Loan.
After Applying Banker will fill all details. 
After clicking on Button 'Make Prection' It will Show all the Entered Details and Whether the person is Eligiblity of Loan.
If Person is Non-Defaulter then Loan gets Approved, and if person is Defaulter then Loan gets Denied.
Then can also visualization Lending Club Dataset.
