
# TODO 目前只设定为处理一个文件下的存在于.assets中文件的编码
import argparse
import re
import os
from glob import glob


def get_args():
    parser = argparse.ArgumentParser(
        description='replace the image links in markdown files under the given \
            folder')
    parser.add_argument('-i', '--indir', type=str,
                        help='the folder containing markdown files')
    args = parser.parse_args()
    return args


def main(args):

    # folder = args.i
    # print(folder)
    folder = args.indir.rstrip('/')
    print(folder)
    files = glob(folder + '/*.md')
    files = [file for file in files if 'tt_' not in file]
    # print(files)
    for file in files:
        with open(file, 'r') as f:
            pass
            s = f.read()
            new_image_path = os.path.basename(file).replace('.md', '.assets')
            # print(new_image_path)
            s2 = re.sub('\]\(.*image-', ']('+new_image_path+'/image-', s)
            # new_file_path = os.path.join(folder, 'tt_'+os.path.basename(file))
        with open(file, 'w') as fw:
            fw.write(s2)

    # path = os.path.dirname(file)
    # print(path)
    # files = [folder+]



if __name__ == '__main__':
    args = get_args()
    main(args)
