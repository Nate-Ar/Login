import os
import time
askuser = input('Username >  ')
usercorect = False;
usernames = []
passwords = []

# Opening and reading user.txt
with open('user.txt', 'r') as g:
    for x in g:
        usernames.append(x)
# Opening and reading pass.txt
with open('pass.txt', 'r') as b:
    for i in b:
        passwords.append(i)


# new account function
def newaccount():
    asknew = input('Do you want to make and account (Y/n) >  ')
    if asknew.lower() == 'y':
        newuser = input('What do you want your Username to be >  ')
        newpass = input('What do you want your Password to be>  ')
        with open('user.txt', 'a') as m:
            with open('pass.txt', 'a') as z:
                confurim = input('Retype Password>  ')
                if confurim == newpass:
                    z.write('\n')
                    z.write(newpass)
                    m.write('\n')
                    m.write(newuser)
                    print('ok your ready to go')
                else:
                    print('passwords dont match')
                    while True:
                        confurim = input('Retype Password>  ')
                        if confurim == newpass:
                            z.write('\n')
                            z.write(newpass)
                            m.write('\n')
                            m.write(newuser)
                            print('ok your ready to go')
                            break
                        else:print('passwords dont match')

    else:
        print('Ok Maybe Next Time')


# Checking Usernames
for c in usernames:
    if askuser + '\n' == c or askuser == c:
        var = usercorect = True
if usercorect == False:
    newaccount()
# Checking Passwords
if usercorect == True:
    askpass = input('Password >  ')
    for t in passwords:
        if askpass +'\n' == t or askpass == t:
            print('your in')
