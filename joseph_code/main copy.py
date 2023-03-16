import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import geopandas as gpd

def plot_comparison_stem():
    """
    the stemplot for comparison between congresional and presidential election
    """
    df_midterm = pd.read_excel('a7.xlsx')
    df_midterm.columns = df_midterm.iloc[3,:]
    # print(df_midterm.iloc[[7,8,9],:])
    df_midterm = df_midterm.iloc[[7,8,9],:]
    df_midterm = df_midterm.set_index(df_midterm.Characteristic)
    df_midterm.index.name = None
    df_midterm = df_midterm.drop(['Characteristic'], axis=1)
    df_midterm.columns = pd.to_numeric(df_midterm.columns, downcast='integer')
    df_midterm.columns.name = None


    df_pesdt = pd.read_excel('a9 (1).xlsx')
    df_pesdt.columns = df_pesdt.iloc[2,:]
    # # print(df_midterm.iloc[[7,8,9],:])
    df_pesdt = df_pesdt.iloc[[6,7,8],:]
    df_pesdt = df_pesdt.set_index(df_pesdt.Characteristic)
    df_pesdt.index.name = None
    df_pesdt = df_pesdt.drop(['Characteristic'], axis=1)
    df_pesdt.columns = pd.to_numeric(df_pesdt.columns, downcast='integer')
    df_pesdt.columns.name = None

    fig, ax = plt.subplots()
    markerline, stemlines, baseline = ax.stem(df_pesdt.columns,df_pesdt.loc['Percent voted'],linefmt='red', markerfmt='D')
    markerline.set_markerfacecolor(None)
    # plt.setp(markerline, markersize=5)      
    # plt.setp(stemlines, 'linewidth', 5)  
    line1 = ax.stem(df_midterm.columns,df_midterm.loc['Percent voted'])
    # ax.stem(df_pesdt.loc['Percent voted'], '-o', ms=20, alpha=0.7, mfc='orange')
    # ax.plot( df_midterm.loc['Percent voted'], '-o', ms=20, alpha=0.7, mfc='blue')
    # ax.legend(bbox_to_anchor=(0.5,0), loc="lower right",  bbox_transform=fig.transFigure)
    plt.ylim([0, 90])
    ax.legend(['presidential', 'congressional'],loc=1,bbox_transform=fig.transFigure)
    plt.xlabel('year')
    plt.ylabel('Voting rate')
    plt.title('Comparison of voting rate between presidential and congressional election')
    plt.show()

def surver_22_plot():
    """
    question 22, for those who have not registered, why? 
    """

    survey_data=pd.read_csv('survey_nonvote.txt').fillna(method='ffill')
    # A dictionary created which contains the potantional answers  
    answers_file=open('answers_sur.txt','r')
    answers_lines=answers_file.readlines()
    dictionary_ans=dict()

    list_qNum=['0']
    for line in answers_lines:
        if line[0]=='Q':
            list_qNum.append(line[1:].replace('\n',''))

    key_tra=''
    count=0
    val_lines=''
    for line in answers_lines:
        if line[0]=='Q':
            dictionary_ans['Q'+list_qNum[count]]=val_lines
            count=count+1
            key_tra=line
            val_lines=''
        else:
            val_lines=val_lines+line
    dictionary_ans['Q'+list_qNum[count]]=val_lines
    df_22 = survey_data.iloc[:,[80]]
    # grp = df_22.groupby('Q22')
    # grp.sum()
    df_22 = df_22.Q22.value_counts()
    df_22 = df_22.drop(df_22.index[-1])
    x = df_22.index.astype('int')
    print(x)
    x = ['don\'t want to register', 'don\'t trust the political system', 'don\'t think my vote matters', 'Other','don\'t have time', 'not eligible', 'don\'t know how to register']
    y = df_22.values
    # d = dict(zip(x,y))
    plt.bar(x,y)
    plt.xticks(rotation=30, ha='right')
    plt.title('Reasons for not registering')
    plt.show()

