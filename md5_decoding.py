import itertools
import hashlib
import threading

def generate_passwords():
    words = "0123456789abcdefghijklmnopqrstuvwxyz" # a set of password characters
    passwords = itertools.product (words, repeat=4) # random combination of 5 characters
    return passwords


def calculate_md5(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def copy_to_regular_list(itertools_list):
    new_list = []
    for item in itertools_list:
        new_list.append("".join(item))
    return new_list

def decode_md5(hashed_password, possible_passwords):
    for password_tuple in possible_passwords:
        password = "".join(password_tuple)  # Convert the tuple to a string
        print("Trying: {}".format(password))
        if calculate_md5(password) == hashed_password:
            print("The password is: {}".format(password))
            return password
    print("Password not found!")
    return None


if __name__ == "__main__":
    hashed_password = "0008669ec4a7163e773d978beef25f3a"
    possible_passwords = generate_passwords()
    possible_passwords = copy_to_regular_list(possible_passwords)

    middle_index = int(len(possible_passwords) / 2)
    start_to_middle = possible_passwords[:middle_index]
    middle_to_end = possible_passwords[middle_index + 1:]

    t1 = threading.Thread(target=decode_md5, args=(hashed_password, start_to_middle))
    t2 = threading.Thread(target=decode_md5, args=(hashed_password, middle_to_end))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Done")