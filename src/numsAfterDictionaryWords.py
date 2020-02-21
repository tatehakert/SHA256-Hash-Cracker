#--------------------------------
from urllib.request import urlopen, hashlib, os

hashes = open("hashes.txt", "r").read()
results = open("results.txt", "a")
counter = 0
numString = ""
allWords = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

numsAndSym = ['0','1','2','3','4','5','6','7','8','9',
              '!','$','@','#','%','?','&','+']
guessF = ""
first = ""
first2 = ""
first3 = ""

for filename in os.listdir(str(os.getcwd()) + "/allWords"):
    allWords += open("allWords/" + filename, "r").read()

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
                    elif hashedGuessCap == hashToCrack.rstrip():
                        print("hashToCrack: " + hashToCrack)
                        print("The password is " + guessF.capitalize())
                        results.write("hashToCrack: " + hashToCrack + " password: " + guessF.capitalize() + "  : numsAfterDicWords.py \n")
                        hashes = hashes.replace(str(hashToCrack + '\n'), "")
                counter += 1
                if counter % 10000000 == 0:
                    print("counter: " + str(counter))
                    print("guessF: " + guessF)

quit()



#------------------------