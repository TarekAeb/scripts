
import random
from datetime import datetime, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define the people
dishwashers = ["Zaki", "Dahmen", "Badro"]
cook_cleaners = ["Tarek", "Abdelhak", "Akram", "Hamza"]

# Define the schedule period
start_date = datetime(2025, 3, 12)
end_date = datetime(2025, 3, 19)
num_days = (end_date - start_date).days + 1

# Initialize the schedule dictionary
schedule = {person: [] for person in dishwashers + cook_cleaners}

# Assign dishwashing task (same every day)
for person in dishwashers:
    for i in range(num_days):
        current_date = start_date + timedelta(days=i)
        date_str = current_date.strftime("%Y-%m-%d")
        schedule[person].append((date_str, "Wash Dishes"))

# Shuffle cook_cleaners to distribute tasks fairly
random.shuffle(cook_cleaners)

# Assign cooking and cleaning tasks ensuring each person gets 4 cooking and 2 cleaning tasks
cook_cleaner_tasks = {person: {"Cook": 0, "Clean Floor": 0} for person in cook_cleaners}

dates = [start_date + timedelta(days=i) for i in range(num_days)]

task_distribution = {date.strftime("%Y-%m-%d"): {"Cook": [], "Clean Floor": None} for date in dates}

for date in dates:
    date_str = date.strftime("%Y-%m-%d")

    # Get the least assigned cook_cleaners for cooking
    available_cooks = sorted(cook_cleaners, key=lambda x: cook_cleaner_tasks[x]["Cook"])
    selected_cooks = available_cooks[:2]

    for cook in selected_cooks:
        schedule[cook].append((date_str, "Cook"))
        cook_cleaner_tasks[cook]["Cook"] += 1
    task_distribution[date_str]["Cook"] = selected_cooks

    # Get the least assigned cook_cleaner for floor cleaning
    available_cleaners = sorted([p for p in cook_cleaners if p not in selected_cooks], key=lambda x: cook_cleaner_tasks[x]["Clean Floor"])
    selected_cleaner = available_cleaners[0]

    schedule[selected_cleaner].append((date_str, "Clean Floor"))
    cook_cleaner_tasks[selected_cleaner]["Clean Floor"] += 1
    task_distribution[date_str]["Clean Floor"] = selected_cleaner

# Function to send email
def send_email(to_email, subject, body):
    from_email = "t6tarek@gmail.com"
    password = "" # Add your email password here

    # Set up the server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()
    server.login(from_email, password)

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Cc'] = "t6tarek@gmail.com"
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server.send_message(msg)
    server.quit()

# Define email addresses for each worker
email_addresses = {
    "Zaki": "zakaria.chetouane@ensia.edu.dz",
    "Dahmen": "abderrahmen.mehaddi@ensia.edu.dz",
    "Badro": "badreddine.zerraf@ensia.edu.dz",
    "Tarek": "abdelbari.tarek.sibachir@ensia.edu.dz",
    "Abdelhak": "abdelhak.benbouziane@ensia.edu.dz",
    "Akram": "abderrehmane.mohamed.akram.seddik@ensia.edu.dz",
    "Hamza": "hamza.abderaouf.khentache@ensia.edu.dz",
}

# Send the schedule via email
for person, tasks in schedule.items():
    body = f"This email is generated automatically, please don't respond to it\n\n Schedule for {person}:\n\n"
    for task in tasks:
        body += f"{task[0]}: {task[1]}\n"
    body+= f"\n\n Saha ramdankom\n\nBest regards,\ndevelopeur"
    # Send email to the person
    send_email(email_addresses[person], f"Ramadan Schedule for {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}", body)
    print(f"Email sent to {person}")

# Print the schedule for each person
for person, tasks in schedule.items():
    print(f"Schedule for {person}:")
    for task in tasks:
        print(f"{task[0]}: {task[1]}")
    print("\n")