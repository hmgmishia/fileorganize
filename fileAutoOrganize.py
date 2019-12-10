import os
import sys
import platform
import getpass
import glob
from argparse import ArgumentParser
import datetime
import shutil

#option引数を受け取るための処理
def get_option():
    argparser = ArgumentParser()
    argparser.add_argument('-p', '--path', type=str,
                           default="Pictures",
                           help='checking path ex:-p Pictures -> checking path: /Users/$username/Pictures')
    argparser.add_argument('-o', '--output', type=str,
                           default="Pictures",
                           help='picture move to path ex:-p Pictures -> move to path: /Users/$username/Pictures/$date')
    return argparser.parse_args()

#args取得
args = sys.argv
optionargs = get_option()
#pathの構築
basepicturepath = os.path.expanduser('~') + "/" + optionargs.path
outputpath = os.path.expanduser('~') + "/" + optionargs.output
filepathlist = glob.glob(basepicturepath + "/*.*")
#取得したファイルを移動する
for filepath in filepathlist:
    dt = datetime.datetime.fromtimestamp(os.stat(filepath).st_ctime)
    movepath = outputpath + "/" + str(dt.year) + "/" + str(dt.month) + "/" + str(dt.day)
    #既に作られててもエラーを出さないようにexitst_okをtrueに
    os.makedirs(movepath, exist_ok=True)
    shutil.move(filepath, movepath + "/" + os.path.basename(filepath))
    
