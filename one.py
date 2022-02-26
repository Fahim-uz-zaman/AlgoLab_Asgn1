import numpy as np
import sys

original_stdout = sys.stdout # Saving a reference to the original standard output

with open('uniform_data_set.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    for i in range(10**5):
        print(np.random.uniform(0, 1))

with open('normal_data_set.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    for i in range(10**5):
        print(np.random.normal(0.0, 1.0))

    sys.stdout = original_stdout # Reset the standard output to its original value
