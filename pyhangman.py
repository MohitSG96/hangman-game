#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:44:57 2019

@author: mohit
"""

import random

class HangMan(object):
    
    hang = []                         #Hang Tower
    hang.append("+---+")
    hang.append("|   |")
    hang.append("|")
    hang.append("|")
    hang.append("|")
    hang.append("|")
    hang.append("+-------")
    
    man = {}                            #Hang Man
    man[0] = ["|   O"]
    man[1] = ["|   O",
              "|   |"]
    man[2] = ["|   O",
              "|  /|"]
    man[3] = ["|   O",
              "|  /|\\"]
    man[4] = ["|   O",
              "|  /|\\",
              "|  /"]
    man[5] = ["|   O",
              "|  /|\\",
              "|  / \\",
              "|",
              "+-     -"]
    
    hangManTower = []
    hangManTower.append(hang[:])
    
    WORDLIST = 'WORDS'
    randnum = random.randint(1,27)  # 27=number of  words in WORDS file
    
    def __init__(self):
        i, j = 2,0
        for l in self.man.values():
            pic, j = self.hang[:],0
            for m in l:
                pic[i+j] = m
                j += 1
            self.hangManTower.append(pic)
                
            
    
    def askAndValidate(self,word,result,missed):
        guess = input()
        if guess == None or len(guess) != 1 or (guess in missed) or (guess in result):
            return None, False
        
        i=0
        right = guess in word
        for c in word:
            if c == guess:
                result[i] = c
            
            i+=1
        return guess, right
    
    def get_random_word(self):
        """Get a random word from the wordlist using no extra memory."""
        curr_word = None
        i = 0
        with open(self.WORDLIST, 'r') as f:
            for word in f:
                word = word.strip().lower()
                if i == self.randnum-1:
                    curr_word = word
                i += 1
        return curr_word
    
    def drawHangMan(self, i):
        for p in self.hangManTower[i]:
            print(p)
        
    
    def start(self):
        print("Welcome to Hangman!")
        word = list(self.get_random_word())
        result = list('*'*len(word))
        print("The word is ",result)
        passed, i, missed = False, 0, []
        while i < len(self.hangManTower)-1:
            print("Guess the word", end="")
            guess, right = self.askAndValidate(word,result,missed)
            if guess == None:
                print("The Word had already guessed")
                continue
            print("".join(result))
            if result == word:
                print("×,.·´¨'°÷·..§", "You have guessed the word","§.·´¨'°÷·..×")
                passed = True
                break
            if not right:
                missed.append(guess)
                i+=1
            self.drawHangMan(i)
            print("Missed charaters ",missed)
            
        if not passed:
            print("(;ﾟ︵ﾟ;) The word was ->>' "+"".join(word),"'<<-the man had been hung (;ﾟ︵ﾟ;)")
        

a = HangMan().start()