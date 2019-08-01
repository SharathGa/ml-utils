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
	1.eda - does the premilinary exploratory data analysis.
	2.catfreq - calculates the value counts of categorical variables.

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
	# if type(df['column']=='object'):
	# 	if fillna=='True':
	# 		df.column.map(dictionary).fillna(df.column.mean())
	# 	else:

#Calculating the frequency counts of categorical columns of the data
def catfreq(df,top= 5):
    
    '''This function calculates the top n value counts for categorical variables. If the total categorical
       columns are greater than 8, It becomes cumbersome to view the reports. I am thinking on an idea solve this 
    '''

    cat = df.select_dtypes(include = ['object']).columns
    if len(cat)> 8:
        print ('There are more than 8 columns')
    else:
        for x in cat:
             print('The Frequency counts for {} column:'.format(x))
             print( df[x].value_counts()[:top], '\n')

		



	





    

