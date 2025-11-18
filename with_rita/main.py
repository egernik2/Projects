LOGINS = ['egernik2']
PASSWORDS = ['passw0rd']

def main():
    print('Wellcome to login app')
    login = input('Login: ')
    password = input('Password: ')
    if login in LOGINS and password in PASSWORDS:
        print('Access granted')
    else:
        print('Access denied')

if __name__ == '__main__':
    main()