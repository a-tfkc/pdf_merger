# coding: utf-8

from PyPDF2 import PdfFileMerger
from tkinter import filedialog
from tkinter import *

FILES = []
LABELS = []


def open_files():
  global FILES, LABELS
  files = filedialog.askopenfilenames(initialdir = "~",
                                      title = "Choose PDF Files",
                                      filetypes = [("PDF Files", "*.pdf")])
  for file in files:
    FILES.append(file)

  # Create a label for each chosen pdf file
  i = 2
  for file in FILES:
    label = Label(root, text=file.split("/")[-1])
    label.grid(row=i, column=1)
    LABELS.append(label)
    i += 1

def clear_files():
  global FILES, LABELS
  FILES = []
  for label in LABELS:
    label.destroy()
  filename.delete(0, END)

def merge_files():
  global FILES
  if FILES != [] and filename.get() != "":
    merger = PdfFileMerger()
    for pdf in FILES:
      merger.append(pdf)
    location = filedialog.askdirectory(initialdir = "~",
                                       title = "Choose Location")
    if location != "":
      merger.write(location + "/" + filename.get() + ".pdf")
      merger.close()
      filename.delete(0, END)
      filename.insert(0, "DONE")

if __name__ == '__main__':

  root = Tk()
  root.title("PDF Merger")

  # Create entry + buttons
  filename = Entry(root)
  filename.insert(0, "Name your pdf")
  openfilesbutton = Button(root, text="Open Files", command=open_files)
  clearfilesbutton = Button(root, text="Delete Files", command=clear_files)
  mergefilesbutton = Button(root, text="Merge Files", command=merge_files)

  # Position entry + buttons
  filename.grid(row=0, column=4)
  openfilesbutton.grid(row=0, column=0)
  clearfilesbutton.grid(row=0, column=1)
  mergefilesbutton.grid(row=0, column=2)

  root.mainloop()
