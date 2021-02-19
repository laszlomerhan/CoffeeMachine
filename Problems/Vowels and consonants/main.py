vow = 'aeiou'
user_input = input()

for i in user_input:
    if i in vow:
        print('vowel')
    elif not i.isalpha():
        break
    else:
        print('consonant')
