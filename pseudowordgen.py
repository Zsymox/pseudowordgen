'''
No Big License
This program can be completely modified like anything and used in any ways but with credits to the author 'Zsymox'
Also returns in the form of small letter.
Contains 4 module Variables
I) Primary:
pri - Contains tuple of all the alphabets 
II) Secondary:
secall - Contains 2d tuple of all alphabet table
secalt - Contains 2d tuple where consonant are followed by vowels and vowels are followed by vowels or consonants
secaltvar - Similiar to secalt but some consonants also include h

should be used in the form of wordgen(length of word,primary,secondary)
'''
import random
#primary
pri = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
#secondary
secall=(#secondary all
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#A
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#B
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#C
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#D
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#E
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#F
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#G
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#H
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#I
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#J
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#K
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#L
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#M
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#N
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#O
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#P
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#Q
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#R
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#S
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#T
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#U
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#V
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#W
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#X
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#Y
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")#Z
                )
secalt=(#secondary alternating
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#A
                ("a","e","i","o","u"),#B
                ("a","e","i","o","u"),#C
                ("a","e","i","o","u"),#D
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#E
                ("a","e","i","o","u"),#F
                ("a","e","i","o","u"),#G
                ("a","e","i","o","u"),#H
                ("a","e","i","o","u"),#I
                ("a","e","i","o","u"),#J
                ("a","e","i","o","u"),#K
                ("a","e","i","o","u"),#L
                ("a","e","i","o","u"),#M
                ("a","e","i","o","u"),#N
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#O
                ("a","e","i","o","u"),#P
                ("a","e","i","o","u"),#Q
                ("a","e","i","o","u"),#R
                ("a","e","i","o","u"),#S
                ("a","e","i","o","u"),#T
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#U
                ("a","e","i","o","u"),#V
                ("a","e","i","o","u"),#W
                ("a","e","i","o","u"),#X
                ("a","e","i","o","u"),#Y
                ("a","e","i","o","u")#Z
                )
secaltvar=(#secondary alternating like variant by creator
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#A
                ("a","e","i","o","u"),#B
                ("a","e","i","o","u","h"),#C
                ("a","e","i","o","u"),#D
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#E
                ("a","e","i","o","u"),#F
                ("a","e","i","o","u"),#G
                ("a","e","i","o","u"),#H
                ("a","e","i","o","u"),#I
                ("a","e","i","o","u"),#J
                ("a","e","i","o","u"),#K
                ("a","e","i","o","u"),#L
                ("a","e","i","o","u"),#M
                ("a","e","i","o","u"),#N
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#O
                ("a","e","i","o","u",'h'),#P
                ("a","e","i","o","u"),#Q
                ("a","e","i","o","u"),#R
                ("a","e","i","o","u","h"),#S
                ("a","e","i","o","u",'h'),#T
                ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"),#U
                ("a","e","i","o","u"),#V
                ("a","e","i","o","u"),#W
                ("a","e","i","o","u"),#X
                ("a","e","i","o","u"),#Y
                ("a","e","i","o","u")#Z
                )

def wordgen(wordlen=6,first=pri,sec=secall):
        x = random.randint(0,len(first)-1)
        wd = first[x]
        for i in range(0,wordlen-1):
            secletter = random.randint(0,len(sec[x])-1)
            letconv = sec[x][secletter]
            wd = wd + letconv
            x = secletter
        print(wd)
