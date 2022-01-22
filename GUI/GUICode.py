# Importing Libray
from tkinter import *
import os
import PyPDF2
import re
import datetime

from PyCode.functions import merge_pdf
from PyCode.functions import get_all_files
import logging
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='w')
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# GUI Functions

def submit_click():
    logging.info("Submit button Clicked")
    pdf_file_output.delete(0.0, END)
    all_file_output.delete(0.0, END)

    folder_Path = folder_path_text.get()
    logging.info("Enter folder path is : " + folder_Path)

    logging.info("Calling Get all file function")
    all_file_list, pdf_file_list = get_all_files(folder_Path)

    logging.info("Printing all file list")
    for file in all_file_list:
        all_file_output.insert(END,f"{file}\n")

    logging.info("Printing PDF file list")
    for file in pdf_file_list:
        pdf_file_output.insert(END, f"{file}\n")

def pdf_click():
    logging.info("PDF Merge Button Clicked")
    logging.info("Calling Get all file function")
    folder_Path = folder_path_text.get()
    logging.info("Enter folder path is : " + folder_Path)
    all_file_list, pdf_file_list = get_all_files(folder_Path)
    logging.info("Merge PDF function")
    merge_pdf(folder_Path,pdf_file_list)
    pdf_file_output.delete(0.0,END)
    all_file_list, pdf_file_list = get_all_files(folder_Path)
    logging.info("Updating PDF list after Merging")
    for file in pdf_file_list:
        pdf_file_output.insert(END, f"{file}\n")

def clear_click():
    logging.info("Clear Button Clicked")
    pdf_file_output.delete(0.0, END)
    all_file_output.delete(0.0, END)

## Initiating Tk Window
window=Tk()
window.title("PDF Merger")
window.configure(background="#0e5c6e")
window.geometry('900x600')

# Adding title image
title_img=PhotoImage(file="Title.png")
Label (window,image=title_img,bg="black").grid(row=0,column=0,sticky="w")

# Create label for Enter path
Label (window,text="Enter path : ",bg="#0e5c6e",fg="white",font="none 12 bold").grid(row=1,column=0,sticky="e")

# Adding Text box for folder path entry
folder_path_text=Entry(window,width=40,bg="white")
folder_path_text.grid(row=1,column=1,sticky="w")

## Adding submit button
submit_button=Button(window,text="Submit",relief=SOLID,width=8,command=submit_click,pady=10)
submit_button.grid(row=1,column=2,sticky="w")


# Print all File List
Label (window,text="\nAvailable Files in enter folder are as below : ",bg="#0e5c6e",fg="white",
       font=("Arial", 10,"bold")).grid(row=3,column=0,sticky="w")
all_file_output=Text(window,width=50,height=20,wrap=WORD,bg="white",fg="black",font=("Arial", 10))
all_file_output.grid(row=4,column=0,sticky="w")


# Print pdf File List
Label (window,text="\nAvailable PDF Files : ",bg="#0e5c6e",fg="white",font=("Arial", 10,"bold")).grid(row=3,column=1,
                                                                                                      sticky="w")
pdf_file_output=Text(window,width=50,height=20,wrap=WORD,bg="white",fg="black",font=("Arial", 10))
pdf_file_output.grid(row=4,column=1,sticky="w")


## Adding button for pdf merger
pdf_button=Button(window,text="Merge PDF and\n Update List",relief=SOLID,width=12,command=pdf_click,pady=10)
pdf_button.grid(row=4,column=3,sticky="w")


## Adding button for clear
clear_button=Button(window,text="clear_all",relief=SOLID,width=12,command=clear_click,pady=10)
clear_button.grid(row=5,column=3,sticky="w")



## Run GUI
logging.info("Start of code Open GUI main Window")
window.mainloop()