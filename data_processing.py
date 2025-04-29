import sys

def read_data(file_path):
    # Read numbers from a file
    with open(file_path, 'r') as file:
        lines = file.readlines()
        numbers = [float(line.strip()) for line in lines if line.strip()]
    return numbers

def calculate_sum(numbers):
    # Calculate sum of the numbers
    return sum(numbers)

def calculate_average(numbers):
    # Calculate average of the numbers
    return sum(numbers) / len(numbers) if numbers else 0

def write_results(output_path, total, average):
    # Write the calculation results to a file
    with open(output_path, 'w') as file:
        file.write(f"Sum of numbers: {total}\n")
        file.write(f"Average of numbers: {average}\n")

def main(input_file, output_file):
    numbers = read_data(input_file)
    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    write_results(output_file, total, average)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python data_processing.py <input_file> <output_file>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])