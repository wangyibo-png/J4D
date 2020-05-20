from DNA_transformer import *
from J4D import *
import os

def main():

    folder_path = '/Users/apple/Downloads/folder/'

    infile_folder = os.path.join(folder_path, 'output/j4d')
    dna_folder = os.path.join(folder_path, 'dna_file')
    message = os.path.join(folder_path, 'message.csv')
    outfile_folder = os.path.join(folder_path, 'outfile/j4d')
    dnaTF = DNA_transformer(infile_folder, dna_folder, message, outfile_folder)


    # JPEG split into fragments
    jpegTF = J4D()
    cnt = jpegTF.encode('original.jpg', output_dir=os.path.join(folder_path,'output'))
    print("No. of fragments: {}".format(cnt))

    # Encode the fragments into DNA
    dnaTF.all_encode()

    # Decode the DNA into fragments
    dnaTF.all_decode()

    # Progressive read the fragments
    jpegTF.decode(cnt, encode_dir=os.path.join(folder_path, 'outfile'),output_dir=os.path.join(folder_path, 'scan_img'), zipfile_dir=infile_folder)

if __name__ == '__main__':
    main()

