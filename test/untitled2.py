# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:19:51 2020

@author: 17862
"""

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]
print(onlyfiles,type(onlyfiles))
import PyPDF2
onlyfiles.remove('untitled2.py')
c=1
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO




#for i in range(len(onlyfiles)):
'''
    pdfFileObj = open(onlyfiles[i],'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #print(pdfReader.numPages)
    pageObj=pdfReader.getPage(0)
    a=pageObj.extractText()
    #print(a)
    #print(type(a))
    count=0
   
    for line in a.splitlines():
        if (line.find('niversity')!=-1 or line.find('ollege')!=-1):
            count=count+1
            if(count==2):
                print(c,line.strip())
                print()
                c=c+1
        #if (line.find('Boston College')!=-1):
         #   print(a)
    if (i==6):
        print(a)
    pdfFileObj.close()'''
    
    #print(convert_pdf_to_txt('Antonio_Cevallos_Resume_200903.pdf'))






from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.converter import TextConverter
import io

resource_manager = PDFResourceManager()
fake_file_handle = io.StringIO()
converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
page_interpreter = PDFPageInterpreter(resource_manager, converter)

with open('Antonio_Cevallos_Resume_200903.pdf', 'rb') as fh:

    for page in PDFPage.get_pages(fh,
                                  caching=True,
                                  check_extractable=True):
        page_interpreter.process_page(page)

    text = fake_file_handle.getvalue()

# close open handles
converter.close()
fake_file_handle.close()

print(text)





