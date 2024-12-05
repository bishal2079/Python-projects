import smtplib 
my_email="sharmabishal037@gmai.com"
password="9846899643"
connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_address=my_email, to_address="bisalsharma77@gmail.com",msg="hello")