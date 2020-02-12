from googlesearch import search
from argparse import ArgumentParser
import os
import sys

print("=======================================================================\n")
print("Goosint by Juan Cruz Tommasi - Base4 Security - www.base4sec.com\n")
print("=======================================================================\n\n")
print("It will start in a minute, please wait..\n\n")

parser = ArgumentParser(description='Goosint by Juan Cruz Tommasi - Base4 Security - www.base4sec.com')

parser.add_argument('-t', '--target', type=str, metavar='', help='Target')
parser.add_argument('-m', '--mode', type=int, metavar='', required=True, help='1-Subdomain 2-Passwords 3-FileExtension 4-IndexOfDirectories')
parser.add_argument('-E', '--ext', type=str, metavar='', help='File extension')

args = parser.parse_args()

results = []
query = ''

def searchCall(query):
	for i in search(query, num=100, start=0, stop=0, pause=23.3):
		print(i)
	pass

if args.mode == 1:
	query = 'site:%s -site:www.%s' % (args.target, args.target)

	pass
elif args.mode == 2:
	query = 'site:%s intext:password' % (args.target)
	pass
elif args.mode == 4:
	site = args.target
	org = site.split('.')[0]
	query = 'intitle:"indexof /" site:%s inurl:%s' % (args.ext, site.replace(org,''), org)
	pass

elif args.mode == 3:
	if args.ext:
		query = 'filetype:%s site:%s' % (args.ext, args.target)
	else:
		sys.exit("Declara por favor una extension para los archivos a listar con -E --ext\n")

searchCall(query)
