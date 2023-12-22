import hashlib


def find_lowest_number(secret_key):
    number = 1
    while True:
        # Combine the secret key and the current number
        input_string = f"{secret_key}{number}"

        # Calculate the MD5 hash
        md5_hash = hashlib.md5(input_string.encode()).hexdigest()

        # Check if the hash has at least five leading zeroes
        if md5_hash[:5] == "00000":
            return number

        # Increment the number for the next iteration
        number += 1


ans = find_lowest_number("iwrupvqb")

print(ans)


def find_lowest_number_six(secret_key, num_zeroes):
    number = 1
    target_prefix = "0" * num_zeroes
    while True:
        # Combine the secret key and the current number
        input_string = f"{secret_key}{number}"

        # Calculate the MD5 hash
        md5_hash = hashlib.md5(input_string.encode()).hexdigest()

        # Check if the hash has the desired number of leading zeroes
        if md5_hash[:num_zeroes] == target_prefix:
            return number

        # Increment the number for the next iteration
        number += 1


ans2 = find_lowest_number_six("iwrupvqb", 6)

print(ans2)
     