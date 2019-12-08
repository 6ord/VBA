import PyPDF2 as pdf
import pandas as pd
import os

os.chdir('C:\\!DONOTDELETE\\devbin\\')
file = 'MarshCanadaT&D_2017-12-29_Auto.pdf'

df = pd.DataFrame()

pdf_file = open(file, 'rb')
read_pdf = pdf.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()

page_content_list = page_content.split(sep=':')
print(page_content_list)

#for field in page_content_list:
#try:
df = df.append(pd.DataFrame({'aa': page_content_list[0],
                                'bb': page_content_list[1],
                                'cc': page_content_list[2],
                                'dd': page_content_list[3],
                                 'ee': page_content_list[4],
                                'ff': page_content_list[5],
                                'gg': page_content_list[6],
                                'hh': page_content_list[7],
                                'ii': page_content_list[8],
                                'jj': page_content_list[9],
                                'kk': page_content_list[10],
                                'll': page_content_list[11],
                                'mm': page_content_list[12]+
                                    page_content_list[13]+
                                    page_content_list[14]+
                                    page_content_list[15]+
                                    page_content_list[16]},
                               index = [0]), ignore_index=True)
#except IndexError:
    #break

df.to_csv('trans&Discl.csv',encoding='utf-8-sig')
