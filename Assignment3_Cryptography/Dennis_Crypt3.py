import random
import re
import crypto_utils
import crypto_utils as cu
from math import gcd


class Cipher():
#hver cipherklasse bør inneholde en liste med mulige nøkkler for den gitte cipheren (unntatt rsa
#funksjon som henter mulige nøkler
#hackerklassen vet hvilken cipher du skal ha, kan skrive for key in cipher.getkeysklassen som er gitt
#prøver i denne forløkka å decode. cipher.decode med den gitte keyen
#har en counter som teller opp
#matcher så med english_wordslist og for hver "match" så økes counter med 1 og
#den som har bestcount = det som er ordet som matcher
#for unbreakable må så må den være større enn 0

    def __init__(self):
        self.alphabet = [chr(i) for i in range(32, 127)]        #definerer ascii alfabetet vi skal bruke, mellomrommet til del, [32, 126]
        self.alphabetSize = len(self.alphabet)

    def encode(self, message, key):    #message to encrypt
        pass                            #pass = nulloperation

    def decode(self, message, key):  #message to decrypt
        pass

    #får klar-tekst inn, koder klar-teksten, dekoder cipher-teksten, og verifiserer at den dekodede teksten er identisk med den initielle klar-teksten.
    def verify(self, encodedText, decodedText):
        return decodedText == self.decode(encodedText) and encodedText == self.encode(decodedText)

    def generate_keys(self):
        pass


class Person():

#instans av dette skal ha tilgang til nøkkel og cipheralgoritme
    def __init__(self, key, cipher):
        self.key = key
        self.cipher = cipher

    def set_key(self, key):         #standar setter og gettere
        self.key = key

    def get_key(self):
        return self.key

    def operate_cipher(self):
        None

#senderen genererer cipher-tekst, og mottakeren genererer klar-tekst.
class Sender(Person):

    def __init__(self, key, cipher):
        super().__init__(key, cipher)

    def operate_cipher(self, message):
        self.encodedText = self.cipher.encode(message, self.key)
        return self.encodedText

    def send_cipher(self, receiver, text):

        if isinstance(self.cipher, RSA):    #Return true if the object argument is an instance of the classinfo argument
            receiver.generate_keys()
            self.key = receiver.senderKey

        receiver.receiveCipher(self.operate_cipher(text))

    def test_print(self):
        return self.encodedText

class Receiver(Person):

    def __init__(self, key, cipher):
        super().__init__(key, cipher)

    def operate_cipher(self, message):
        self.encodedText = message
        self.decodedText = self.cipher.decode(message, self.key)
        return self.decodedText

    def receiveCipher(self, message):
        self.operate_cipher(message)

    def senderKey(self):
        return self.senderKey

    def generate_keys(self):
        firstPrime = crypto_utils.generate_random_prime(8)
        secondPrime = firstPrime
        _gcd = 0

        while firstPrime == secondPrime or _gcd != 1:
            firstPrime = crypto_utils.generate_random_prime(8)
            secondPrime = crypto_utils.generate_random_prime(8)
            phi = (firstPrime - 1) * (secondPrime - 1)
            e = random.randint(3, phi - 1)
            _gcd = gcd(e, phi)


        n = firstPrime * secondPrime
        d = crypto_utils.modular_inverse(e, phi)

        self.senderKey = (n, e)

        self.key = (n, d)

    def testPrint(self):
        return self.decodedText




class Hacker(Receiver):
    #"postpone"
    """words = []
    limit = None

    def __init__(self):
        super().__init__()
        word_list = open("english_words.txt", "r")  #åpner opp og leser
        word = word_list.readline()                 #definererer ordene for hver linje
        while word:
            self.words.append(word.split("\n")[0])  #legger alt inn i liste som splittes ved hvert linjeshift
            word = word_list.readline()
        word_list.close()

        self.limit = self.cipher.size

    def operate_cipher(self, s):
        pass


    #uferdig
    def hack(self, s):
        best_match = [None, 0, None, None]

        if isinstance(self.cipher, Affine): #Return true if the object argument is an instance of the classinfo argumen
            for i in range(0, self.limit):
                for j in range(0, self.limit):
                    decode = self.cipher.decode(s, i, j)
                    decoded_words = decode.split(" ")
                    match = 0
                    for word in decoded_words:
                        if word in self.words and len(word) > 0:
                            match += 1
                    if match > best_match[1]:
                        best_match = (decode, match, i, j)
                    if best_match[1] == len(decoded_words):  # hvis oversettelsen er perfekt
                        return best_match
            return best_match

        elif isinstance(self.cipher, Unbreakable):
            for i in self.words:
                print(i)
                decode = self.cipher.decode(s, i, 0)
                decoded_words = decode.split(" ")
                match = 0
                for word in decoded_words:
                    if word in self.words and len(word) > 0:
                        match += 1
                if match > best_match[1]:
                    best_match = (decode, match, i)
                    print(best_match)
                if best_match[1] == len(decoded_words):  # hvis oversettelsen er perfekt
                    return best_match
            return best_match

        else:
            for i in range(0, self.limit):  # Denne bruker laaaaang tid
                decode = self.cipher.decode(s, i, 0)
                decoded_words = decode.split(" ")
                match = 0
                for word in decoded_words:
                    if word in self.words and len(word) > 0:
                        match += 1
                if match > best_match[1]:
                    best_match = (decode, match, i)
                if best_match[1] == len(decoded_words):  # hvis oversettelsen er perfekt
                    return best_match
            return best_match"""

