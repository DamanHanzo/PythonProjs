
# Functions to use for verifying anagrams

def moveToFront(word,pos):

    """anagram produced by moving word[pos] to the start (front) of word
         requires: 0 <= pos < len(word)"""
    return word[pos]+word[:pos]+word[pos+1:]

def moveToBack(word,pos):
    """anagram produced by moving word[pos] to the back (end of word
         requires: 0 <= pos < len(word)"""
    return word[:pos]+word[pos+1:]+word[pos]

def swap(word,pos1,pos2):
    """anagram produced by swapping characters at positions pos1 and pos2
         requires: 0 <= pos1 <= pos2 < len(word)"""
    return word[:pos1]+word[pos2]+word[pos1+1:pos2]+word[pos1]+word[pos2+1:]

def reverse(word,pos1,pos2):
    """produced by reversing the substring from pos1 up to, but not including, pos2
          requires: 0 <= pos1 <= pos2 < len(word)"""
    return word[:pos1]+word[pos1:pos2][::-1]+word[pos2:]

front=moveToFront("good show",3)
back=moveToBack("good show",3)
switch=swap("good show",2,6)
flop=reverse("good show",2,6)
