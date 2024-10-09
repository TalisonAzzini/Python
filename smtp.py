import smtplib

smtp_server = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(smtp_server, port)
server.starttls()

remetente_email = REMETENTE_EMAIL
receptor_email = input("E-mail do  destinatário: ")
assunto = input("Assunto: ")
mensagem = input("Mensagem: ")

server.login(remetente_email, REMETENTE_SENHA)
text = f"Subject: {assunto}\n\n{mensagem}"

server.sendmail(remetente_email, receptor_email, text)
print("E-mail enviado para " + receptor_email)
