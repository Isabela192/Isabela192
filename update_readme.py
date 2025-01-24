from datetime import datetime

def update_readme():
    days_left = (datetime(2026, 1, 1) - datetime.now()).days
    
    with open('README.md', 'r') as file:
        content = file.read()
    
    updated_content = content.replace('{var_days}', str(days_left))
    
    with open('README.md', 'w') as file:
        file.write(updated_content)

if __name__ == "__main__":
    update_readme()