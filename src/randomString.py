from urllib.request import hashlib, os

hashes = open("hashes.txt", "r").read()
results = open("results.txt", "a")
counter = 0
first2 = ""
first3 = ""
first4 = ""
first5 = ""
charString = ""
chars = ['a','b','c','d','e','f','g','h','i','j',
         'k','l','m','n','o','p','q','r','s','t',
         'u','v','w','x','y','z','0','1','2','3',
         '4','5','6','7','8','9','!','$','@','#',
         '%', '/', '.', '?', '&']

charsOnly = ['a','b','c','d','e','f','g','h','i','j',
             'k','l','m','n','o','p','q','r','s','t',
             'u','v','w','x','y','z']

numsOnly = ['0','1','2','3','4','5','6','7','8','9']

numsAndSym = ['0','1','2','3','4','5','6','7','8','9',
              '!','$','@','#','%','?','&','+']

chars9toAnd = ['9','!', '$', '@', '#', '%', '/', '.', '?', '&']
guessedHash = ""

for i in range(1000000):
    guessedHash = hashlib.sha256(bytes(str(i), 'utf-8')).hexdigest()
    if i % 100000 == 0:
        print("counter: " + str(counter))

    for hashToCrack in hashes.split('\n'):
        if guessedHash == hashToCrack.rstrip():
            print("hashToCrack: " + hashToCrack)
            print("The password is ", str(i))
            results.write("hashToCrack: " + hashToCrack + "password: " + str(i) + "  :randomString.py\n")
            hashes = hashes.replace(str(hashToCrack + '\n'), "")
    counter += 1

print("finished checking numbers 0-999999 \n")

for char1 in charsOnly:
    print("counter:" + str(counter))
    print("-----------------char1: " + char1)
    for char2 in charsOnly:
        print("counter:" + str(counter))
        print("----char2: " + char2)
        first2 = char1 + char2
        for char3 in charsOnly:
            #print("counter:" + str(counter))
            #print("char3: " + char3)
            first3 = first2 + char3
            for char4 in charsOnly:
                first4 = first3 + char4
                for char5 in numsAndSym:
                    first5 = first4 + char5
                    for char6 in numsAndSym:
                        charString = first5 + char6
                        guessedHash = hashlib.sha256(bytes(charString, 'utf-8')).hexdigest()

                        for hashToCrack in hashes.split('\n'):

                            if guessedHash == hashToCrack.rstrip():
                                print("hashToCrack: " + hashToCrack)
                                print("The password is ", charString)
                                results.write("hashToCrack: " + hashToCrack + "password: " + charString + "\n")
                        counter += 1