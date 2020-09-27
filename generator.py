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
    first_three_letters = string[0:3]
    return first_three_letters



def generate_password():
    print("function")


def main():
    #get the website name from user
    website = get_website_name()
    
    #Check if it is valid and keep looping until they provide a valid name
    while not website.isalpha() and website.lenth() > 3:
        website = get_website_name()

    phrase = get_base_phrase()
    password = ""

    while not phrase.isalpha():
        phrase = get_base_phrase()
    
    letters = get_first_three_letters(website).capitalize()

    password = letters + "!" + phrase.lower() +

    



if __name__ == "__main__":
    main()