def survey_24():
    """
    whether registered, why method would you perfer
    """
    survey_data=pd.read_csv('survey_nonvote.txt').fillna(method='ffill')
    # A dictionary created which contains the potantional answers  
    answers_file=open('answers_sur.txt','r')
    answers_lines=answers_file.readlines()
    dictionary_ans=dict()

    list_qNum=['0']
    for line in answers_lines:
        if line[0]=='Q':
            list_qNum.append(line[1:].replace('\n',''))

    key_tra=''
    count=0
    val_lines=''
    for line in answers_lines:
        if line[0]=='Q':
            dictionary_ans['Q'+list_qNum[count]]=val_lines
            count=count+1
            key_tra=line
            val_lines=''
        else:
            val_lines=val_lines+line
    dictionary_ans['Q'+list_qNum[count]]=val_lines

    df_24 = survey_data.iloc[:,[79,82]]
    grp=df_24.groupby('Q21')

    tp = ('Absentee Ballot' , 'In-person before eletion day', 'In-person on eletion day')
    print(grp.get_group(2))
    total_1 = len(grp.get_group(1).index)
    t1 = grp.get_group(1).groupby("Q24").sum()
    t1 = tuple(t1.iloc[1:4,:].values.flatten())
    t1 = tuple(round(i/total_1,3) for i in t1)

    total_2 = len(grp.get_group(2).index)
    t2 = grp.get_group(2).groupby("Q24").sum()
    t2 = tuple(t2.iloc[1:4,:].values.flatten())
    t2 = tuple(round(i/712,3) for i in t2)


    d = {
        'Those who decided to vote in November 2020 election':t1
    , 'Those who decided NOT to vote in November 2020 election':t2
    }

    x = np.arange(len(tp))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')
    for attribute, measurement in d.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_ylabel('number of people')
    ax.set_title('Comparison of pereference over method of voting')
    ax.set_xticks(x + width, tp)
    ax.legend(loc='upper left')
    ax.set_ylim(0, 1)
    plt.xticks(rotation=30, ha='right')

    plt.show()


