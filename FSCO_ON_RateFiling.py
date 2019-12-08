import bs4
import requests
import pandas as pd
import os

os.chdir('C:\\!DONOTDELETE\\devbin\\')

# list of QQ-YYYY to build URLs
urlf = 'http://www.fsco.gov.on.ca/en/auto/rates/Pages/q'
urlm = '-'
urle = '.aspx'

df = pd.DataFrame()


urlList = []

for y in range(2008,2012):

	for q in range(1,5):
		urlList.append(urlf+str(q)+urlm+str(y)+urle)
# credit to:
# https://github.com/grantaguinaldo/taco-bell-scrape/blob/master/Taco%20Bell%20Scrape.ipynb
# for guidance in translating BeautifulSoup content to Pandas

for qtr in urlList:
    #print(qtr)    
    page = bs4.BeautifulSoup(requests.get(qtr).text, 'html.parser')
    chart = page.select('.ms-rteTable-6 tr')
    for row in chart:
        try:
                df = df.append(pd.DataFrame({'carrier': row.getText().split('\n')[0],
                                             'share': row.getText().split('\n')[1],
                                             'nb_eff': row.getText().split('\n')[2],
                                             'rn_eff': row.getText().split('\n')[3],
                                             'avgRateChg_pct': row.getText().split('\n')[4],
                                             'Yr': qtr[49:53],
                                             'Qtr': qtr[46:48]},
                                            index = [0]), ignore_index=True)
        except IndexError:
                break


urlList = []
for y in range(2012,2014):

	for q in range(1,5):
		urlList.append(urlf+str(q)+urlm+str(y)+urle)

for qtr in urlList:
    #print(qtr)    
    page = bs4.BeautifulSoup(requests.get(qtr).text, 'html.parser')
    chart = page.select('.ms-rteTable-6 tr')
    for k in range(1,int(len(chart))):
        try:
                df = df.append(pd.DataFrame({'carrier': chart[k].getText().split('\n')[1],
                                             'share': chart[k].getText().split('\n')[2],
                                             'nb_eff': chart[k].getText().split('\n')[3],
                                             'rn_eff': chart[k].getText().split('\n')[4],
                                             'avgRateChg_pct': chart[k].getText().split('\n')[5],
                                             'Yr': qtr[49:53],
                                             'Qtr': qtr[46:48]},
                                            index = [0]), ignore_index=True)
        except IndexError:
                break


urlList = []
for y in range(2014,2019):

        for q in range(1,5):
                urlList.append(urlf+str(q)+urlm+str(y)+urle)

for qtr in urlList:
        #print(qtr)    
        page = bs4.BeautifulSoup(requests.get(qtr).text, 'html.parser')
        
        oddRows = page.select('.ms-rteTable-6 .ms-rteTableOddRow-6')
        evnRows = page.select('.ms-rteTable-6 .ms-rteTableEvenRow-6')
        
        for i in range(int(len(oddRows))):
                for j in range(4):
                        try:
                                df = df.append(pd.DataFrame({'carrier': bs4.BeautifulSoup(str(oddRows[i]),'html.parser').select('.ms-rteTableEvenCol-6')[j].getText(),
                                                             'share': bs4.BeautifulSoup(str(oddRows[i]),'html.parser').select('.ms-rteTableOddCol-6')[j].getText(),
                                                             'nb_eff': bs4.BeautifulSoup(str(oddRows[i]),'html.parser').select('.ms-rteTableEvenCol-6')[j+1].getText(),
                                                             'rn_eff': bs4.BeautifulSoup(str(oddRows[i]),'html.parser').select('.ms-rteTableOddCol-6')[j+1].getText(),
                                                             'avgRateChg_pct': bs4.BeautifulSoup(str(oddRows[i]),'html.parser').select('.ms-rteTableEvenCol-6')[j+2].getText(),
                                                             'Yr': qtr[49:53],
                                                             'Qtr': qtr[46:48]},
                                                            index = [0]), ignore_index=True)
                        except IndexError:
                                continue


        for i in range(int(len(evnRows))):
                for j in range(4):
                        try:
                                df = df.append(pd.DataFrame({'carrier': bs4.BeautifulSoup(str(evnRows[i]),'html.parser').select('.ms-rteTableEvenCol-6')[j].getText(),
                                                             'share': bs4.BeautifulSoup(str(evnRows[i]),'html.parser').select('.ms-rteTableOddCol-6')[j].getText(),
                                                             'nb_eff': bs4.BeautifulSoup(str(evnRows[i]),'html.parser').select('.ms-rteTableEvenCol-6')[j+1].getText(),
                                                             'rn_eff': bs4.BeautifulSoup(str(evnRows[i]),'html.parser').select('.ms-rteTableOddCol-6')[j+1].getText(),
                                                             'avgRateChg_pct': bs4.BeautifulSoup(str(evnRows[i]),'html.parser').select('.ms-rteTableEvenCol-6')[j+2].getText(),
                                                             'Yr': qtr[49:53],
                                                             'Qtr': qtr[46:48]},
                                                            index = [0]), ignore_index=True)
                        except IndexError:
                                break




print(df.head())

df2=df[(df.carrier!='Insurer') & (df.carrier!='Total Market Impact')& (df.carrier!='')]

df2['carrier'] = df2['carrier'].str.strip()
df2['share'] = df2['share'].str.replace('%','')
df2['share'] = df2['share'].str.strip()
df2['nb_eff'] = df2['nb_eff'].str.strip()
df2['rn_eff'] = df2['rn_eff'].str.strip()
df2['avgRateChg_pct'] = df2['avgRateChg_pct'].str.replace('%','')
df2['avgRateChg_pct'] = df2['avgRateChg_pct'].str.strip()

df2.to_csv('OntarioRateFilings.csv',encoding='utf-8-sig')
df.to_csv('OntarioRateFilings_raw.csv',encoding='utf-8-sig')



#rowSoup = bs4.BeautifulSoup(str(oddRows[0]),'html.parser')
#rowSoup.select('.ms-rteTableEvenCol-6')[0].getText()

# my test
# page = bs4.BeautifulSoup(requests.get(url).text, 'html.parser')
# test = page.select('.ms-rteTable-6 tr')
# print(len(test))
# print(test[1].getText())

#re.match('^\D+',test)
