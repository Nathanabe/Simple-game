#!/usr/bin/env python3
print("Welcome to the brain game")

playing = input("Do you want to test your of the world? ")

if playing != "yes":
    quit()

print("okay let's play :)")
score = 0
print("Question "  +  str(1))

answer = input("what part of the sun has the most gravitational pull? ")
if answer.lower() == "the black spot":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(2))

answer = input("who was the first man to land on the moon? ")
if answer.lower() == "niel armstrong":
    print("correct!")
    score += 1

else:
    print("incorrect!")

answer = input("what does DNA stand for? ")
if answer.lower() == "deoxoribonucliec acid":
    print("correct!")
    score += 1

else:
    print('incorrect!')

print("Question "  +  str(3))

answer = input("How many bones are here in the human body? ")
if answer == "206":
    print("correct!")
    score += 1

else:
    print("incorrect")

print("Question "  +  str(4))

answer = input("The concept of gavity was discovered by which famous scientist? ")
if answer.lower() == "sir isaac newton":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(5))

answer == input("What is the hardest natural substance on earth? ")
if answer.lower() == "diamond":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(6))

answer == input("Which is the main gas that makes up the earth's atmosphere? ")
if answer.lower() == "nitrogen":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(7))

answer == input("Humans and chimpanzees share roughly how much DNA? ")
if answer == "98 percent":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(8))

answer == input("Roughly how long does it take for sunlight to reach the earth? ")
if answer == "8 minutes":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(8))

answer == input("Which famous British physicist wrote a brief histor of time? ")
if answer.lower() == "stephen hawking":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(9))

answer == input("At what temperature are Celsius and Fahrenheit equal? ")
if answer == "-40":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(10))

answer == input("What modern-day country was Marie Curie born in? ")
if answer.lower() == "Poland":
    print("correct!")
    score += 1

else:
    print("correct!")

print("Question "  +  str(11))

answer == input("what is the name is given for the number of protons found in the nucleus of an atom? ")
if answer.lower() == "atomic number":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(12))

answer == input("How many vertebrae does the average man posses? ")
if answer == "33":
    print("correct!")
    score += 1

else:
    print("correct!")

print("Question "  +  str(13))

answer == input("which oath of ethics taken by doctors is named after an ancient Greek physician? ")
if answer.lower() == "hippocratic oath":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(14))

answer == input("What is the study of mushrooms called? ")
if answer.lower() == "mycology":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(15))

answer == input("What is the fastest land animal? ")
if answer.lower() == "cheetah":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(16))

answer == input("What do the letters in the word LASER stand for? ")
if answer.lower() == "light amplfication by stimulated emission of radiation":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(17))

answer == input("Who is credited with the creation of the world wide web? ")
if answer.lower() == "tim berners-lee":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(18))

answer == input("Which of the worlds ocean is the deepest? ")
if answer.lower() == "pacific":
    print("correct!")
    score += 1

else:
    print("incorrect!")

print("Question "  +  str(19))

answer == input("how many bones do sharks have? ")
if answer.lower() == "zero":
    print("correct!")
    score += 1

else:
    print("incorret!")

print("Question "  +  str(20))

answer == input("What does desquamation? ")
if answer.lower() == "peeling skin":
    print("correct!")
    score += 1

print("You got " + str(score) +  " questions correct")
print("You got " + str((score / 20) * 100) +  "%.")
