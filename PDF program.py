# -*- coding: utf-8 -*-
"""
Created on Thu May 18 10:51:28 2023

@author: zachm
"""
import pandas
import pdfquery
from pdfquery import PDFQuery
path1 = r'C: \your\pdf\path.pdf'
path2 = r'C:\your\pdf\path.pdf2.pdf'
pdf1 = PDFQuery(path1)
pdf1.load()
pdf2 = PDFQuery(path2)
pdf2.load()
# Use CSS-like selectors to locate the elements
#text_elements = pdf1.pq('LTTextLineHorizontal')
#text_elements = pdf2.pq('LTTextLineHorizontal')


# Extract the text from the elements
#text = [t.text for t in text_elements]
#convert the pdf to XML
pdf1.tree.write('bookofbusinessreveiw1.xml', pretty_print = True)




print(text)