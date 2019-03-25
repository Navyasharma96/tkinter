import smtplib
sender="mishuashrin9509@gmail.com"
reciever="apurvas494@gmail.com"
passwd="navya@sharma@mishu"
print("port started")
var=smtplib.SMTP("smtp.gmail.com",587)
print("port ended")
var.starttls()
var.login(sender,passwd)
message="it is a testing of smtp through the python"
subject="python"
print("for start")
var.sendmail(sender,reciever,message)
var.quit()
print ("sucessfull")