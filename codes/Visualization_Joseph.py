import numpy as np 
import matplotlib.pyplot as plt 
#import ploty.express as px
import pandas as pd 
import os
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import Normalizer
from scipy.stats import pearsonr
'''
Code for 143 project
Author : Joseph Kuo
email: jokuo@ucsd.edu
Yiyang Zhang and I contributed in world_mp_plot.py 
'''
plt.rcParams["figure.figsize"] = (25, 10)

def extractData(Table, FirstLevelRowInfo, SecondLevelRowInfo, SecondLevelColInfo):
    '''
    This function extract data for table 5 by 
    selecting first level index in the table from param "FirstLevelRowInfo"
    selecting second level index in the table from param "SecondLevelRowInfo"
    selecting second level column in the table from param "SecondLevelColInfo"
    '''
    #/ECE143 Final Project/Voting Election 2020 Table
    # *** In thousands ***
    df_5_1 = pd.read_excel(Table,  header=[0,1,2],index_col=[0,1])
    #print(df_5_1.columns)
    #print(df)
    census_data_table_5_1 = df_5_1.iloc[:21]
    #print("this is updated df")
    #print(census_data_table_5_1)
    census_data_table_5_1_sorted = census_data_table_5_1.sort_index()
    Election_2020_sorted = census_data_table_5_1_sorted.loc[(FirstLevelRowInfo,SecondLevelRowInfo),('United States citizen',SecondLevelColInfo)]
    #print(reportednotRegistered2020_sorted)
    return Election_2020_sorted

def extractSameRowOrCol(TableNumbers, TableName, FirstLevelRowInfo, SecondLevelRowInfo, SecondLevelColInfo):
    '''
    This function extract data for different table in table 5 ex: table05_1, table05_2, etc.
    selecting how many tables you want to extract, for ex: there are 6 different tables for table 5, you can put param
    "TableNumbers" = 6
    selecting table name, for ex: table05_1 => TableName = "table05"
    selecting first level index in the table from param "FirstLevelRowInfo"
    selecting second level index in the table from param "SecondLevelRowInfo"
    selecting second level column in the table from param "SecondLevelColInfo"
    This function outputs a dictionary. Each value in the key is a pandas series object
    '''
    thedict = {}
    for table in range(1,TableNumbers+1,1):
        thedict[table] =  extractData('%s_%d.xlsx' %(TableName, table), FirstLevelRowInfo, SecondLevelRowInfo, SecondLevelColInfo)
    return thedict



