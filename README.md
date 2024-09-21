Introduction
Bloom Filters are powerful probabilistic data structures that efficiently test whether an element is a member of a set. They use a fixed amount of memory and allow for false positives, making them ideal for scenarios where space is at a premium.


1.1 What is a Bloom Filter?

A Bloom Filter is a space-efficient data structure that allows for fast membership checks. It uses multiple hash functions to map items to a bit array. The trade-off for its efficiency is that it may return false positives.

1.2 Key Components:

Bit Array: A fixed-size array initialized to zeros.

Hash Functions: Functions that generate indices in the bit array.


Installation
To run the Bloom Filter example, ensure you have Python installed on your system. You can download Python from python.org.

Clone the Repository: Open your terminal and run the following command to clone the repository:
git clone https://github.com/Ansudeen/BloomFilter.git

Navigate to the Project Directory: Change your directory to the cloned repository:
cd BloomFilter

Create a Virtual Environment (Optional): It's a good practice to use a virtual environment. You can create one using:
python -m venv venv

Activate the virtual environment:
On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Run the Bloom Filter Example: You can run the Bloom Filter example by executing the following command:
python src/BloomFilters.py

Check Results: The program will output whether specific email addresses (derived from usernames) are in the Bloom Filter, along with checks for unknown email addresses.

Example
When you run the example, you should see output similar to:
Is 'Alice@example.com' in the Bloom filter? True
Is 'unknown@example.com' in the Bloom filter? False
This indicates whether the specified email addresses are likely present in the set.

Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
