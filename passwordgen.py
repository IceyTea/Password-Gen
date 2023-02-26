import random


uppercaseletter1 = chr(random.randint(65,90))
uppercaseletter2 = chr(random.randint(65,90))
lowercaseletter1 = chr(random.randint(97,122))
lowercaseletter2 = chr(random.randint(97,122))
digit1 = str(random.randint(0,9))
digit2 = str(random.randint(0,9))

punctuation_list = [33, 35, 36, 37, 38, 60, 62, 64]
random.shuffle(punctuation_list)
punk1 = chr(punctuation_list[0])
punk2 = chr(punctuation_list[1])   

password = uppercaseletter1 + uppercaseletter2 + lowercaseletter1 + lowercaseletter2 + digit1 + digit2 + punk1 + punk2
truepassword = list(password)
random.shuffle(truepassword)

print(''.join(truepassword))



