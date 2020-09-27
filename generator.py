import sys
import string

# used to get the website name and return it
def get_website_name():
    website_name = input("What website are you creating a password for? ")
    return website_name

#used to get the base phrase for the password and return it
def get_base_phrase():
    base_phrase = input('''Pick a word or phrase that your password will be based on (do not include spaces or special characters): ''')
    return base_phrase


def get_first_three_letters(string):
    print(string[0:3])


def generate_password():
    print("function")


def main():
    website = get_website_name()
    phrase = get_base_phrase()

    while not phrase.isalpha():
        phrase = get_base_phrase()
    
    get_first_three_letters(website)
    

    



if __name__ == "__main__":
    main()