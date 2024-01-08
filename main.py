import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def read_data():
    dataframe = pd.read_excel('budget.xlsx',sheet_name='current_data')
    #print (dataframe[['MINISTRY','BUDGETARY_UNIT','ITEM_DESCRIPTION','AMOUNT','OBLIGED?']])

    #print(dataframe['MINISTRY'].unique())
    health_ministries =  ['กระทรวงศึกษาธิการ','กระทรวงสาธารณสุข','กระทรวงการอุดมศึกษา วิทยาศาสตร์ วิจัยและนวัตกรรม']
    health_ministries2 = ['กระทรวงศึกษาธิการ', 'กระทรวงการอุดมศึกษา วิทยาศาสตร์ วิจัยและนวัตกรรม']

    df = dataframe[['MINISTRY','BUDGETARY_UNIT','ITEM_DESCRIPTION','AMOUNT','OBLIGED?']]

    df2 = df.loc[df['MINISTRY'].isin(health_ministries2)]

    df2.drop(df[df['BUDGETARY_UNIT'] == 'สำนักงานคณะกรรมการการศึกษาขั้นพื้นฐาน'].index, inplace=True)

    df2_1 = df2[df2['ITEM_DESCRIPTION'].str.contains("โรงพยาบาล|แพทย์|แพทยศาสตร์|ทันตะ|ทันตกรรม")]
    df_result1 = df2_1.groupby(['MINISTRY','BUDGETARY_UNIT'])['AMOUNT'].sum()

    df_result2 = df2.groupby(['MINISTRY','BUDGETARY_UNIT'])['AMOUNT'].sum()

    result3 = pd.merge(df_result1,df_result2,how='inner', on='BUDGETARY_UNIT')

    x = result3['AMOUNT_x'].index.tolist()
    y1 = result3['AMOUNT_x'].values.tolist()
    y2 = result3['AMOUNT_y'].values.tolist()

    print(x)
    print(y1)
    print(y2)

    #Deduct duplicate budget
    y3 = []
    i = 0
    for n in y2:
        y3.append(n - y1[i])
        i += 1

    print (y3)

    # plot bars in stack manner
    plt.bar(x, y1, color='r')
    plt.bar(x, y3, bottom=y1, color='b')
    plt.show()


if __name__ == '__main__':
    read_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
