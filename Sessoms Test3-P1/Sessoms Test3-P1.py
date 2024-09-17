'''
Sessoms Test3-P1
Carson Sessoms
sessomsc@usca.edu
Test #3
ask the user to enter a string and tells them how many words, vowels, and consonants it has
4/12/2023
'''
def count_vowels(user_string):
    vowels = "aeiouAEIOU"
    i = 0
    for char in user_string:
        if char in vowels or char.endswith("y"):
            i = i + 1
    return i
def count_consonants(user_string):
    vowels = "aeiouAEIOU"
    i = 0
    for char in user_string:
        if char not in vowels and char.isalpha():
            i = i + 1
    return i
def count_words(user_string):
    split_string = user_string.split()
    words = len(split_string)
    return words        
def main():
    while True:
        user_string = input("Enter a string or EXIT to quit: ")
        user_string = user_string.strip()
        print()
        if user_string == "EXIT":
            break
        elif any(i.isdigit() for i in user_string):
            print("Please enter a valid input and try again.")
            print()
        else:
            try:
                num_vowels = count_vowels(user_string)
                num_consonants = count_consonants(user_string)
                num_words = count_words(user_string)
                print("The string you entered includes ", num_vowels, " vowels.")
                print("The string you entered includes ", num_consonants, " consonants.")
                print("The string you entered includes ", num_words, " words.")
                print()
            except:
                print("Please enter a valid input and try again.")
                print()
if __name__ == "__main__":
    main()
            
        
