from binarytree import *

class MorseTree:
    def __init__(self): # creates the morse code binary tree
        morsecode = open("morse.txt","r")

        self.MorseTree = BinaryTree("$")

        for aline in morsecode:
            parent = self.MorseTree
            dotsndash = aline.split()
            a = dotsndash[0]
            i = a[:len(a)-1]
            while i != "":
                achar = i[0]
                if "." in achar:
                    parent = parent.getLeftChild()
                if "-" in achar:
                    parent = parent.getRightChild()
                i = i[1:]
            if "." in a[-1]:
                parent.insertLeft(dotsndash[-1])
            if "-" in a[-1]:
                parent.insertRight(dotsndash[-1])

        
    def decode(self, messagefile):# decodes a message into rough form ("/" instead of " ")
        message = open(messagefile, "r") # make sure message is in txt format
        morse = self.MorseTree
        messagestring = ""
        for aline in message:
            words = aline.split()
            for aword in words:
                parent = morse
                while aword != "":
                    achar = aword[0]
                    if "." in achar:
                        parent = parent.getLeftChild()
                    if "-" in achar:
                        parent = parent.getRightChild()
                    aword = aword[1:]
                messagestring = messagestring + parent.getRootVal()
        return messagestring               
                
            
    def cleanDecode(self, dirtydecode):
        clean = dirtydecode.replace("/"," ")
        return clean

    
    
