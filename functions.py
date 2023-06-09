"""all the functions"""
import os
import shutil
from docx import Document
from docx2pdf import convert
from PyPDF2 import PdfMerger, PdfReader


def combine_pdfs(file1, file2, file3):

    """Function to combine three pdfs"""
    # Create a merger object
    merger = PdfMerger()

    # Open the two PDF files and add them to the merger object
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2, open(file3, 'rb') as f3:
        pdf1 = PdfReader(f1)
        pdf2 = PdfReader(f2)
        pdf3 = PdfReader(f3)
        merger.append(pdf1)
        merger.append(pdf2)
        merger.append(pdf3)

    # Create a file name for the combined PDF file
    file2_name = os.path.splitext(os.path.basename(file2))[0]
    directory = os.path.dirname(file2)
    output_name = f'{directory}/{file2_name} Final.pdf'

    # Write the combined PDF file to disk
    with open(output_name, 'wb') as f:
        merger.write(f)

    return output_name



def word_to_pdf(input_file):
    """Convert the Word file to PDF using docx2pdf"""
    output_file = os.path.splitext(input_file)[0] + '.pdf'
    convert(input_file, output_file)




def replace_text_in_docx(docx_path, replaceable_text, replacement_text):
    """replace text in word file"""
    doc = Document(docx_path)
    for p in doc.paragraphs:
        if replaceable_text in p.text:
            inline = p.runs
            for elem in enumerate(inline):
                if replaceable_text in elem[1].text:
                    text = elem[1].text.replace(replaceable_text, replacement_text)
                    elem[1].text = text
    doc.save(docx_path)




def copy_file(src_path, dest_path):
    try:
        shutil.copy(src_path, dest_path)
        return
    except IOError as e:
        print(f"Unable to copy file: {e}")


def delete_files(filePath):
    """function to delete files using filepath"""
    if os.path.exists(filePath):
        os.remove(filePath)
        return
    return
