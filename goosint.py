from googlesearch import search
from argparse import ArgumentParser
import os
import random
import time
import sys

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    if v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean Value Expected')

def insertResultsInFile(result, filename):
        try:
                file = open(filename, 'a+')
                file.write(result + "\n")
        except IOError:
                print("error writing file")
def banner():
        print("\n\n=======================================================================\n")
        print("Goosint by Juan Cruz Tommasi - Base4 Security - www.base4sec.com\n")
        print("=======================================================================\n\n")
        print("Results in a minute, please wait..\n\n")

def utfEncodeAndLinesToArray(filename):
    file = ''
    try:
            file = open(filename, 'r')
    except IOError:
            print("Error reading file > " + file)
    dorks = file.read()
    dorks = dorks.unicode()
    dorks = dorks.splitlines()
    return dorks

parser = ArgumentParser(description='Goosint by Juan Cruz Tommasi - Base4 Security - www.base4sec.com')

parser.add_argument('-t', '--target', type=str, metavar='', help='Target')
parser.add_argument('-m', '--mode', type=int, metavar='',default=0 ,required=False, help='1-Subdomain 2-Passwords 3-FileExtension 4-IndexOfDirectories, (default 0: weblist)')
parser.add_argument('-E', '--ext', type=str, metavar='', help='File extension')
parser.add_argument('-C', '--country', type=str, metavar='', help='Specify a country', default='')
parser.add_argument('-D', '--dorksource', type=str, metavar='', default=False, help='Multiple Queryies, Multiple dorks - MASSIVE INFO')
parser.add_argument('--save', type=str2bool, nargs='?', const=True, default=False, help='Save results in txt file')

args = parser.parse_args()

results = []
query = ''
fn = ''

def searchCall(query):
    iterator = 0
    for result in search(query, num_results=100,lang="es"):
            insertResultsInFile(result, "log.txt")
            iterator = iterator + 1
            print('[' + str(iterator) + '] - ' + result)
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

elif args.mode == 0:
    query = '%s' % (args.target)
    pass

######################
#execution
######################

banner()

if args.dorksource != False:
    dorks = utfEncodeAndLinesToArray(args.dorksource)
    print("[*] Dork file readed successfully")
    sleeptimeAcc = 0
    for dork in dorks:
        safeSearchTime = random.randint(200,500)
        if sleeptimeAcc != 0:
            print("[*] Sleeping %s seconds until next dork scraping.. ", safeSearchTime)
            time.sleep(safeSearchTime)
            sleeptimeAcc = sleeptimeAcc + safeSearchTime
        print("[*] Scraping websites from: %s", dork)
        searchCall(dork)
else:
    if len(query) != 0:
        searchCall(query)
    else:
        print("[!] No query Specified")
