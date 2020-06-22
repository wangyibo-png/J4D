# J4D
python包：reedsolo  0.3.0

在运行过程中会生成诸多文件，推荐将文件生成存储到之外的文件夹中。

J4D相关文件：J4D.py,jpegtran相关,scanfile.txt(存储扫描的相关信息)

Fountain相关：DNAFountain.py,Helper_Functions.py,RPNG.py

DNA_transformer.py融合上面模块

可直接运行main.py，其中folder_path将会存储DNA序列、扫描图片等输出。

输出：

message.csv：存储data和pad_num

dna_file：存储分层的DNA序列文件

scan_img：存储分层扫描文件

outfile：从DNA序列中decode后，unzip生成的文件

output：J4D部分encode生成的文件

不足之处：

1.outfile的文件层数太多

2.大文件处理时间过长(可以尝试将j4d文件进一步拆分，然后最后合并)
