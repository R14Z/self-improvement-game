one = 1000

level = 0

# things that you need to get more exp

# exercise 

exercise = input('Have you done any exercise today (Y,N) ').upper()

if exercise == 'Y':
    # the amount of exercise
    pushups_fifty = 50
    pushups_eighty = 100
    pushups_hundred = 150
    weights = 150

    # exercise node
    exercise_q = input('Have you done push-ups or weights? (P,W,B) ').upper()
    if exercise_q == 'P':
        pushup_q = int((input('How many have you done? (50, 80, 100) ')))
        if pushup_q == 50:
            level = level + pushups_fifty
        elif pushup_q == 80:
            level = level + pushups_eighty
        elif pushup_q == 150:
            level = level + pushups_hundred
        else:
            print('Bye!')
    if exercise_q == 'W':
        level = level + weights
    if exercise_q == 'B':
        print('Damn, good job. You earned a 2x bonus.')
        level = level + 300
else:
    print('Do it. Now. I thought you wanted to be the strongest in your bloodline. No? ')

# meditating

meditating = 100 

meditating_q = input('Have you meditated today? (Y,N) ')
if meditating_q == 'Y':
    print('Good job, you have earned 100xp.')
    level = level + 100
else:
    print('Okay, do it.')

# social media

social = 100

social_q = input('Have you used social media for less than 50 minutes today? (Y,N) ')
if social_q == 'Y':
    print('Good job. Nice little dopamine detox. ')
    level = level + social
else:
    print('Better luck next time.')

# nature 

nature = 200

nature_q = input('Have you explored nature today? (Y,N) ')
if nature_q == 'Y':
    print('Good job.')
    level = level + nature
else:
    print("It's always good to explore nature, maybe next time.")


# journalizing

journalize = 50
journalize_phone = 70

journalize_q = input('Have you journalized today? (Y,N) ')
if journalize_q == 'Y':
    device = input('Have you journalized on a phone or another device? (P,O) ')
    if device == 'P':
        print('Nice! You earned a 20xp bonus for journalizing on phone.')
        level = level + journalize_phone
    else:
        print('Good job. You earned 50xp. ')
        level = level + journalize_phone

# clean

clean = 80

clean_q = input('Have you cleaned anything? (Y,N) ')
if clean_q == 'Y':
    print('Nice, helping out your parents.')
    level = level + clean
else:
    print('Do it next time. NEXT TIME.')

# study

study_30 = 50 
study_1 = 150

# programming has the same values as studying 
programming_30 = study_30
programming_1 = study_1 

# water
water_1point5L = 30
water_2L = 50

# books
book_10 = 100 
book_15 = 150

# muay thai (or self-defense learning)
muay_thai = 100

# learn something new, thats helpful 
learning = 50

# pray 
question_Fajr = input('Have you prayed Fajr? (Y,N) ').upper()
if question_Fajr == 'Y':
    question_Zuhr = input('Good job, have you prayed Zuhr? ').upper()
    if question_Zuhr == 'Y':
        question_Asr = input('Asr? ').upper()
        if question_Asr == 'Y':
            question_Maghrib_Isha = input('Have you prayed Maghrib and Isha? ')
            if question_Maghrib_Isha == 'Y':
                print('Good job, you prayed the whole day! ')
            elif question_Zuhr or question_Asr or question_Maghrib_Isha == 'N':
                print("Go pray, or you'll lose points. ")    
else:
    print('Go pray.')    

# cold shower
cold_shower = 100 

# ** negative points ** 
fap = -500 
not_praying = -600

# counter
counter = int(input("Add how many points that you've got "))

print(f'You have got {counter} amount of points.')
