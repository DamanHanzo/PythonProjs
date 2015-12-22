word = 'debit-card'
print(word)
word = moveToFront(word,7)
print(word)
word = moveToBack(word,5)
print(word)
word = swap(word,2,5)
print(word)
word = reverse(word,3,6)
print(word)
word = swap(word,7,4)
print(word)
word = moveToBack(5)
print(word)
word = swap(word,8,9)
print(word)
word = moveToFront(word,5)
print(word)

# Functions to use for verifying anagrams

word_str = input('Input a word string: ')
position1 = int(input('Input a position value: '))
position2 = int(input('Input a position value: '))

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
front=moveToFront(word_str,position1)
back=moveToBack(word_str,position1)
switch=swap(word_str,position1,position2)
flop=reverse(word_str,position1,position2)
