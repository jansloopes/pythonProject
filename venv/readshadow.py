# program to read shadow file and to check password with salt sha256.
# normally this program needs to run with root privileges.
#jfh 24092020
#
import crypt


def read_shadow(sh_file: str) -> dict:
    dict_shadow: dict = {}
    try:
        with open(sh_file, "r") as f:
            for line in f:
                s = line.strip().split(":")
                # print (s)
                dict_shadow[s[0]] = (s[1])
        f.close()
        return dict_shadow

    except IOError:
        print("Could not open {}".format(sh_file))
        return dict_shadow


def login_salt(dict_shadow: dict, unknown_usr: str) -> str:
    salt_usr: str = input("Geef je usernaam: ")
    print("username is: {} ".format(salt_usr))
    # print(crypt.crypt(salt_pwd, salt_string))
    if salt_usr in dict_shadow:
        return salt_usr
    else:
        return unknown_usr


def check_pwd(salted_pwd_str: str, salt_pwd) ->int:
    salt_shadow: str = salted_pwd_str[0:20]
    pwd_salted_shadow: str = salted_pwd_str[26:]
    pwd_salted_calc = crypt.crypt(salt_pwd, salt_shadow)
    print("userpwd: {}\n  pw_salted: {} \n salt_shadow is: {} \n pwd_salted_calculated is: {}".format(salt_pwd,
                                                                                                      pwd_salted_shadow,
                                                                                                      salt_shadow,
                                                                                                      pwd_salted_calc))
    if salted_pwd_str == pwd_salted_calc:
        return 1
    else:
        return 0


def main():
    sh_file: str = '/home/jan/Documents/shadow'
    dict_shadow: dict = {}
    unknown_usr: str = "unknown"

    dict_shadow = read_shadow(sh_file)
    salt_usr: str = login_salt(dict_shadow, unknown_usr)
    #  print("print dictionary", dict_shadow)
    print("user is ", salt_usr)
    if salt_usr != unknown_usr:
        salt_pwd: str = input("geef pwd: ")
        if check_pwd(dict_shadow[salt_usr], salt_pwd):
            print("password {} is gelijk aan opgeslagen password.".format(salt_pwd))
        else:
            print ("password {} is niet gelijk aan opgeslagen password.".format(salt_pwd))

# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()
