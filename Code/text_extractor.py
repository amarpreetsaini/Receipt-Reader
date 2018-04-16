try:
	import Image
except ImportError:
	from PIL import Image
from pytesseract import pytesseract
file = 'Receipts/20180413_224908.jpg'
pytesseract.run_tesseract(file, 'output', extension='', lang=None, config="hocr")

with open('output.hocr', 'rb') as output_file:
    hocr_data = output_file.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(hocr_data, 'html.parser')

data_list = []

for span in soup.find_all('span'):
	text_string = span.text
	coordinates = ','.join(span.get('title').split(' ')[1:5]).rstrip(';')
	coordinates_tuple = tuple(coordinates.split(','))
	data_list.append((coordinates_tuple, text_string))

left_dict = [data for data in data_list]

print(left_dict)

for data in data_list:
	print(data[0][0], data[1])

