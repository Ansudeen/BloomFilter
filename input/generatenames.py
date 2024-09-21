import random

def generate_usernames(count):
    first_names = [
        "Alice", "Bob", "Charlie", "David", "Emma", "Fiona", "George", 
        "Hannah", "Ivy", "Jack", "Kathy", "Liam", "Mia", "Noah", "Olivia", 
        "Paul", "Quinn", "Rachel", "Sam", "Tina", "Uma", "Victor", "Wendy", 
        "Xander", "Yara", "Zoe"
    ]
    
    last_names = [
        "Anderson", "Baker", "Clark", "Davis", "Evans", "Garcia", 
        "Hernandez", "Johnson", "King", "Lee", "Martinez", "Nelson", 
        "O'Connor", "Parker", "Robinson", "Smith", "Turner", "Walker", 
        "Young", "Zhang"
    ]
    
    usernames = set()
    
    while len(usernames) < count:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        number = random.randint(1, 9999)
        username = f"{first_name}.{last_name}{number}"
        usernames.add(username)
    
    return usernames

def write_usernames_to_file(usernames, filename):
    with open(filename, 'w') as file:
        for username in usernames:
            file.write(f"{username}\n")

if __name__ == "__main__":
    num_usernames = 100000
    usernames = generate_usernames(num_usernames)
    write_usernames_to_file(usernames, 'users.txt')
    print(f"Generated {num_usernames} realistic usernames and written to 'users.txt'.")
