import os
import datetime
import subprocess

# Sana oralig‘i
start_date = datetime.date(2025, 1, 1)
end_date = datetime.date(2025, 3, 31)

# Har kun uchun commit va push
current_date = start_date
while current_date <= end_date:
    # 1. README.md fayliga o‘zgarish kiritish
    with open("README.md", "a") as f:
        f.write(f"\nUpdate for {current_date}")

    # 2. git add .
    subprocess.run(["git", "add", "."], check=True)

    # 3. git commit -m "asd" (env bevosita funksiyada)
    subprocess.run(
        ["git", "commit", "-m", "asd"],
        check=True,
        env={**os.environ, "GIT_AUTHOR_DATE": f"{current_date}T12:00:00", "GIT_COMMITTER_DATE": f"{current_date}T12:00:00"}
    )

    # 4. git push (env bilan)
    subprocess.run(
        ["git", "push"],
        check=True,
        env={**os.environ, "GIT_AUTHOR_DATE": f"{current_date}T12:00:00", "GIT_COMMITTER_DATE": f"{current_date}T12:00:00"}
    )

    # 5. Keyingi kunga o'tish
    current_date += datetime.timedelta(days=1)
