import os

def transfrom_xyz_to_txt(input, output):
    with open(input, 'r') as xyz_file, open(output, 'w') as txt_file:
        for line in xyz_file:
            x, y, z = line.strip().split()
            txt_file.write(f"{x}\t{y}\t{z}\n")

dir_in = os.path.dirname(os.path.abspath(__file__))
input = os.path.join(dir_in, '../01_DATA/Z13/cutCAD_Z13.xyz')

dir_out = os.path.dirname(os.path.abspath(__file__))
output = os.path.join(dir_out, '../01_DATA/Z13/cutCAD_3D_Z13.txt')

transfrom_xyz_to_txt(input, output)