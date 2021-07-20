from tkinter import *
import os


from PyPDF2 import PdfFileReader, PdfFileMerger
pdf_file1=PdfFileReader("pdf1.pdf")
pdf_file2=PdfFileReader("pdf2.pdf")
output=PdfFileMerger()
output.append(pdf_file1)
output.append(pdf_file2)
output.write("mergedfile.pdf")

if output :

    def main_account_screen():
        global main_screen
        main_screen = Tk()
        main_screen.geometry("300x250")
        #main_screen.title("SUCCESS")
        Label(text="Your pdf has been merged", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
        #Label(text="").pack()
        #Button(text="Login", height="2", width="30", command = login).pack()
        #Label(text="").pack()
        #Button(text="Register", height="2", width="30", command=register).pack()

        main_screen.mainloop()
 
 
main_account_screen()
