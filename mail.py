import smtplib
from email.mime.text import MIMEText
def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
def send_email(content):
    sender = "uskhuunymdavaa9@gmail.com"
    password = "diky pwdc zhwh xwdh"
    receiver = "kenshimobile13@gmail.com"

    msg = MIMEText(content)
    msg["Subject"] = "File-ээс явуулсан email 😎"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

# 🚀 main
def main():
    data = read_file("mail.txt")
    print("File уншигдлаа:\n", data)

    send_email(data)
    print("Email амжилттай явлаа 📧🔥")

main()