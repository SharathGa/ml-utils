''' 
This contains all the reusable code that I need for ML 
'''


''' importing the necessary packages for the analysis '''
import pandas as pd 
import numpy as np 

#first eda function for preliminary analysis 
# class klassifyer(object):

"""
	These are the commonly used functions that we need for
	classfication problems and for test and analysis.
	The following are list of functions available in this class
	1.eda
	2.
"""


def eda(df):
    #wrting a funciton to do the basic necessary eda analysis of a dataframe
    
    #checking the shape of the data
    print('The dimensions of the data is:')
    print(df.shape,'\n')
   
    
    #listing the name of the columns 
    print('The column names are:')
    print(df.columns,'\n')

    
    #inspecting the head and tail of a df 
    print('The head and tail of a df:')
    cf = pd.concat([df.head(), df.tail()],axis = 0 )
    print(cf,2*'\n')
  
    
    #checking the type of the columns
    print('The the following is the info: ')
    print(df.info(),2*'\n')
   
    
    #checking the total missing values columnwise
    print('the total column wise missing values are: ')
    print(df.isnull().sum(),2*'\n')
    
 

#replacing values in function
def replace_val(df, column , dictionary,fill_na= True):
	''' 
	This function is used to replace/map values from the column with
	the mappings given in the dict and if fillna is true , replace the 
	categorical variables with the mode of that column and for continous 
	variables replace it with mean of the data in that column 
	'''
	if type(df['column']=='object'):
		if fillna=='True':
			df.column.map(dictionary).fillna(df.column.mean())
		else
		
		



	





    

