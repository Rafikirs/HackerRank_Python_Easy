def print_formatted(number):
    width = len(bin(number)) - 2  # Width based on the binary length of the number

    for i in range(1, number + 1):
        # Using string formatting to ensure proper alignment and width
        print(f"{i:>{width}} {oct(i)[2:]:>{width}} {hex(i)[2:].upper():>{width}} {bin(i)[2:]:>{width}}")
