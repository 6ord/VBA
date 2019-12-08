#import PyPDF2 as pdf
import pandas as pd
#import numpy as np
import os, re
from datetime import datetime
import itertools as it
import operator as op
from functools import reduce
from fuzzywuzzy import fuzz
##https://www.datacamp.com/community/tutorials/fuzzy-string-python

print(datetime.now())

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def comPair(a,b):
    #return min(sum([item in a for item in b])/len(b),sum([item in b for item in a])/len(a))
    #return fz.token_set_ratio(a,b)
    return fuzz.token_sort_ratio(a,b)

def compare(tpl):
    pctMatch = []
    for i in range(len(list(it.combinations(tpl,2)))):
        pctMatch.append(comPair(list(it.combinations(tpl,2))[i][0],list(it.combinations(tpl,2))[i][1]))
    try:
        return min(pctMatch)
    except ValueError:
        return 100
    
#  https://stackoverflow.com/questions/5278122/checking-if-all-elements-in-a-list-are-unique
def unique_values(g):
    s = set()
    for x in g:
        if x in s: return False
        s.add(x)
    return True


pd.set_option('display.max_columns',500)
pd.set_option('display.max_rows',50)
pd.set_option('display.width',1000)

#os.chdir('Y:\\QlikBin\\')
os.chdir('C:\\!DONOTDELETE\\devbin\\namedInsured\\')


fileHOME = 'actvHab_fromR_20191028.csv'
fileAUTO = 'actvAut_fromR_20191028.csv'
fileSEGM = 'polCurr_20191028.csv'


rawHOME = pd.read_csv(fileHOME, encoding = 'ISO-8859-1')
rawAUTO = pd.read_csv(fileAUTO, encoding = 'ISO-8859-1')
rawSEGM = pd.read_csv(fileSEGM, encoding = 'ISO-8859-1')
#rawACTV = pd.read_csv(fileACTV, encoding = 'ISO-8859-1')
#align columns, rename to same and combine

print('...csv files import complete')

book = rawSEGM
book.columns = ['SEGMENT','CUST_ID','POL_TYPE','POL_IDX','EMAIL', 'HDG', 'LANG']
#book['NAME'] = book.apply(lambda x: str(x['NAME']).upper(),axis=1)
book['POL_TYPE'] = book.apply(lambda x: str(x['POL_TYPE']).replace('Auto','AUTO'),axis=1)
book['POL_TYPE'] = book.apply(lambda x: str(x['POL_TYPE']).replace('Aux Property','AUTO'),axis=1)
book['POL_TYPE'] = book.apply(lambda x: str(x['POL_TYPE']).replace('Residential','HOME'),axis=1)
book['POL_TYPE'] = book.apply(lambda x: str(x['POL_TYPE']).replace('Business','HOME'),axis=1)
book['POL_TYPE'] = book.apply(lambda x: str(x['POL_TYPE']).replace('Aux Liab','LIAB'),axis=1)
book['POL_TYPE'] = book.apply(lambda x: str(x['POL_TYPE']).replace('Package','HOME'),axis=1)
book['POL_TYPE'] = book.apply(lambda x: str(x['POL_TYPE']).replace('Life & Health','LIFE'),axis=1)
book['POL_TYPE'] = book.apply(lambda x: str(x['POL_TYPE']).replace('Aux Veh(land/water)','AUTO'),axis=1)
book['POL_TYPE'] = book.apply(lambda x: str(x['POL_TYPE']).replace('Aux Contents','HOME'),axis=1)


## TEMP
## rawAUTO['LIC_PROV'] = 'XX'

#cust = rawHOME[['POL_REC','POL_IDX','NAME']]
home = rawHOME[['POL_REC','POL_IDX','APP_NAME', 'APP_PROV', 'RISK_PROV']]    #concat APP_ATTN     APP_PROV or RISK_PROV
auto = rawAUTO[['POL_REC','POL_IDX','INSUREDAPP','INSUREDAP6', 'LIC_PROV']] #concat INSUREDAP2   INSUREDAP6 or LIC_PROV

# auto app province is 'INSUREDAP6'
# add RISK column = Auto or Prop
# multi policy, multi named insured

home.columns = ['POL_REC','POL_IDX','NAME','PROV_APP','PROV_RSK'] #incl ATT field
auto.columns = ['POL_REC','POL_IDX','NAME','PROV_APP','PROV_RSK'] #incl ATT field
home['POL_TYPE'] = 'HOME'
auto['POL_TYPE'] = 'AUTO'
allRisks = home.append(auto)


book['POL_IDX_TYPE'] = book.apply(lambda x: str(x['POL_IDX'])+str(x['POL_TYPE']), axis=1)
allRisks['POL_IDX_TYPE'] = allRisks.apply(lambda x: str(x['POL_IDX'])+str(x['POL_TYPE']), axis=1)

#Merge all risks with active policies listing
allRisks = pd.merge(allRisks, book[['POL_IDX_TYPE','SEGMENT','EMAIL','HDG','LANG']], left_on='POL_IDX_TYPE', right_on='POL_IDX_TYPE', how='left')
#Takes Active Only
risks = allRisks[allRisks.SEGMENT.notnull()]


#Concatenate Name, replace NAME with FULLNAME from here on  #####################################
#test['FULLNAME'] = test.apply(lambda x: str(x['NAME'])+str(x['ATT']), axis=1)

risks['CUST_ID'] = risks.apply(lambda x: str(x['POL_REC'])[:7],axis=1)

