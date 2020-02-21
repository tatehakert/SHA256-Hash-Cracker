#--------------------------------
from urllib.request import urlopen, hashlib, os

#hashes = open("hashes.txt", "r").read()
hashes = open("originalHashList.txt", "r").read()
results = open("results.txt", "a")
counter = 0
guessedHashCounter = 0
guessedHash = ""
guessedHashCap = ""
commonPasswords = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
allWords = commonPasswords

for filename in os.listdir(str(os.getcwd()) + "/allWords"):
    #if filename != "length02.txt" & filename != "length02.txt" & filename != "length03.txt" & filename != "length04.txt" & filename != "length4Capital.txt":
    allWords += open("allWords/" + filename, "r").read()


print("\nchecking single dictionary words\n")
for guess in allWords.split('\n'):
    guess = guess.lower()
    guessedHash = hashlib.sha256(bytes(guess, 'utf-8')).hexdigest()
    guessedHashCap = hashlib.sha256(bytes(guess.capitalize(), 'utf-8')).hexdigest()
    guessedHashAllCap = hashlib.sha256(bytes(guess.upper(), 'utf-8')).hexdigest()

    for hashToCrack in hashes.split('\n'):
        # print("hashToCrack = " + hashToCrack)
        if guessedHash == hashToCrack.rstrip():
            print("hashToCrack: " + hashToCrack)
            print("The password is: " + guess)
            results.write("hashToCrack: " + hashToCrack + " password: " + guess + "  :single dictionary words\n")
            hashes = hashes.replace(str(hashToCrack + '\n'), "")
            guessedHashCounter += 1
        elif guessedHashCap == hashToCrack.rstrip():
            print("hashToCrack: " + hashToCrack)
            print("The password is: " + guess.capitalize())
            results.write( "hashToCrack: " + hashToCrack + " password: " + guess.capitalize() + "  :single dictionary words\n")
            hashes = hashes.replace(str(hashToCrack + '\n'), "")
            guessedHashCounter += 1
        elif guessedHashAllCap == hashToCrack.rstrip():
            print("hashToCrack: " + hashToCrack)
            print("The password is: " + guess.upper())
            results.write("hashToCrack: " + hashToCrack + " password: " + guess.upper() + "  :single dictionary words\n")
            hashes = hashes.replace(str(hashToCrack + '\n'), "")
            guessedHashCounter += 1
    counter += 1

print("finished checking single dictionary words\n")
print("\nchecking numbers 0-999999\n")

for i in range(1000000):
    guessedHash = hashlib.sha256(bytes(str(i), 'utf-8')).hexdigest()
    if i % 100000 == 0:
        print("counter: " + str(counter))

    for hashToCrack in hashes.split('\n'):
        if guessedHash == hashToCrack.rstrip():
            print("hashToCrack: " + hashToCrack)
            print("The password is ", str(i))
            results.write("hashToCrack: " + hashToCrack + "password: " + str(i) + "  :randomNumbers\n")
            hashes = hashes.replace(str(hashToCrack + '\n'), "")
            guessedHashCounter += 1
    counter += 1

print("finished checking numbers 0-999999 \n")


numsAndSym = ['0','1','2','3','4','5','6','7','8','9',
              '!','$','@','#','%','?','&','+']

print("checking words followed by 1 nums/sym\n")
for guess in allWords.split('\n'):
    guess = guess.lower()
    for char1 in numsAndSym:
                guessF = guess + char1
                #print("guessF: " + guessF)
                hashedGuess = hashlib.sha256(bytes(guessF, 'utf-8')).hexdigest()
                hashedGuessCap = hashlib.sha256(bytes(guessF.capitalize(), 'utf-8')).hexdigest()
                for hashToCrack in hashes.split('\n'):
                    if hashedGuess == hashToCrack.rstrip():
                        print("hashToCrack: " + hashToCrack)
                        print("The password is " + guessF)
                        results.write("hashToCrack: " + hashToCrack + " password: " + guessF + "  : words followed by 1 nums/sym \n")
                        hashes = hashes.replace(str(hashToCrack + '\n'), "")
                        guessedHashCounter += 1
                    elif hashedGuessCap == hashToCrack.rstrip():
                        print("hashToCrack: " + hashToCrack)
                        print("The password is " + guessF.capitalize())
                        results.write("hashToCrack: " + hashToCrack + " password: " + guessF.capitalize() + "  : words followed by 1 nums/sym \n")
                        hashes = hashes.replace(str(hashToCrack + '\n'), "")
                        guessedHashCounter += 1
                counter += 1
                if counter % 10000000 == 0:
                    print("counter: " + str(counter) + "  guessedHashCount: " + str(guessedHashCounter))
                    print("guessF: " + guessF)

print("\nfinished checking words followed by 1 nums/sym\n")

