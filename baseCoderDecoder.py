import os
import base64


class bColors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'


def banner():
    print(bColors.GREEN + '<<< IP-TRACKER v1.0>>>')
    print(bColors.RED + r'''
  _
 | |
 | |___
 |  _  \   _   _
 | |_)  | | (_) |
  \____/   \__, |
            __/ |
           |___/
                                        _                                                         _
                                       | |                                                       (_)
                  ____     ____     ___| |   ___ _   ______   ______    ___ _   ______   ______   _   _ ____
                 / ___\   /    \   /  _  |  / _ | | / _____| / _____|  / _ | | / _____| / _____| | | | |   | \
                | |____  |  ()  | |  (_| | | (_|| | \______\ \______\ | (_|| | \______\ \______\ | | | |   | |
                 \____/   \____/   \____/   \___|_| |______/ |______/  \___|_| |______/ |______/ |_| |_|   |_|
     ''')


default = True
depth = 30
level_of_encryption = 11


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def base85decode(n):
    level = 1
    user_decoded = n
    for i in range(0, depth):
        user_decoded = base64.b85decode(user_decoded)
        print(f"Decoded {level} times: '{user_decoded.decode()}' ")
        level += 1


def base16decode(n):
    level = 1
    user_decoded = n
    for i in range(0, depth):
        user_decoded = base64.b16decode(user_decoded)
        print(f"Decoded {level} times: '{user_decoded.decode()}' ")
        level += 1


def base32decode(n):
    level = 1
    user_decoded = n
    for i in range(0, depth):
        user_decoded = base64.b32decode(user_decoded)
        print(f"Decoded {level} times: '{user_decoded.decode()}' ")
        level += 1


def base64encode(n):
    level = 1
    user_encoded = n
    for i in range(0, level_of_encryption):
        user_encoded = base64.b64encode(user_encoded)
        print(f"Encoded {level} times: '{user_encoded.decode()}'")
        level += 1


def base64decode(n):
    level = 1
    user_decoded = n
    for i in range(0, depth):
        user_decoded = base64.b64decode(user_decoded)
        print(f"Decoded {level} times: '{user_decoded.decode()}' ")
        level += 1


def b85(user):
    try:
        base85decode(user)
    except Exception as e:
        print("Gone through b85")

    input("\npress enter to continue ")
    clear()
    main()


def b16(user):
    try:
        base16decode(user)
    except Exception as e:
        print("Gone through b16")

    input("\npress enter to continue")
    clear()
    main()


def b32(user):
    try:
        base32decode(user)
    except Exception as e:
        print("Gone through b32")

    input("\npress enter to continue")
    clear()
    main()


def b64(user):
    action = input("Choose [e]ncode or [d]ecode: ")
    if action == "e":
        try:
            base64encode(bytes(user, 'utf-8'))
        except Exception as e:
            pass
    try:
        base64decode(user)
    except Exception as e:
        print("Gone through b64")

    input("\npress enter to continue  ")
    clear()
    main()


def tryall(user):
    try:
        print("\nb64 decoded:")
        base64decode(user)
    except Exception as e:
        pass
    try:
        print("\nb32 decoded:")
        base32decode(user)
    except Exception as e:
        pass
    try:
        print("\nb16 decoded:")
        base16decode(user)
    except Exception as e:
        pass
    try:
        print("\nb85 decoded:")
        base85decode(user)
    except Exception as e:
        pass

    input("\npress enter to continue: ")
    clear()
    main()


def main():
    print(bColors.GREEN + "ENCODING ONLY ON B64")
    formats = ["b64", "b32", "b16", "b85", "all", ]
    user = input(bColors.BLUE + "Choose base 'b64', 'b32', 'b16', 'b85' or 'all': ")
    if user not in formats:
        print(bColors.RED + "invalid input!")
        main()

    string = input("Paste your string: ")
    if user == "b64":
        b64(string)
    if user == "b32":
        b32(string)
    if user == "b16":
        b16(string)
    if user == "b85":
        b85(string)
    if user == "all":
        tryall(string)


if default:
    banner()
    try:
        clear()
        main()
    except KeyboardInterrupt:
        clear()
        print("KEYBOARD INTERRUPT")
