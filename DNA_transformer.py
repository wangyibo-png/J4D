from utils import *
from DNAFountain import *
import zipfile, os
import bz2, lzma
import csv, shutil
logging.getLogger().setLevel(logging.DEBUG)

class DNA_transformer:

    def __init__(self, infile_folder, dna_folder, message_file, out_file_folder):
        self.infile_folder = infile_folder
        self.dna_folder = dna_folder
        self.message_file = message_file
        self.out_file_folder = out_file_folder
    
    def Jpeg2DNA(self, input_file, dna_file):
        in_file = 'temp_in_file'
        temp_file = zipfile.ZipFile(in_file,mode='w', allowZip64=False, compression=zipfile.ZIP_LZMA)
        temp_file.write(input_file)
        temp_file.close()

        data, pad_num = preprocess(in_file, 17)

        f = DNAFountain(data, alpha=0.5, rs=4)
        f.encode()
        f.save(dna_file)
        os.remove(in_file)

        return len(data), pad_num

    def DNA2Jpeg(self, dna_file, data_length, pad_num, out_file_folder):
        out_file = 'temp_out_file'
        g = Glass(dna_file, data_length, rs=4, pad_num=pad_num)
        g.decode()
        g.save(out_file)

        out_zip_file = zipfile.ZipFile(out_file, 'r')
        out_zip_file.extractall(out_file_folder)
        os.remove(out_file)

    def all_encode(self):
        if os.path.exists(self.dna_folder):
            shutil.rmtree(self.dna_folder)
        os.mkdir(self.dna_folder)
        file_names = os.listdir(self.infile_folder)
        for i in range(len(file_names)):
            if (file_names[i].split('.'))[-1] != 'j4d':
                del(file_names[i])
        file_names.sort(key=lambda x:int(x.split('.')[0]))
        f = open(self.message_file, 'w')
        f_csv = csv.writer(f)
        for file_name in file_names:
            print('-'*20+'encode '+file_name+'-'*20)
            f_csv.writerow(self.Jpeg2DNA(input_file=os.path.join(self.infile_folder,file_name), dna_file=os.path.join(self.dna_folder, file_name+'.dna.Fasta')))



    def all_decode(self):
        file_names = os.listdir(self.dna_folder)
        file_names.sort(key=lambda x:int(x.split('.')[0]))
        param = []
        with open(self.message_file,'r') as f:
            f_csv = csv.reader(f)
            for line in f_csv:
                param.append([int(line[0]), int(line[1])])
        for i in range(len(file_names)):
            print('-'*20+'decode '+file_names[i]+'-'*20)
            self.DNA2Jpeg(dna_file=os.path.join(self.dna_folder, file_names[i]), data_length=param[i][0], pad_num=param[i][1], out_file_folder=self.out_file_folder)