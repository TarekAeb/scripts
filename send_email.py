import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials (use environment variables instead of hardcoding in production)
EMAIL_ADDRESS = "t6tarek@gmail.com"
EMAIL_PASSWORD = "jyqv qhbs zoxv digg"

# SMTP settings for Gmail (change if using another provider)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# List of recipients (name, email)
recipients = [
    ("Tarek", "tareksibachir01@gmail.com"),
    ("Akram", "abdelbari.tarek.sibachir@ensia.edu.dz"),
    ("Charlie", "charlie@example.com"),
]

# Email sending function
def send_email(name, recipient_email):
    # TODO: edit the email subject and body
    subject = "Invitation to the Olympole Closing Ceremony 🎉!"
    body = f"Dear {name},\n\nWe are delighted to invite you to the closing ceremony of Olympole, which will take place on Thursday, February 27. This special occasion marks the culmination of an incredible journey filled with competition, talent, and teamwork.\nDuring the ceremony, we will:\n- 🎖️ Honor and reward the champions of each Olympole activity
🏆 Announce the winners of the Mathematical Olympiad and Drawing Competition\nWe also take this opportunity to express our sincere gratitude for your support and contributions, which played a vital role in making this event a success. Your presence would mean a lot as we celebrate the achievements of all participants together.\nWe look forward to welcoming you!\nBest regards,\nENSIA Sport & Culture Club\n\nالسيد/السيدة {name} المحترم/المحترمة،\nيسعدنا أن ندعوكم لحضور حفل اختتام\nOlympole يوم الخميس 27 فبراير. هذا الحدث يمثل لحظة مميزة نختم بها رحلة رائعة مليئة بالتحديات، الإبداع، والعمل الجماعي.\n\nخلال الحفل، سنقوم بـ:\n🏆 الإعلان عن الفائزين في أولمبياد للرياضيات ومسابقة الرسم\n🎖️ تكريم الأبطال في مختلف أنشطة أوليمبول\n\nكما ننتهز هذه الفرصة لنتوجه إليكم بجزيل الشكر والتقدير لدعمكم الكبير ومساهمتكم القيمة، التي كان لها أثر كبير في نجاح هذا الحدث. سيكون لحضوركم معنا وقع خاص ونحن نحتفي بإنجازات جميع المشاركين.\n\nبانتظاركم بكل سرور!\n\nأطيب التحيات،\nENSIA Sport & Culture Club"

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())

# Send emails to all recipients
for name, email in recipients:
    send_email(name, email)
    print(f"Email sent to {name} at {email}")


