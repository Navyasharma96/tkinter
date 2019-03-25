import smtplib
sender="mishuashrin9509@gmail.com"
reciever="apurvas494@gmail.com"
r2="er.harminder2019@gmail.com"
r3="priyajassal499@gmail.com",
receiver=["apurvas494@gmail.com","er.harminder2019@gmail.com","priyajassal499@gmail.com"]
passwd="navya@sharma@mishu"
print("port started")
var=smtplib.SMTP("smtp.gmail.com",587)
print("port ended")
var.starttls()
var.login(sender,passwd)
message="it is a testing of smtp through the python"
subject="python"
print("for start")
for i in receiver:
  var.sendmail(sender,i,message)
var.quit()
print ("sucessfull")