if __name__ == "__main__":
    """
    Remember to change or delete the directory, it could be different on different computers
    """
    os.chdir('../US_census')
    dict_education_level_Voted = extractSameRowOrCol(6,'table05','BOTH SEXES',slice(None),'Reported voted')

    dict_less_than_9th_grade_Voted = extractSameRowOrCol(6,'table05','BOTH SEXES','Less than 9th grade','Reported voted')
    dict_9th_to_12th_grade_no_diploma_Voted = extractSameRowOrCol(6,'table05','BOTH SEXES','9th to 12th grade, no diploma','Reported voted')
    dict_high_school_graduate_Voted = extractSameRowOrCol(6,'table05','BOTH SEXES','High school graduate','Reported voted')
    dict_some_college_or_associate_deg_Voted = extractSameRowOrCol(6,'table05','BOTH SEXES','Some college or associate\'s degree','Reported voted')
    dict_bachelor_deg_Voted = extractSameRowOrCol(6,'table05','BOTH SEXES','Bachelor\'s degree','Reported voted')
    dict_advanced_deg_Voted = extractSameRowOrCol(6,'table05','BOTH SEXES','Advanced degree','Reported voted')
    data = np.array(list(dict_education_level_Voted.values())).reshape(-1, 2)
    df_education_level_Voted = pd.DataFrame(data, columns=['Education level', 'Reported voted'])
    for num_key in dict_education_level_Voted:
        dict_education_level_Voted[num_key] = dict_education_level_Voted.get(num_key).reset_index(level=0, drop = True).iloc[0:6,:]

    # print(dict_education_level_Voted.get(1))
    df_all_ages_eduction_level_Voted = pd.DataFrame.from_dict(dict_education_level_Voted.get(1))
    df_all_ages_eduction_level_Voted.index.name = 'Education level'

    #df_all_ages_eduction_level_Voted['Percent'] = df_all_ages_eduction_level_Voted['Percent'].apply(lambda x : x/100)
    df_all_ages_eduction_level_Voted['I'] = [2,6,5,3,1,4]
    df_sabi = df_all_ages_eduction_level_Voted.sort_values('I')
    
    #temp = df_sabi.to_numpy()[:,[2]]
    #ts = Normalizer().fit(temp)
    #ncol = ts.transform(temp)
    # print(reg.score(df_sabi.to_numpy()[:,[2]], df_sabi.to_numpy()[:,1]))


    df_less_than_9th_grade_Voted = pd.DataFrame.from_dict(dict_less_than_9th_grade_Voted).loc[:,2:6].drop('Percent').transpose().rename(columns={'Number': 'Voted (< 9th)'}, index={2:'age 18 ~ 24',3:'age 25 ~ 44',4:'age 45 ~ 64',5:'age 65 ~ 74',6:'age 75 ~ over'})
    df_9th_to_12th_grade_no_diploma_Voted = pd.DataFrame.from_dict(dict_9th_to_12th_grade_no_diploma_Voted).loc[:,2:6].drop('Percent').transpose().rename(columns={'Number': 'Voted (9th-12th)'}, index={2:'age 18 ~ 24',3:'age 25 ~ 44',4:'age 45 ~ 64',5:'age 65 ~ 74',6:'age 75 ~ over'})
    df_high_school_graduate_Voted = pd.DataFrame.from_dict(dict_high_school_graduate_Voted).loc[:,2:6].drop('Percent').transpose().rename(columns={'Number': 'Voted (High school Grad)'}, index={2:'age 18 ~ 24',3:'age 25 ~ 44',4:'age 45 ~ 64',5:'age 65 ~ 74',6:'age 75 ~ over'})
    df_some_college_or_associate_deg_Voted = pd.DataFrame.from_dict(dict_some_college_or_associate_deg_Voted).loc[:,2:6].drop('Percent').transpose().rename(columns={'Number': 'Voted (College/Associate\'s deg)'}, index={2:'age 18 ~ 24',3:'age 25 ~ 44',4:'age 45 ~ 64',5:'age 65 ~ 74',6:'age 75 ~ over'})
    df_bachelor_deg_Voted = pd.DataFrame.from_dict(dict_bachelor_deg_Voted).loc[:,2:6].drop('Percent').transpose().rename(columns={'Number': 'Voted (Bachelor\'s deg)'}, index={2:'age 18 ~ 24',3:'age 25 ~ 44',4:'age 45 ~ 64',5:'age 65 ~ 74',6:'age 75 ~ over'})
    df_advanced_deg_Voted = pd.DataFrame.from_dict(dict_advanced_deg_Voted).loc[:,2:6].drop('Percent').transpose().rename(columns={'Number': 'Voted (Advanced deg)'}, index={2:'age 18 ~ 24',3:'age 25 ~ 44',4:'age 45 ~ 64',5:'age 65 ~ 74',6:'age 75 ~ over'})
    #print(df_less_than_9th_grade_Voted)

    # df_all_ages_eduction_level_Voted = df_all_ages_eduction_level_Voted

    df_total = pd.concat([df_less_than_9th_grade_Voted, df_9th_to_12th_grade_no_diploma_Voted, df_high_school_graduate_Voted,df_some_college_or_associate_deg_Voted, df_bachelor_deg_Voted, df_advanced_deg_Voted], axis=1).transpose()
    df_total.index.name = "Education Level"
    # print(df_total)
    
    
    #plot0 = df_all_ages_eduction_level_Voted.plot.pie(title='US Citizen Voted: Education Level (All ages) ', y = 'Number', figsize = (5,5), autopct = '%1.1f%%', fontsize = 10)
    #plot1 = df_less_than_9th_grade_Voted.plot.pie(title='US Citizen Voted Whose Education Level is Less than 9th Grade', y = 'People Voted', figsize = (5,5), autopct = '%1.1f%%', fontsize = 10)
    #plot2 = df_9th_to_12th_grade_no_diploma_Voted.plot.pie(title='US Citizen Voted Whose Education Level is 9th Grade to 12th Grade', y = 'People Voted', figsize = (5,5), autopct = '%1.1f%%', fontsize = 10)
    #plot3 = df_high_school_graduate_Voted.plot.pie(title='US Citizen Voted Whose Education Level is High School Graduate', y = 'People Voted', figsize = (5,5), autopct = '%1.1f%%', fontsize = 10)
    #plot4 = df_some_college_or_associate_deg_Voted.plot.pie(title='US Citizen Voted Whose Education Level is Some College or Associate\'s Degree', y = 'People Voted', figsize = (5,5), autopct = '%1.1f%%', fontsize = 10)
    #plot5 = df_bachelor_deg_Voted.plot.pie(title='US Citizen Voted Whose Education Level is Bachelor\'s Degree', y = 'People Voted', figsize = (5,5), autopct = '%1.1f%%',fontsize = 10,)
    #plot5 = df_advanced_deg_Voted.plot.pie(title='US Citizen Voted Whose Education Level is Advanced Degree', y = 'People Voted', figsize = (5,5), autopct = '%1.1f%%', fontsize =10)


    #out of 154628 who voted
    #ppl at age 18 ~ 24 13752 voted => (all rows, 1st col) 43 + 713 + 3646 + 6844 + 2331 + 175 = 13752
    #ppl at age 25 ~ 44 47512 voted => (all rows, 2nd col) 152 + 983 + 9038 + 12875 + 16113 + 8351 =  47512
    #ppl at age 45 ~ 64 53646 voted => (all rows, 3rd col) 567 + 1681 + 13205 + 15414 + 13787 + 8993 = 53647
    #ppl at age 65 ~ 74 24050 voted => (all rows, 4th col) 462 + 909 + 6323 + 6976 + 5292 + 4088 = 24050
    #ppl at age 75 ~ over 15668 voted => (all rows, 5th col) 576 + 998 + 5244 + 3847 + 2790 + 2213 = 15668
    # 13752 + 47512 + 53646 + 24050 + 15668 =  154628


    reg = LinearRegression().fit(df_sabi.to_numpy()[:,[2]], df_sabi.to_numpy()[:,1])
    
    #reg_y_pred = reg.predict(diabetes_X_test)
    #clf = LogisticRegression().fit(df_sabi.to_numpy()[:,[2]], df_sabi.to_numpy()[:,1])
    #print(df_sabi.to_numpy()[:,[2]])
    #print(df_sabi.to_numpy()[:,1])
    coeff = reg.coef_
    intercept = reg.intercept_
    
    df_14 = pd.read_excel('table14.xlsx',  header=[0,1],index_col=[0,1])
    # print(df_14)
    table14 = df_14.iloc[:40].drop(index=['TOTAL'], columns=['Total voted'])
    table14.columns = table14.columns.droplevel()
    table_14_sorted = table14.sort_index().transpose()
    #print(table_14_sorted)
    df_14_1 = table_14_sorted.groupby(level=0, axis=1).mean().drop(index='Don\'t know or Refused').rename(index={'In-person on Election Day':'I.P. E.', 'In-person Before Election Day': 'I.P. Before E.'}).transpose()
    #print(df_14_1)
    #plot2 = df_14_1.plot.bar(figsize = (8,8))
    #Election_2020_sorted = census_data_table_5_1_sorted.loc[(FirstLevelRowInfo,SecondLevelRowInfo),('United States citizen',SecondLevelColInfo)]
    #print(reportednotRegistered2020_sorted)
    #plt.scatter(df_sabi.to_numpy()[:,[2]], df_sabi.to_numpy()[:,1])
    # plot3 = plt.scatter(x = df_sabi.to_numpy()[:,[2]], y = df_sabi.to_numpy()[:,1])
    fig , ax = plt.subplots()
    plt.scatter(x = df_sabi.to_numpy()[:,[2]], y = df_sabi.to_numpy()[:,1])
    x_vals = np.array(ax.get_xlim())
    y_vals = intercept + coeff * x_vals
    plt.plot(x_vals, y_vals)
    cclemon = pearsonr(np.squeeze(df_sabi.to_numpy()[:,[2]]),np.squeeze(df_sabi.to_numpy()[:,1]))
    print(cclemon[0])
    # ax[1] = df_14_1.plot.bar(rot = 45)
    #ax = plt.axes()
    ax.set_xticks([1,2,3,4,5,6])
    # locs, labels = plt.xticks()
    # plt.xticks([0,1,], ['January', 'February', 'March'],rotation=20)
    ax.set_xticklabels(['less_than_9th_grade','9th_to_12th_grade','high_school_graduate','some_college_or_associate_deg','bachelor_deg','advanced_deg'],weight='bold')
    
    # plt.xlabel("Education Level")
    # plt.ylabel("Percent")
    
    plt.xticks(rotation = 15,fontsize=15)
    plt.yticks(weight='bold',fontsize=15)
    plt.xlabel("Education Level",weight='bold',fontsize=15)
    plt.ylabel("Percent",weight='bold',fontsize=15)
    plt.show()

    plot2 = df_14_1.plot.bar(rot = 30, title = 'Voting Methods Preferred in Different Characteristic', ylabel = 'Percent',fontsize=20)
    plt.show()
    
    plot = df_total.plot.bar(rot=0, figsize = (5,5))
    plt.show()
    print(df_all_ages_eduction_level_Voted)
    cmap = plt.get_cmap("PiYG")(np.linspace(0.3,0.7,len(df_all_ages_eduction_level_Voted.Number.values)))
    # outer_colors = cmap(np.arange(3)*4)
    # inner_colors = cmap([1, 2, 5, 6, 9, 10])

    plot0 = df_all_ages_eduction_level_Voted.plot.pie(title='US Citizen Voted: Education Level (All ages) ', y = 'Number', figsize = (8,8), autopct = '%1.1f%%', fontsize=15)
    plt.show()

    plt.pie(df_all_ages_eduction_level_Voted.Number.values, labels = ['9th to 12th grade(no diploma)','Advanced deg','Bachelor\'s deg','High school graduate', 'Less than 9th grade','Some college or associate\'s deg'],autopct = '%1.1f%%',textprops={'fontsize': 24}, colors = cmap)
    plt.text(6, 10, 'Bold Font',  fontsize=16)  

    plt.show()