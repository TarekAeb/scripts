import random
import json
import smtplib
from email.mime.text import MIMEText

# Define the team members
only_dishwashers = ["zaki", "Dahmen", "Badro"]  # 3 people
cooks_and_dishwashers_and_cleaners = ["Tarek", "Abdelhak", "hamza", "akram"]  # 4 people
all_members = only_dishwashers + cooks_and_dishwashers_and_cleaners

days = ["March 12", "March 13", "March 14", "March 15", "March 16", "March 17", "March 18", "March 19"]

# Task weights
TASK_WEIGHTS = {
    "Cooking": 0.42,
    "Dishwashing": 0.33,
    "Floor Cleaning": 0.25
}

# Track workload per member
workload = {member: 0 for member in all_members}

timetable = {}

for day in days:
    # Select 2 cooks ensuring balanced workload
    cooks = sorted(cooks_and_dishwashers_and_cleaners, key=lambda x: workload[x])[:2]
    for cook in cooks:
        workload[cook] += TASK_WEIGHTS["Cooking"]
    
    # Select 3 dishwashers ensuring balanced workload
    remaining_dishwashers = list(set(only_dishwashers + cooks_and_dishwashers_and_cleaners) - set(cooks))
    dishwashers = sorted(remaining_dishwashers, key=lambda x: workload[x])[:3]
    for dishwasher in dishwashers:
        workload[dishwasher] += TASK_WEIGHTS["Dishwashing"]
    
    # Select 1 floor cleaner ensuring balanced workload
    cleaner = sorted(cooks_and_dishwashers_and_cleaners, key=lambda x: workload[x])[0]
    workload[cleaner] += TASK_WEIGHTS["Floor Cleaning"]
    
    # Store in timetable
    timetable[day] = {
        "Cooking": cooks,
        "Dishwashing": dishwashers,
        "Floor Cleaning": cleaner
    }

# Save timetable to a JSON file
with open("timetable.json", "w") as f:
    json.dump(timetable, f, indent=4)

print("Timetable generated and saved to timetable.json!")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
# Email sending function
def send_email(to_email, subject, body):
    sender_email = "t6tarek@gmail.com"  # Replace with your email
    sender_password = "jyqv qhbs zoxv digg"  # Replace with your App Password
    
    msg = MIMEText()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email
    msg.attach(MIMEText(body, "plain"))
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")

# Define emails for each person (replace with actual emails)
emails = {
    "Tarek": "abdelbari.tarek.sibachir@ensia.edu.dz",
    # "Person B": "@ensia.edu.dz",
    # "Person C": "@ensia.edu.dz",
    # "Person D": "@ensia.edu.dz",
    # "Person E": "@ensia.edu.dz",
    # "Person F": "@ensia.edu.dz",
    # "Person G": "@ensia.edu.dz"
}

# Send personalized emails
for person, email in emails.items():
    schedule = []
    print(f"Attempting to send email to {email} for {person} with schedule: {schedule}")
    for day, tasks in timetable.items():
        for role, workers in tasks.items():
            print(f"Checking {person} in {workers}")
            if isinstance(workers, list) and person in workers:  # Ensure it's a list
                schedule.append(f"{day}: {role}")
                print(f"Added {day}: {role} to {person}'s schedule")
            elif isinstance(workers, str) and person == workers:  # Handle single cleaner
                schedule.append(f"{day}: {role}")
