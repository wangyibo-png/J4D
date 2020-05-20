from trans_DNA import *
from J4D import *
import os

# def main():
#     '''
#     example of using J4D
#     '''
#     clf = J4D() 
#     cnt = clf.encode('original.jpg')
#     print(cnt)
#     clf.decode(cnt)

# if __name__ == '__main__':
#     main()

infile_folder = 'output/j4d'
dna_folder = 'dna_file'
message = 'message.csv'
outfile_folder = 'outfile/j4d'
trans_DNA = trans_DNA(infile_folder, dna_folder, message, outfile_folder)
clf = J4D()
cnt = clf.encode('original.jpg')
print(cnt)
trans_DNA.all_encode()
trans_DNA.all_decode()
clf.decode(cnt, encode_dir='outfile', zipfile_dir=infile_folder)