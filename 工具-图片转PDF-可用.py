import os
from fpdf import FPDF
PDF = FPDF()
PDF.set_auto_page_break(0)
path = r'c:/imgs'
images = [i for i in os.listdir(path)]
NUM = 1
width = 200
height = 284
for index, image in enumerate(images):
    if index == 0:
        PDF.add_page()
    elif index % NUM ==0:
        PDF.add_page()
    PDF.image(os.path.join(path,image),w=width,h=height)
PDF.output(os.path.join(path,'test.pdf'),'F')
print ('转换完毕')