#all to upper and clean words
risks['NAME'] = risks.apply(lambda x: str(x['NAME']).upper(),axis=1)
risks['NAME'] = risks.apply(lambda x: str(x['NAME']).replace('.',''),axis=1)
risks['NAME'] = risks.apply(lambda x: str(x['NAME']).replace(',',''),axis=1)
#risks['NAME'] = risks.apply(lambda x: str(x['NAME']).replace('-',' '),axis=1)
risks['NAME'] = risks.apply(lambda x: str(x['NAME']).replace(' AND ',' & '),axis=1)
#risks['NAME'] = risks.apply(lambda x: str(x['NAME']).replace(' AND ',''),axis=1)
#risks['NAME'] = risks.apply(lambda x: str(x['NAME']).replace('***',''),axis=1)

#Tokenize named insureds
#risks['tk'] = risks.apply(lambda x: tuple(str(x['NAME']).split()),axis=1)
risks['tk'] = 0

#build TAM Customer ID
#temp.columns = ['POL_IDX','NUMRISKS']
#risks = pd.merge(risks, temp, left_on='POL_IDX', right_on='POL_IDX', how='left')

agg = risks.groupby(by=['CUST_ID','POL_TYPE'], as_index = False).agg({'POL_IDX': lambda x: x.nunique()})
agg.columns = ['CUST_ID','POL_TYPE','NUM_POLIDX']
risks = pd.merge(risks, agg, left_on=['CUST_ID','POL_TYPE'], right_on=['CUST_ID','POL_TYPE'], how='left')
#risks['MULTINAME'] = risks.apply(lambda x: str(x['NAME']).find(' & '), axis = 1)
risks['MULTINAME'] = risks['NAME'].apply(lambda x: 'True' if str(x).find(' & ')>-1 else 'False')


#risks['MULTIRSK'] = pd.Index(risks['POL_IDX']).duplicated(keep = False)

#risks['MULTIPOL'] = pd.Index(risks['POL_IDX']).duplicated(keep = False)

### TO DO ###
#Build POL_IDX
#Subset active Policies Only
#
#risks['REC'] = risks.apply(lambda x: str(x['POL_REC'])[-3:],axis=1)
#risks['SLOT'] = risks.apply(lambda x: (int(re.findall(r'\d+',x['REC'])[0])*1000)+1,axis=1)

## @@@@@@@@@@@@@@@@@@@@@@@@
#allAuto$POL_IDX<-ifelse(allAuto$SLOT>9999,paste(allAuto$custID, allAuto$SLOT, sep=''),paste(allAuto$custID, allAuto$SLOT, sep='-'))

#risks['POL_IDX'] = ['red' if x == 'Z' else 'green' for x in df['Set']]
#risks['POL_IDX'] = risks.Set.map( lambda x: 'red' if x == 'Z' else 'green')
#risks['POL_IDX'] = risks.apply(lambda x: str(x['POL_REC'])[:7]+'-'+str(x[SLOT],axis=1) if x['SLOT'] < 10000  else str(x['POL_REC'])[:7]+str(x[SLOT]),axis=1)
#risks['POL_IDX'] = str(risks['POL_REC'])[:7]+str(risks['SLOT'])
#risks[['POL_REC','TEMP']].head(25)
#dataframe["period"] = dataframe["Year"].map(str) + dataframe["quarter"]

#risks['POL_IDX'] = np.where(risks['SLOT'] > 9999, risks['POL_REC']+str(risks['SLOT']),risks['POL_REC']+"-"+str(risks['SLOT']))

#allAuto$REC <- NULL
#allAuto$SLOT <- NULL

#risksNameOnly = risks[['CUST_ID','POL_IDX','POL_REC','NAME','tk']]


#for each POL_REC, compare() each pair of tk, take minimum
uniqCust = pd.DataFrame({'CUST_ID': list(risks.CUST_ID.unique())})

uniqCust['NAME'] = ''

#TEST OPTION
#for i in range(50):
for i in range(len(uniqCust)):

    uniqCust['NAME'][i] = risks.loc[(risks.CUST_ID == uniqCust.iloc[i,0])]['NAME']
    
uniqCust['MATCH'] = uniqCust.apply(lambda x: compare(x['NAME']),axis=1)

uniqCust[['CUST_ID','MATCH']].to_csv('nameMatch.csv', sep=',', encoding='utf-8')
risks.to_csv('risks.csv', sep=',', encoding='utf-8')
agg.to_csv('agg.csv', sep=',', encoding='utf-8')


# Test #
print(risks.loc[(risks.CUST_ID== 'ACERRA1')])
print(risks.loc[(risks.CUST_ID== 'ABARVI1')])
print(agg.loc[(agg.CUST_ID=='DINALA1')])

#output['tk'] = output.apply(lambda x: compare(list(risksNameOnly.loc[(risksNameOnly.CUST_ID == x.iloc[12501,0])]['tk'])),axis=1)

### FOR TESTING ###

#list(it.combinations(a,2))
#len(risksNameOnly.loc[(risksNameOnly.CUST_ID == uniqCust.iloc[12501,0])])
#risksNameOnly.loc[(risksNameOnly.CUST_ID == uniqCust.iloc[12501,0])]
#compare(list(risksNameOnly.loc[(risksNameOnly.CUST_ID == uniqCust.iloc[12501,0])]['tk']))
a = ['a','b','c','d','e']
b = ['b','d','c','x']
c = ['d','c','x']
ab = [a,b]
abc = [a,b,c]

print(datetime.now())
