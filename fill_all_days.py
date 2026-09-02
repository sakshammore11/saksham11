import os
import random
import subprocess
from datetime import datetime, timedelta

# Account created on Oct 12, 2025
START_DATE = datetime(2025, 10, 13)
END_DATE = datetime(2026, 9, 2)

current_date = START_DATE
total_commits = 0

# Set git user name and github noreply email
EMAIL = "237561937+sakshammore11@users.noreply.github.com"
NAME = "sakshammore11"

subprocess.run(['git', 'config', 'user.name', NAME], check=True)
subprocess.run(['git', 'config', 'user.email', EMAIL], check=True)

while current_date <= END_DATE:
    # 2 to 5 commits per day to give a rich green graph
    num_commits = random.randint(2, 5)
    
    for i in range(num_commits):
        hour = random.randint(9, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        
        commit_dt = current_date.replace(hour=hour, minute=minute, second=second)
        date_str = commit_dt.strftime('%Y-%m-%dT%H:%M:%S+05:30')
        
        with open('data.json', 'w') as f:
            f.write(f'{{"date": "{date_str}", "commit_num": {total_commits + 1}}}\n')
        
        subprocess.run(['git', 'add', 'data.json'], check=True)
        
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = date_str
        env['GIT_COMMITTER_DATE'] = date_str
        env['GIT_AUTHOR_EMAIL'] = EMAIL
        env['GIT_COMMITTER_EMAIL'] = EMAIL
        env['GIT_AUTHOR_NAME'] = NAME
        env['GIT_COMMITTER_NAME'] = NAME
        
        subprocess.run(
            ['git', 'commit', '-m', f'Commit for {date_str}'],
            env=env,
            check=True,
            stdout=subprocess.DEVNULL
        )
        total_commits += 1
        
    current_date += timedelta(days=1)

print(f'Successfully created {total_commits} commits with official GitHub noreply email ({EMAIL}).')
