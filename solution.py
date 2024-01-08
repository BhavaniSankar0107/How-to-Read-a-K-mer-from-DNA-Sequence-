#Here in this code we are finding the repeated string of length 9
from collections import Counter

# Specify the path to your file
file_path = "Vibrio_cholerae.txt"  # Replace with the actual path to your file

# Read the sequence from the file
with open(file_path, 'r') as file:
    sequence = file.read()

# Perform further analysis on the sequence as needed
# For example, finding and counting 9-mers:
k = 9
n_mers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]

# Count the occurrences of each 9-mer
mer_counts = Counter(n_mers)

# Find the most occurred 9-mer
most_occurred_9mer, count = mer_counts.most_common(1)[0]

# Display the result
print(f"The most occurred 9-mer: {most_occurred_9mer}, Count: {count}")
