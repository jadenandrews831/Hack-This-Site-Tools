#!/usr/bin/env python3

from argparse import ArgumentParser

def decrypt(wrd):
  d_wrd = ''
  for i, c in enumerate(wrd):
    d_wrd += chr(ord(c)-i)
  return d_wrd

if __name__ == '__main__':
  parser = ArgumentParser(description='A tool for reversing the encryption method\n\
                                      used in the Hack This Site Basic Excercise #6')
  parser.add_argument('-w --word', dest="word", help='the word to be decrypted', required=True)

  parsed_args = parser.parse_args()
  wrd = parsed_args.word
  print(f'The decrypted word is: {decrypt(wrd)}')
