import PyPDF2 as pdf
import pandas as pd
import os
import re

os.chdir('C:\\!DONOTDELETE\\devbin\\')
file = 'machineable_presort_fsalist_february2014.pdf'
#source: https://www.canadapost.ca/cpo/mc/assets/pdf/business/nps/machineable_presort_fsalist_february2014.pdf

namSeries = pd.Series()

pdf_file = open(file, 'rb')
read_pdf = pdf.PdfFileReader(pdf_file)

allpages = ''

for i in range(1,int(read_pdf.getNumPages())):
    allpages = allpages+read_pdf.getPage(i).extractText()

fsaSeries = pd.Series(re.findall('\s+([A-Za-z]{1}\d{1}[A-Za-z]{1})',allpages))

for i in range(int(fsaSeries.size)):
    try:
        regex = str(fsaSeries[i]+'(.*)'+fsaSeries[i+1])
        namSeries = namSeries.append(pd.Series(re.findall(regex,allpages)[0]))
    except KeyError:
        regex = str(fsaSeries[i]+'(.{40})')
        namSeries = namSeries.append(pd.Series(re.findall(regex,allpages)[0]))

namSeries = namSeries.str.replace('\#', ' ', regex=True)
namSeries = namSeries.str.strip()

fsadf = pd.DataFrame({'index':fsaSeries.index,'fsa':fsaSeries.values, 'name':namSeries.values})
fsadf.to_csv('fsaList.csv',encoding='utf-8-sig')
