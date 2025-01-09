import subprocess
import random
from datetime import datetime, timedelta
import os

def create_dated_commits():
    """
    Create fake git commits with specified date constraints:
    - Starts exactly one year ago from today
    - 1-5 commits per day
    - Commits between 10 AM and 10 PM
    """
    # Initialize git repo if not already initialized
    if not os.path.exists('.git'):
        subprocess.run(['git', 'init'])
    
    # Create a dummy file if it doesn't exist
    dummy_file = 'activity.txt'
    if not os.path.exists(dummy_file):
        with open(dummy_file, 'w') as f:
            f.write('Activity log\n')
    
    # Add file to git if not already tracked
    subprocess.run(['git', 'add', dummy_file])
    
    # Set default author info if not configured
    try:
        subprocess.run(['git', 'config', 'user.email'], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        subprocess.run(['git', 'config', 'user.email', 'test@example.com'])
        subprocess.run(['git', 'config', 'user.name', 'Test User'])
    
    # Calculate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    
    current_date = start_date
    while current_date <= end_date:
        # Generate random number of commits for the day (1-5)
        num_commits = random.randint(1, 5)
        
        # Generate random times for the commits between 10 AM and 10 PM
        commit_times = []
        for _ in range(num_commits):
            # Generate random hour between 10 and 22 (10 PM)
            hour = random.randint(10, 22)
            # Generate random minute
            minute = random.randint(0, 59)
            # Generate random second
            second = random.randint(0, 59)
            
            commit_time = current_date.replace(hour=hour, minute=minute, second=second)
            commit_times.append(commit_time)
        
        # Sort commit times to maintain chronological order
        commit_times.sort()
        
        # Create commits for each time
        for commit_time in commit_times:
            # Update the file
            with open(dummy_file, 'a') as f:
                f.write(f'Activity on {commit_time.strftime("%Y-%m-%d %H:%M:%S")}\n')
            
            # Stage the changes
            subprocess.run(['git', 'add', dummy_file])
            
            # Create the commit with the specified date
            env = os.environ.copy()
            env['GIT_AUTHOR_DATE'] = commit_time.isoformat()
            env['GIT_COMMITTER_DATE'] = commit_time.isoformat()
            
            subprocess.run([
                'git', 'commit',
                '-m', f'Activity logged on {commit_time.strftime("%Y-%m-%d %H:%M:%S")}',
            ], env=env)
            
            print(f'Created commit for {commit_time.strftime("%Y-%m-%d %H:%M:%S")}')
        
        # Move to next day
        current_date += timedelta(days=1)

if __name__ == '__main__':
    print("Starting commit generation...")
    create_dated_commits()
    print("Finished creating commits!")
