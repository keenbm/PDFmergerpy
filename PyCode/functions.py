# File Path borwser

from tkinter import *
from tkinter import filedialog
import os
import PyPDF2
import datetime

import logging
logger = logging.getLogger()
log = logging.getLogger(__name__)

def get_file_path():
    try:
        filename = filedialog.askopenfilename(title='open')
        return filename
    except Exception as e:
        pass


def merge_pdf(folder_path,pdf_file_list):
    today = datetime.datetime.now()
    date_time = today.strftime("%m%d%Y_%H%M%S_")
    mergeFile = PyPDF2.PdfFileMerger()
    file_list = pdf_file_list
    log.info("merge_pdf Function : Merging PDF")
    try:
        for pdf in pdf_file_list:
            if len(pdf_file_list)>1:
                mergeFile.append(PyPDF2.PdfFileReader(folder_path + "\\" + pdf, 'rb'))
        mergeFile.write(folder_path + "\\" + date_time+"MergedFile.pdf")
        log.info("New Merger PDF created with name :  "+ date_time + "MergedFile.pdf")
    except Exception as e:
        log.error("merge_pdf Function : Error occurred while merging pdf")
        log.exception("Exception occurred : " + str(e))

def get_all_files(folder_path):
    log.info("get_all_files Function ")
    try:
        all_file_list = os.listdir(folder_path)
    except Exception as e:
        log.error("get_all_files Function : Error occurred while fetching file name")
        log.exception("Exception occurred : " + str(e))
    pdf_file_list = []
    try:
        for file in all_file_list:
            if file.find("pdf") > 0:
                pdf_file_list.append(file)
        return(all_file_list,pdf_file_list)
    except Exception as e:
        log.error("get_all_files Function : Error occurred while iterating file name")
        log.exception("Exception occurred : " + str(e))