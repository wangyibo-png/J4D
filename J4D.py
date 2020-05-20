'''
This class is used for progressive preview,
and J4D only exists two methods: encode and decode.
You can find the example in the main function.
We support only windows, linux and mac, due to the jpegtran binary file, and we are not sure about other platforms.

By Hanmo Chen, Yucheng Han.
'''
import pandas as pd 
import os
import platform
import shutil
import sys 


class J4D():
    def __init__(self, scan_file='scanfile.txt', binary_fpath=''):
        '''
        @params:
        scan_file: the path of the scanfile, which is used to define how to progressively
                handle the jpeg images.
        binary_fpath: the dir of the jpegtran binary file e.g. jpeg.exe. default to be ''
        '''
        self.scan_file = scan_file
        self.binary_fpath = binary_fpath
        self.platform = platform.platform()
        # self.scan_cmds = pd.read_csv(self.scan_file, comment='#', header=None, sep='nonsense')[0]
        if 'Windows' in self.platform or 'windows' in self.platform:
            print('running on windows system')
            self.binary_fpath = os.path.join(self.binary_fpath, 'jpegtran.exe')
        elif 'linux' in self.platform or 'Linux' in self.platform:
            print('running on Linux system')
            self.binary_fpath = os.path.join(os.getcwd(), self.binary_fpath, 'jpegtran_linux')
        else:
            print('running on not windows system')
            self.binary_fpath = os.path.join(os.getcwd(), self.binary_fpath, 'jpegtran')
    
    def encode(self, input_img, output_dir='output'):
        '''
        @params:
        input_img: the img needs to be handle.
        output_dir: there will be the j4d files and the progressively previewd images.
        '''
        if output_dir == '':
            raise ValueError('output dir should not be set to None')
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        os.mkdir(output_dir)
        # if os.path.exists('encode_img'):
        #     shutil.rmtree('encode_img')
        # if os.path.exists('j4d'):
        #     shutil.rmtree('j4d')
        os.mkdir(os.path.join(output_dir, 'encode_img'))
        os.mkdir(os.path.join(output_dir, 'j4d'))

        tem_output = os.path.join(output_dir, 'encode_img', 'temp.jpg')
        if 'Windows' in self.platform or 'windows' in self.platform:
            os.system('{} -progressive -scans {} {} {}'.format(self.binary_fpath, self.scan_file, input_img, tem_output))
        else:
            os.system('{} -progressive -scans {} {} > {}'.format(self.binary_fpath, self.scan_file, input_img, tem_output))

        with open(tem_output,'rb') as f:
            jpegBytes = f.read()
        pos = 0
        cnt = 0
        tem_fragment = 0


        while(pos != -1):
            next_pos = jpegBytes.find(b'\xff\xda',pos+1)
            fragment = jpegBytes[pos:next_pos] if next_pos != -1 else jpegBytes[pos:]
            frag_name = os.path.join(output_dir, 'j4d', str(cnt) + '.j4d')
            if cnt == 0:
                tem_fragment = fragment
            else:
                with open(frag_name, 'wb') as f:
                    if cnt == 1:
                        fragment = tem_fragment + fragment
                    f.write(fragment)
            cnt = cnt + 1
            print('find fragment {}'.format(cnt))   
            pos = next_pos

        return cnt
    
    def decode(self, cnt, encode_dir='output', output_dir='scan_img', zipfile_dir='output/j4d'):
        '''
        you can preview the imgs from the .j4d files.
        @params:
        cnt: the amount of the fragment, which is also the output of the encode function.
        encode_dir: the param 'output_dir' of the encode function, and this function will
                find the j4d file in 'encode_dir/j4d'
        output_dir: the dir for the result of the decoding.
        '''
        if output_dir == '' or encode_dir == '':
            raise ValueError('output dir or j4d dir should not be set to None')
        if not os.path.exists(os.path.join(encode_dir, 'j4d')):
            raise ValueError('there is no j4d file in the output_dir')
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
        os.mkdir(output_dir)
        with open(os.path.join(encode_dir,'j4d' , zipfile_dir,'1.j4d'),'rb') as f:
            jpegBytes = f.read()
        for idx in range(2,cnt):
            frag_name = os.path.join(encode_dir, 'j4d', zipfile_dir, str(idx) + '.j4d')
            with open(frag_name,'rb') as f:
                readBytes = f.read()
            jpegBytes = jpegBytes + readBytes
            img_name = os.path.join(output_dir, str(idx-1)+'_scan.jpg')
            with open(img_name, 'wb') as f:
                f.write(jpegBytes)