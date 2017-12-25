#!/usr/bin/python
import sys

nato_phonetic = {'a': 'Alpha', 'c': 'Charlie', 'b': 'Bravo', 'e': 'Echo', 'd': 'Delta', 'g': 'Golf', 'f': 'Foxtrot', 'i': 'India', 'h': 'Hotel', 'k': 'Kilo', 'j': 'Juliet', 'm': 'Mike', 'l': 'Lima', 'o': 'Oscar', 'n': 'November', 'q': 'Quebec', 'p': 'Papa', 's': 'Sierra', 'r': 'Romeo', 'u': 'Uniform', 't': 'Tango', 'w': 'Whiskey', 'v': 'Victor', 'y': 'Yankee', 'x': 'X-ray', 'z': 'Zulu', '.': 'Dot' , '@': 'At', ' ': ' ', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}

if len(sys.argv) < 2:
  print "usage: spell <word1> <word2> <word3>...\nwrites phonetic spelling"
  print nato_phonetic

for w in sys.argv[1:]:
  try:
    spelling = " , ".join([nato_phonetic[l] for l in w.lower()])
    print w+" --> "+spelling
  except KeyError:
    print w+" contains non-letters"