print("checking words followed by 2 nums/sym\n")
for guess in allWords.split('\n'):
    guess = guess.lower()
    for char1 in numsAndSym:
        first = char1
        for char2 in numsAndSym:
                first2 = first + char2
                guessF = guess + first2
                #print("guessF: " + guessF)
                hashedGuess = hashlib.sha256(bytes(guessF, 'utf-8')).hexdigest()
                hashedGuessCap = hashlib.sha256(bytes(guessF.capitalize(), 'utf-8')).hexdigest()
                for hashToCrack in hashes.split('\n'):
                    if hashedGuess == hashToCrack.rstrip():
                        print("hashToCrack: " + hashToCrack)
                        print("The password is " + guessF)
                        results.write("hashToCrack: " + hashToCrack + " password: " + guessF + "  : numsAfterDicWords.py \n")
                        hashes = hashes.replace(str(hashToCrack + '\n'), "")
                        guessedHashCounter += 1
                    elif hashedGuessCap == hashToCrack.rstrip():
                        print("hashToCrack: " + hashToCrack)
                        print("The password is " + guessF.capitalize())
                        results.write("hashToCrack: " + hashToCrack + " password: " + guessF.capitalize() + "  : numsAfterDicWords.py \n")
                        hashes = hashes.replace(str(hashToCrack + '\n'), "")
                        guessedHashCounter += 1
                counter += 1
                if counter % 10000000 == 0:
                    print("counter: " + str(counter) + "  guessedHashCount: " + str(guessedHashCounter))
                    print("guessF: " + guessF)
print("\nfinished checking words followed by 2 nums/sym\n")

print("checking words followed by 3 nums/sym\n")
for guess in allWords.split('\n'):
    guess = guess.lower()
    for char1 in numsAndSym:
        first = char1
        for char2 in numsAndSym:
            first2 = first + char2
            for char3 in numsAndSym:
                first3 = first2 + char3
                guessF = guess + first3
                #print("guessF: " + guessF)
                hashedGuess = hashlib.sha256(bytes(guessF, 'utf-8')).hexdigest()
                hashedGuessCap = hashlib.sha256(bytes(guessF.capitalize(), 'utf-8')).hexdigest()
                for hashToCrack in hashes.split('\n'):
                    if hashedGuess == hashToCrack.rstrip():
                        print("hashToCrack: " + hashToCrack)
                        print("The password is " + guessF)
                        results.write("hashToCrack: " + hashToCrack + " password: " + guessF + "  : numsAfterDicWords.py \n")
                        hashes = hashes.replace(str(hashToCrack + '\n'), "")
                        guessedHashCounter += 1
                    elif hashedGuessCap == hashToCrack.rstrip():
                        print("hashToCrack: " + hashToCrack)
                        print("The password is " + guessF.capitalize())
                        results.write("hashToCrack: " + hashToCrack + " password: " + guessF.capitalize() + "  : numsAfterDicWords.py \n")
                        hashes = hashes.replace(str(hashToCrack + '\n'), "")
                        guessedHashCounter += 1
                counter += 1
                if counter % 10000000 == 0:
                    print("counter: " + str(counter) + "  guessedHashCount: " + str(guessedHashCounter))
                    print("guessF: " + guessF)
print("\nfinished checking words followed by 3 nums/sym\n")

print("checking dictionary word pairs\n")

for guess in commonPasswords.split('\n'):
    guess = guess.lower()
    for guess2 in commonPasswords.split('\n'):
        guess2 = guess2.lower()
        guessedHash     = hashlib.sha256(bytes(guess + guess2, 'utf-8')).hexdigest()
        guessedHashCap  = hashlib.sha256(bytes(guess.capitalize() + guess2.capitalize(), 'utf-8')).hexdigest()
        if counter % 1000000 == 0:
            print("counter: " + str(counter) + "  guessedHashCount: " + str(guessedHashCounter))
            #print("guess: " + guess + guess2)
            #print("guessCap: " + guess.capitalize() + guess2.capitalize())

        for hashToCrack in hashes.split('\n'):
            #print("hashToCrack = " + hashToCrack)
            if guessedHash == hashToCrack.rstrip():
                print("hashToCrack: " + hashToCrack)
                print("The password is: " + guess + guess2)
                results.write("hashToCrack: " + hashToCrack + " password: " + guess + guess2 + "  :dictionaryWordPairs\n")
                hashes = hashes.replace(str(hashToCrack + '\n'),"")
                guessedHashCounter += 1
            elif guessedHashCap == hashToCrack.rstrip():
                print("hashToCrack: " + hashToCrack)
                print("The password is: " + guess.capitalize() + guess2.capitalize())
                results.write("hashToCrack: " + hashToCrack + " password: " + guess.capitalize() + guess2.capitalize() + "  :dictionaryWordPairs\n")
                hashes = hashes.replace(str(hashToCrack + '\n'), "")
                guessedHashCounter += 1
        counter += 1


quit()
#---------------------------------


