import PyPDF2, sys, os

try:
	path = sys.argv[1]
	directory = sys.argv[2]
except IndexError:
	print("Please add the input and output folders\' names: \"python pdfmerger.py INPUT_FOLDER OUTPUT_FOLDER\"")
	exit()

if not os.path.exists(path):
	print('You need to create input folder first and put there the pdf files')
	exit()

pdf_list = os.listdir(path)

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(f'{path}/{pdf}')
	merger.write(f'{directory}/merged.pdf')

if not os.listdir(path):
	print(f'Put pdf files into the \"{sys.argv[1]}\" folder!')
else:
	if not os.path.exists(directory):
		os.makedirs(directory)
	pdf_combiner(pdf_list)