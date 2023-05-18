import requests




url = input('[+] Enter the url : ')
dict_file = input('[+] Enter the file name {Just Enter for default File} : ')

if dict_file == '':
    dict_file = 'DirectoryBruteForceDict.txt'
else:
    pass



def req(URL):
    try:
        return requests.get('http://' + URL)
    except requests.exceptions.ConnectionError:
        pass



File = open(dict_file, 'r')

for l in File:
    directory = l.strip()
    N_url = url + '/' + directory
    response = req(N_url)
    if response:
        print('[*] Found :', N_url)

        
