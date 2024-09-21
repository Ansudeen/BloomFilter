import hashlib

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        """Generate hash values for the item using multiple hash functions."""
        hashes = []
        for i in range(self.hash_count):
            hash_result = hashlib.md5(f"{item}{i}".encode()).hexdigest()
            hashes.append(int(hash_result, 16) % self.size)
        return hashes

    def add(self, item):
        """Add an item to the Bloom filter."""
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def check(self, item):
        """Check if an item is in the Bloom filter."""
        for hash_value in self._hashes(item):
            if self.bit_array[hash_value] == 0:
                return False
        return True

def generate_email(username):
    return f"{username}@example.com"

def load_usernames(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def main():
    # Define Bloom filter parameters
    bloom_size = 100000  # Adjust size based on expected number of users
    hash_count = 5

    # Create Bloom filter
    bloom = BloomFilter(size=bloom_size, hash_count=hash_count)

    # Load usernames from file
    usernames_file = './input/users.txt'  # Adjust the path based on your structure
    usernames = load_usernames(usernames_file)

    # Add email addresses to Bloom filter
    for username in usernames:
        email = generate_email(username)
        bloom.add(email)

    # Example: Check for a specific email
    test_email = generate_email("Alice")  # Replace with an actual username from your file
    print(f"Is '{test_email}' in the Bloom filter? {bloom.check(test_email)}")  # Expected: True or False
    print(f"Is 'unknown@example.com' in the Bloom filter? {bloom.check('unknown@example.com')}")  # Expected: False (may return True due to false positives)

if __name__ == "__main__":
    main()
