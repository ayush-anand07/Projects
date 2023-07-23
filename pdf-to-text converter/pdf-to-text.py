import os
import sys
from pypdf import PdfReader

if getattr(sys, 'frozen', False):
    pdf_dir = os.path.dirname(sys.executable)
else:
    pdf_dir = os.path.dirname(os.path.abspath(__file__))

# pdf_dir = os.path.dirname(__file__)
print(pdf_dir)
pdf_path_list = [f'{pdf_dir}/{filename}' for filename in os.listdir(pdf_dir) if filename.endswith('.pdf')]

for i in range(0, len(pdf_path_list)):
    # print(pdf_path_list[i])
    reader = PdfReader(pdf_path_list[i])
    page = reader.pages
    with open(f"{pdf_path_list[i].split('.')[0]}.txt", 'w', encoding='utf-8') as f:
        for j in range(0, len(page)):
            f.write((page[j].extract_text()))
os.startfile(pdf_dir)
print(f"{len(pdf_path_list)} pdf files converted to text file.")
os.system("pause")