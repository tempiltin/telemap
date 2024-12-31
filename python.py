import os
import random
import datetime

# Pascal fayllari uchun papka
if not os.path.exists("pascal"):
    os.makedirs("pascal")

# Tasodifiy Pascal kod namunalar
CODE_TEMPLATES = [
    "program HelloWorld; begin writeln('Hello, World!'); end.",
    "program SumTwoNumbers; var a, b: integer; begin a := 5; b := 10; writeln(a + b); end.",
    "program PrintNumbers; var i: integer; begin for i := 1 to 10 do writeln(i); end.",
    "program Factorial; var n, f, i: integer; begin n := 5; f := 1; for i := 1 to n do f := f * i; writeln(f); end.",
    "program ReverseString; var s: string; begin s := 'Pascal'; writeln(copy(s, length(s), 1)); end."
]

# 2025 yil yanvar-mart oylari kunlarini olish
def get_full_active_dates():
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2025, 3, 31)
    all_days = [(start_date + datetime.timedelta(days=i)) for i in range((end_date - start_date).days + 1)]
    return all_days

# Pascal faylini yaratish
def generate_pascal_file(file_name):
    code = random.choice(CODE_TEMPLATES)
    with open(file_name, "w") as f:
        f.write(code)

# Git commit va push
def commit_and_push(date, commit_count):
    for _ in range(commit_count):
        file_name = f"pascal/code_{date}_{random.randint(1, 10000)}.pas"
        generate_pascal_file(file_name)

        os.system("git add .")
        commit_date = date.strftime("%Y-%m-%dT%H:%M:%S")
        os.system(f'git commit --date="{commit_date}" -m "Commit on {commit_date}"')

    os.system("git push")

# Asosiy funksiya
def main():
    commit_dates = get_full_active_dates()

    for date in commit_dates:
        commit_count = random.randint(5, 20)
        commit_and_push(date, commit_count)
        print(f"✅ {date} kuni uchun {commit_count} ta commit bajarildi.")

if __name__ == "__main__":
    main()
