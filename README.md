# GOOSINT
## Get google search links in terminal
#### Tool desarrollada para extraer información de google sobre un objetivo.
![](https://i.ibb.co/1nVxcFR/banner.jpg)

#### First install dependency:
> python3 -m pip install googlesearch-python

### MODES
```
0-default: web list of query
1- list Subdomain
2- search for Passwords 
3- dork file FileExtension 
4- search for IndexOfDirectories 
```

### ARGS
```
-t --target DORK
-m --mode MODES
-e --ext File extension
-c --country Specify a country
-d --dorksource Read dorks from file >> Multiple Queryies, Multiple dorks - MASSIVE INFO
-o --output Save results in txt file
```

# EXAMPLES:

#### listar todas las urls de un query
> python3 goosint.py -t "query"

#### listar subdominios indexados por google
> python3 goosint.py -t target.com -m 1

#### verificar si hay passwords indexados que coincidan con el objetivo
> python3 goosint.py -t target.com -m 2

#### verificar archivos con una extension determinada sobre un objetivo
> python3 goosint.py -t target.com -m 3 -E pdf

#### verificar si un objetivo tiene directorios de archivos públicos indexados
> python3 goosint.py -t target.com -m 4
