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
  i = 1
  for file in FILES:
    label = Label(root, relief=GROOVE, text=file.split("/")[-1])
    label.grid(row=i, column=0, columnspan=3, padx=5, sticky=W+E+N+S)
    LABELS.append(label)
    i += 1

def clear_files():
  global FILES, LABELS
  FILES = []
  for label in LABELS:
    label.destroy()

def merge_files():
  global FILES
  if FILES != []:
    merger = PdfFileMerger()
    for pdf in FILES:
      merger.append(pdf, import_bookmarks=False)
    location = filedialog.asksaveasfile(initialdir = "~", 
                                      title = "Merge Files", 
                                      filetypes = [("PDF", "*.pdf")],
                                      defaultextension=".pdf")
    if location != None:
      merger.write(location.name)
      merger.close()


if __name__ == '__main__':

  root = Tk()
  root.title("PDF Merger")
  root.resizable(width=False, height=False)

  # Create entry + buttons
  clear = Button(root, text="Delete Files", command=clear_files)
  open = Button(root, text="Open Files", command=open_files)
  merge = Button(root, text="Merge Files", command=merge_files)

  # Position entry + buttons
  clear.grid(row=0, column=0, padx=10, pady=10, sticky=W+E+N+S)
  open.grid(row=0, column=1, padx=10, pady=10, sticky=W+E+N+S)
  merge.grid(row=0, column=2, padx=10, pady=10, sticky=W+E+N+S)

  # Center window
  root.eval('tk::PlaceWindow . center')

  root.mainloop()