class Hacker(Receiver):

    def __init__(self):
        self.ckey = [x for x in range(0,95)]
        self.mkey = []
        for x in range(0,95):
            if cu.modular_inverse(x,95)!= 1:
                self.mkey.append(x)
        file = open("english_words.txt", 'r')
        self.words = file.readlines()
        self.words = [x.strip() for x in self.words]

    def crack(self, message, cipherType = None):
        possibleMessages = []
        if not cipherType or type(cipherType) == type(Caesar()):
            self.set_cipher(Caesar(0))
            for key in self.ckey:
                self.cipher.set_key(key)
                self.decode(message,possibleMessages)

        if not cipherType or type(cipherType) == type(Multiplicative()):
            self.set_cipher(Multiplicative(0))
            for key in self.mkey:
                self.cipher.set_key(key)
                self.decode(message,possibleMessages)

        if not cipherType or type(cipherType) == type(Affine()):
            self.set_cipher(Affine([0,0]))
            for key in self.ckey:
                for key2 in self.mkey:
                    self.cipher.set_key([key2,key])
                    if self.decode(message,possibleMessages):
                        print(possibleMessages)

        if not cipherType or type(cipherType) == type(Unbreakable()):
            self.set_cipher(Ucipher(''))
            for key in self.words:
                self.cipher.set_key(key)
                if self.decode(message, possibleMessages):
                    print(possibleMessages)
                    print(key)

        if not possibleMessages:
            print("no correct message found for", message)
        else:
            print("possible messages for",message,'->', possibleMessages)

    def decode(self,message,possibleMessages):
        decoded = self.operate_cipher(message)
        # split decoded into words
        # \w -> only alphanumeric
        # \S -> only non-whitespace
        wordList = re.sub("[^\S]", " ", decoded).split()
        wordList = [x.lower() for x in wordList]
        if not wordList:
            return False
        allwordsright = True
        for word in wordList:
            if not self.verify(word):
                allwordsright = False
                break
                #possibleMessages.append(wordList)
        if allwordsright and decoded not in possibleMessages:
            possibleMessages.append(decoded)
        return allwordsright

    def verify(self,message):
        for word in self.words:
            if word == message:
                return True
        return False







class Caesar(Cipher):

    def __init__(self):
        super().__init__()

    def encode(self, message, key):            #encryptmelding
        self.encoded = ""
        for i in range(len(message)):
            letter = (self.alphabet.index(message[i]) + key) % self.alphabetSize
            self.encoded += self.alphabet[letter]
        return self.encoded

    def decode(self, toDecipher, key):         #decryptmelding
        self.decoded = ""
        for i in range(len(toDecipher)):
            letter = (self.alphabet.index(toDecipher[i]) + (self.alphabetSize - key)) % self.alphabetSize
            self.decoded += self.alphabet[letter]
        return self.decoded

    def generate_keys(self, whoseKey):          #hvilken key som brukes
        keys = [self.key, self.alphabetSize - self.key]
        return keys[whoseKey]


class Multiplication(Cipher):                   #erstatter addisjon med multiplikasjon istedet

    def __init__(self):
        super().__init__()

    def encode(self, message, key):            #melding som skal krypteres

        self.encoded = ""

        for i in range(len(message)):
            letter = self.alphabet.index(message[i])
            letter *= key
            letter %= self.alphabetSize
            self.encoded += self.alphabet[letter]

        return self.encoded

    def decode(self, message, key):            #melding dekrypt

        self.decoded = ""
        self.newKey = crypto_utils.modular_inverse(key, self.alphabetSize)  #beskrivelse i cryptoutils

        for i in range(len(message)):
            index = self.alphabet.index(message[i])
            self.decoded += self.alphabet[(index * self.newKey) % self.alphabetSize]

        return self.decoded

    def generate_keys(self, key):
        return crypto_utils.modular_inverse(key, self.alphabetSize)


class Affine(Cipher):                           #kombinasjon av mult og caesar, bruker tuppel av to heltall som nøkkel

    def __init__(self):
        super().__init__()

    def encode(self, message, key):

        mult = Multiplication()
        multEncoded = mult.encode(message, key[0])

        caesar = Caesar()
        caesarEncoded = caesar.encode(multEncoded, key[1])

        return caesarEncoded

    #viktig å gjøre operasjonene i motsatt rekkefølge når decoder her
    def decode(self, message, key):

        caesar = Caesar()
        caesarDecoded = caesar.decode(message, key[1])       ##kaller metoden i caesar cipher as usual..

        mult = Multiplication()
        multDecoded = mult.decode(caesarDecoded, key[0])   ##bruker de to heltallene som nøkkel, n=(n1,n2)


        return multDecoded


