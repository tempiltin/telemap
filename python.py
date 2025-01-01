import os
import datetime
import subprocess

# Sana oralig‘i
start_date = datetime.date(2025, 1, 1)
end_date = datetime.date(2025, 3, 31)

# Har kun uchun commit va push
current_date = start_date
while current_date <= end_date:
    # Fayl yaratamiz (har xil nom bilan)
    filename = f"daily_commit_{current_date}.txt"
    with open(filename, "w") as f:
        f.write(f"Commit for {current_date}")

    # Git add
    subprocess.run(["git", "add", "."], check=True)

    # Sana UTC formatda commitga beriladi
    date_str = f"{current_date}T12:00:00"
    
    # Git uchun vaqt muhit o‘zgaruvchilarini sozlash
    os.environ["GIT_AUTHOR_DATE"] = date_str
    os.environ["GIT_COMMITTER_DATE"] = date_str

    # Commit
    subprocess.run(["git", "commit", "-m", f"Commit for {current_date}"], check=True)

    # Push
    subprocess.run(["git", "push"], check=True)

    current_date += datetime.timedelta(days=1)