def survey_26():
    survey_data=pd.read_csv('survey_nonvote.txt').fillna(method='ffill')
    # A dictionary created which contains the potantional answers  
    answers_file=open('answers_sur.txt','r')
    answers_lines=answers_file.readlines()
    dictionary_ans=dict()

    list_qNum=['0']
    for line in answers_lines:
        if line[0]=='Q':
            list_qNum.append(line[1:].replace('\n',''))

    key_tra=''
    count=0
    val_lines=''
    for line in answers_lines:
        if line[0]=='Q':
            dictionary_ans['Q'+list_qNum[count]]=val_lines
            count=count+1
            key_tra=line
            val_lines=''
        else:
            val_lines=val_lines+line
    dictionary_ans['Q'+list_qNum[count]]=val_lines

    df_26_Q1 = survey_data.iloc[:,[84,41]]
    df_26_Q2 = survey_data.iloc[:,[84,42]]
    df_26_Q3 = survey_data.iloc[:,[84,43]]
    # df_26.Q26.unique()

    grp_Q1 = df_26_Q1.groupby('Q26')
    grp_Q2 = df_26_Q2.groupby('Q26')
    grp_Q3 = df_26_Q3.groupby('Q26')

    tp = ('Almost always ' , 'Sometimes', 'Rarely ','Never ')

    # print(grp_Q1.get_group(1)) # total people who said always voted
    total_1 = len(grp_Q1.get_group(1).index)
    t1 = grp_Q1.get_group(1).groupby("Q10_1").sum()
    t1_Q2 = grp_Q2.get_group(1).groupby("Q10_2").sum()
    t1_Q3 = grp_Q3.get_group(1).groupby("Q10_3").sum()
    t1_total = [t1.iloc[1].values.flatten()[0], t1_Q2.iloc[1].values.flatten()[0],t1_Q3.iloc[1].values.flatten()[0]]
    t1_total = [round(i/total_1,3) for i in t1_total]
    t1_total 

    total_2 = len(grp_Q1.get_group(2).index)
    t2 = grp_Q1.get_group(2).groupby("Q10_1").sum()
    t2_Q2 = grp_Q2.get_group(2).groupby("Q10_2").sum()
    t2_Q3 = grp_Q3.get_group(2).groupby("Q10_3").sum()
    # print(t2)
    t2_total = [t2.iloc[1].values.flatten()[0], t2_Q2.iloc[1].values.flatten()[0],t2_Q3.iloc[1].values.flatten()[0]]
    t2_total = [round(i/total_2,3) for i in t2_total]
    t2_total 

    # print(grp_Q1.get_group(3))
    t3 = grp_Q1.get_group(3).groupby("Q10_1").sum()
    t3_Q2 = grp_Q2.get_group(3).groupby("Q10_2").sum()
    t3_Q3 = grp_Q3.get_group(3).groupby("Q10_3").sum()
    print(t3)
    t3_total = [t3.iloc[0].values.flatten()[0], t3_Q2.iloc[0].values.flatten()[0],t3_Q3.iloc[0].values.flatten()[0]]
    t3_total = [round(i/1023,3) for i in t3_total]
    t3_total 

    t4 = grp_Q1.get_group(4).groupby("Q10_1").sum()
    # print(t4)
    t4_Q2 = grp_Q2.get_group(4).groupby("Q10_2").sum()
    # print(t4)
    t4_Q3 = grp_Q3.get_group(4).groupby("Q10_3").sum()
    t4_total = [t4.iloc[1].values.flatten()[0], t4_Q2.iloc[1].values.flatten()[0],t4_Q3.iloc[1].values.flatten()[0]]
    t4_total = [round(i/1757,3) for i in t4_total]
    t4_total 

    tt1 = tuple(i[0] for i in [t1_total,t2_total,t3_total,t4_total])
    tt2 = tuple(i[1] for i in [t1_total,t2_total,t3_total,t4_total])
    tt3 = tuple(i[2] for i in [t1_total,t2_total,t3_total,t4_total])

    # t_i total:
    # for those who answer i in Q26 [perct answer 1 in question 10_1, perct answer 1 in question 10_2]

    d = {
        'percentage of reciving long term disability':tt1
    , 'percentage of having a chronic disease':tt2,
    'percentage of being evicted':tt3
    }

    x = np.arange(len(tp))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')
    for attribute, measurement in d.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_xlabel('claimed frequency of voting')
    ax.set_ylabel('percentage of respectively population')
    ax.set_title('Comparison over people with different voting frequencies')
    ax.set_xticks(x + width, tp)
    ax.legend(loc='upper left')
    ax.set_ylim(0, 1)
    plt.xticks(rotation=30, ha='right')

    plt.show()

def f(x):
    if x.last_valid_index() is None:
        return np.nan
    else:
        return x[x.last_valid_index()]


def plot_map():
    df = pd.read_csv('voter-turnout.csv')
    # df.index = df.Entity
    # df = df.drop(columns=['Entity','Code'])
    print(df.columns)
    table = pd.pivot_table(df,index=['Entity','Code'], columns=['Year'])
    # print(table)

    table['temp'] = table.apply(f,axis=1)
    df_new = table['temp']
    # print(df_new)

    countries = gpd.read_file(
                gpd.datasets.get_path("naturalearth_lowres"))
    countries['Code'] = countries['iso_a3']

    df_to_plot = pd.merge(countries, df_new, on = 'Code')
    ax = df_to_plot.plot("temp", cmap = "Blues",figsize=(15,15))
    ax.set_axis_off()
    plt.show()

    
if __name__ =="__main__":
    # plot_comparison_stem()
    surver_22_plot()