class Unbreakable(Cipher):          #bruker nøkkelord som key

    def __init__(self):
        super().__init__()

    def encode(self, message, keyWord):
        keyWordCounter = len(keyWord)
        currentKeyWordCount = 0
        encoded = ""

        for i in range(len(message)):
            encodingKey = self.alphabet.index(keyWord[currentKeyWordCount])
            currentKeyWordCount += 1
            currentKeyWordCount %= keyWordCounter
            letter = (self.alphabet.index(message[i]) + encodingKey) % self.alphabetSize
            encoded += self.alphabet[letter]
        return encoded

    #For å dekryptere koden trenger vi et annet kode-ord som “matcher” det vi brukte for ˚a lage ciphertekst. Kodeordet genereres ved at vi posisjon for posisjon bytter symbolet som står der med et annet
    def decode(self, message, keyWord):
        newKeyWord = self.getDecodingKey()
        keyWordCounter = len(newKeyWord)            #analyserer lengden til nøkkelord
        currentKeyWordCount = 0
        decoded = ""                              #definerer dekodea som tom streng i starten

        for i in range(len(message)):
            encodingKey = self.alphabet.index(newKeyWord[currentKeyWordCount])
            currentKeyWordCount += 1
            currentKeyWordCount %= keyWordCounter
            letter = (self.alphabet.index(message[i]) + encodingKey) % self.alphabetSize
            decoded += self.alphabet[letter]              ##legger til bokstav i den tomme strengen
        return decoded


    def decode(self, message, keyWord):
        decodingKeyword = ""

        for i in range(len(keyWord)):
            if len(keyWord) == 0:
                continue
            else:
                index = self.alphabet.index(keyWord[i])
                decodingKeyword += self.alphabet[(self.alphabetSize - index) % self.alphabetSize]

        return self.encode(message, decodingKeyword)


class RSA(Cipher):      #offentliggjøring av nøkkel, nphardt å cracke
    #bruker modularinverse i reiver

    def __init__(self):
        super().__init__()

    def encode(self, message, key):
        n, publicKey = key
        blocks = crypto_utils.blocks_from_text(message, 2)

        return [pow(block, publicKey, n) for block in blocks]

    def decode(self, message, key):
        decodedNumbs = [pow(int(t), int(key[1]), int(key[0])) for t in message]

        decodedText = crypto_utils.text_from_blocks(decodedNumbs, 2)

        return decodedText



def main():
    caesar = Caesar()
    mult = Multiplication()
    affine = Affine()
    unbreakable = Unbreakable()
    rsa = RSA()
#    hacker = Hacker()
    testTekst = input("message to crypt: " + "\n")


    #CAESARSTART
    ## testmottaker og sender til Caesar
    print("\n" + "Caesar-Cipher: \n")
    caesarSender = Sender(2, caesar)
    caesarReceiver = Receiver(2, caesar)
    # Sender til receiver og tester printen fra sender og receiver.
    caesarSender.send_cipher(caesarReceiver, testTekst)
    print("message crypted: " + caesarSender.test_print())
    print("message decrypted: " + caesarReceiver.testPrint())
    #CAESARSLUTT

#    hack.hack(Caesar)

    #MULTIPLICATIONSTART
    print("\n\nMultiplication:\n")
    #testmottaker og sender til Multiplication
    multSender = Sender(3, mult)
    multReceiver = Receiver(3, mult)

    multSender.send_cipher(multReceiver, testTekst)
    print("message crypted: " + multSender.test_print())
    print("message decrypted: " + multReceiver.testPrint())
    #MULTIPLICATIONSLUTT


    #AFFINESTART
    print("\n\nAffine-Cipher: \n")
    #Lager testmottaker og sender til Affine
    affineSender = Sender((2, 3), affine)
    affineReceiver = Receiver((2, 3), affine)

    affineSender.send_cipher(affineReceiver, testTekst)
    print("message crypted: " + affineSender.test_print())
    print("message decrypted: " + affineReceiver.testPrint())
    #AFFINESLUTT


    #UNBREAKABLESTART
    print("\n\nUnbreakable:\n")
    unbreakableSender = Sender("Shablonger", unbreakable)
    unbreakableReceiver = Receiver("Shablonger", unbreakable)

    unbreakableSender.send_cipher(unbreakableReceiver, testTekst)

    print("message crypted: " + unbreakableSender.test_print())
    print("message decrypted: " + unbreakableReceiver.testPrint())
    #UNBREAKABLESLUTT


    #RSASTART
    print("\n\nRSA-Cipher:\n")
    rsaSender = Sender("RSA", rsa)
    rsaReceiver = Receiver("RSA", rsa)

    rsaSender.send_cipher(rsaReceiver, testTekst)
    print("message crypted: " + str(rsaSender.test_print()))
    print("message crypted: " + rsaReceiver.testPrint())
    #RSASLUTT

    print("\n""Hacker-Initiate: \n")
    cracks = Hacker().crack(testTekst, caesar)
    print("message cracked" + cracks.test_print())



if __name__ == "__main__":
    main()


