# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:04:41 2021

@author: VISHAL
"""

#%%

#importing libraries:
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

#%%

app=Flask(__name__)

#%%

model=pickle.load(open('log_model.pkl','rb'))

#%%

@app.route('/')
def home():
    return render_template('home.html')
#%%
term_to_int={0:"36 Months",1:"64 Months"} 
   
application_type={0:"Individual",1:"Joint"}

grade={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G"}

sub_grade={0:"A1",1:"A2",2:"A3",3:"A4",4:"A5",
           5:"B1",6:"B2",7:"B3",8:"B4",9:"B5",
           10:"C1",11:"C2",12:"C3",13:"C4",14:"C5",
           15:"D1",16:"D2",17:"D3",18:"D4",19:"D5",
           20:"E1",21:"E2",22:"E3",23:"E4",24:"E5",
           25:"F1",26:"F2",27:"F3",28:"F4",29:"F5",
           30:"G1",31:"G2",32:"G3",33:"G4",34:"G5"}

emp_length={0:"1 Year",1:"10+ Years",2:"2 Years",3:"3 Years",4:"4 Years",5:"5 Year",
            6:"6 Years",7:"7 Years",8:"8 Years",9:"9 Years",10:"< 1 Year"}

home_ownership={0:"Mortage",1:"Others",2:"Own",3:"Rent"}

verification_status={0:"Income Source Verified",1:"Not Verified",2:"Verified"}

purpose={0:"Car",1:"Credit Card",2:"Dept Consolidation",3:"Educational",4:"Home Improvement",
         5:"House",6:"Major Purpose",7:"Medical",8:"Moving",9:"Others",10:"Renewable Energy",
         11:"Small Business",12:"Vacation",13:"Wedding"}

addr_state={0:"Alaska",1:"Alabama",2:"Arkansas",3:"Arizona",4:"California",5:"Colorado",
            6:"Connecticut",7:"District of Columbia",8:"Delaware",9:"Florida",10:"Georgia",
            11:"Hawaii",12:"Iowa",13:"Idaho",14:"Illinois",15:"Indiana",16:"Kansas",
            17:"Kentucky",18:"Louisiana",19:"Massachusetts",20:"Maryland",21:"Maine",
            22:"Michigan",23:"Minnesota",24:"Missouri",25:"Mississippi",26:"Montana",
            27:"North Carolina",28:"North Dakota",29:"Nebraska",30:"New Hampshire",
            31:"New Jersey",32:"New Mexico",33:"Nevada",34:"New York",35:"Ohio",36:"Oklahoma",
            37:"Oregon",38:"Pennsylvania",39:"Rhode Island",40:"South Carolina",41:"South Dakota",
            42:"Tennessee",43:"Texas",44:"Utah",45:"Virginia",46:"Vermont",47:"Washington",
            48:"Wisconsin",49:"West Virginia",50:"Wyoming"}

initial_list_status={0:"Fractional",1:"Whole"}

#%%
    
@app.route("/Individual", methods=['GET', 'POST'])
def Individual():
    if request.method == 'GET':
        return render_template('individual.html')
    
    if request.method =='POST':
        int_features=[int(x) for x in request.form.values()]
        final_features=[np.array(int_features)]
        prediction=model.predict(final_features)
        
        
        
        data2=request.form["loan_amnt"]
        data3=request.form["term"]
        data4=request.form["int_rate"]
        data5=request.form["installment"]
        data6=request.form["grade"]
        data7=request.form["sub_grade"]
        data8=request.form["emp_length"]
        data9=request.form["home_ownership"]
        data10=request.form["annual_inc"]
        data11=request.form["verification_status"]
        data12=request.form["purpose"]
        data13=request.form["addr_state"]
        data14=request.form["dti"]
        data15=request.form["delinq_2yrs"]
        data16=request.form["inq_last_6mths"]
        data17=request.form["open_acc"]
        data18=request.form["pub_rec"]
        data19=request.form["revol_bal"]
        data20=request.form["revol_util"]
        data21=request.form["total_acc"]
        data22=request.form["initial_list_status"]
        data23=request.form["out_prncp"]
        data24=request.form["out_prncp_inv"]
        data25=request.form["total_pymnt"]
        data26=request.form["total_rec_prncp"]
        data27=request.form["total_rec_int"]
        data28=request.form["total_rec_late_fee"]
        data29=request.form["last_pymnt_amnt"]
        data30=request.form["collections_12_mths_ex_med"]
        data31=request.form["application_type"]
        data32=request.form["acc_now_delinq"]
        data33=request.form["tot_coll_amt"]
        data34=request.form["tot_cur_bal"]
        
        
        
    
        
        #create original output dict
        output_dict= dict()
        output_dict['Desired Loan Amount']=data2
        output_dict['Term (in Months)']=term_to_int[int(data3)]
        output_dict['Interest Rate on the loan']=data4
        output_dict['Installment']=data5
        output_dict['Grade']=grade[int(data6)]
        output_dict['Sub Grade']=sub_grade[int(data7)]
        output_dict['Employee Length']=emp_length[int(data8)]
        output_dict['Home Ownership']=home_ownership[int(data9)]
        output_dict['Annual Income']=data10
        output_dict['Verification Status']=verification_status[int(data11)]
        output_dict['Loan Purpose']=purpose[int(data12)]
        output_dict['Address State']=addr_state[int(data13)]
        output_dict['Total Debt Obligation Income']=data14
        output_dict['Delinquency for the past 2 years']=data15
        output_dict['Inquiries in past 6 months (excluding auto and mortgage inquiries)']=data16
        output_dict["Number of open credit lines in the borrower's credit file"]=data17
        output_dict['Number of derogatory public records']=data18
        output_dict['Total credit revolving balance']=data19
        output_dict['Revolving line utilization rate']=data20
        output_dict["Total number of credit lines currently in the borrower's credit file"]=data21
        output_dict['Initial List Status']=initial_list_status[int(data22)]
        output_dict['Remaining outstanding principal for total amount funded']=data23
        output_dict['Remaining outstanding principal for portion of total amount funded by investors']=data24
        output_dict['Payments received to date for total amount funded']=data25
        output_dict['Principal received to date']=data26
        output_dict['Interest received to date']=data27
        output_dict['Late fees received to date']=data28
        output_dict['Last total payment amount received']=data29
        output_dict['Number of collections in 12 months excluding medical collections']=data30
        output_dict['Application Type']=application_type[int(data31)]
        output_dict['Number of accounts on which the borrower is now delinquent']=data32
        output_dict['Total collection amounts ever owed']=data33
        output_dict['Total current balance of all accounts']=data34
    
        return render_template('individualresult.html',original_input=output_dict,data=prediction)
#%%
    
@app.route("/Joint", methods=['GET', 'POST'])
def Joint():
    
    if request.method == 'GET':
        return render_template('joint.html')
    
    if request.method =='POST':
        
        int_features=[int(x) for x in request.form.values()]
        final_features=[np.array(int_features)]
        prediction=model.predict(final_features)
        
        
        
        data2=request.form["loan_amnt"]
        data3=request.form["term"]
        data4=request.form["int_rate"]
        data5=request.form["installment"]
        data6=request.form['grade']
        data7=request.form["sub_grade"]
        data8=request.form["emp_length"]
        data9=request.form["home_ownership"]
        data10=request.form["annual_inc"]
        data11=request.form["verification_status"]
        data12=request.form["purpose"]
        data13=request.form["addr_state"]
        data14=request.form["dti"]
        data15=request.form["delinq_2yrs"]
        data16=request.form["inq_last_6mths"]
        data17=request.form["open_acc"]
        data18=request.form["pub_rec"]
        data19=request.form["revol_bal"]
        data20=request.form["revol_util"]
        data21=request.form["total_acc"]
        data22=request.form["initial_list_status"]
        data23=request.form["out_prncp"]
        data24=request.form["out_prncp_inv"]
        data25=request.form["total_pymnt"]
        data26=request.form["total_rec_prncp"]
        data27=request.form["total_rec_int"]
        data28=request.form["total_rec_late_fee"]
        data29=request.form["last_pymnt_amnt"]
        data30=request.form["collections_12_mths_ex_med"]
        data31=request.form["application_type"]
        data32=request.form["acc_now_delinq"]
        data33=request.form["tot_coll_amt"]
        data34=request.form["tot_cur_bal"]
        
        
        
        #create original output dict
        output_dict= dict()
        output_dict['Desired Loan Amount']=data2
        output_dict['Term (in Months)']=term_to_int[int(data3)]
        output_dict['Interest Rate on the loan']=data4
        output_dict['Installment']=data5
        output_dict['Grade']=grade[int(data6)]
        output_dict['Sub Grade']=sub_grade[int(data7)]
        output_dict['Employee Length']=emp_length[int(data8)]
        output_dict['Home Ownership']=home_ownership[int(data9)]
        output_dict['Annual Income']=data10
        output_dict['Verification Status']=verification_status[int(data11)]
        output_dict['Loan Purpose']=purpose[int(data12)]
        output_dict['Address State']=addr_state[int(data13)]
        output_dict['Total Debt Obligation Income']=data14
        output_dict['Delinquency for the past 2 years']=data15
        output_dict['Inquiries in past 6 months (excluding auto and mortgage inquiries)']=data16
        output_dict["Number of open credit lines in the borrower's credit file"]=data17
        output_dict['Number of derogatory public records']=data18
        output_dict['Total credit revolving balance']=data19
        output_dict['Revolving line utilization rate']=data20
        output_dict["Total number of credit lines currently in the borrower's credit file"]=data21
        output_dict['Initial List Status']=initial_list_status[int(data22)]
        output_dict['Remaining outstanding principal for total amount funded']=data23
        output_dict['Remaining outstanding principal for portion of total amount funded by investors']=data24
        output_dict['Payments received to date for total amount funded']=data25
        output_dict['Principal received to date']=data26
        output_dict['Interest received to date']=data27
        output_dict['Late fees received to date']=data28
        output_dict['Last total payment amount received']=data29
        output_dict['Number of collections in 12 months excluding medical collections']=data30
        output_dict['Application Type']=application_type[int(data31)]
        output_dict['Number of accounts on which the borrower is now delinquent']=data32
        output_dict['Total collection amounts ever owed']=data33
        output_dict['Total current balance of all accounts']=data34
    
        return render_template('jointresult.html',original_input=output_dict,data=prediction)
#%%
    
if __name__=='__main__':
    app.run(debug=True)
