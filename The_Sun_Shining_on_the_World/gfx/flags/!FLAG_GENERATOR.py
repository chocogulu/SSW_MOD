import re
import shutil
import os

# これは、イデオロギーを新しく追加した時にとりあえず仮の国旗を追加するプログラムです
# 作者：Y式植林装置

BASE_PATH = "The_Sun_Shining_on_the_World/gfx/flags/"
DIR_STRUCTURE = {"large": {"path": "", "template": "ANARCHISM汎用大.tga"},
                 "medium": {"path": "medium/", "template": "ANARCHISM汎用中.tga"},
                 "small": {"path": "small/", "template": "ANARCHISM汎用小.tga"}}

# 国家タグ一覧を取得する
tags_file = open(
    "The_Sun_Shining_on_the_World/common/country_tags/00_countries.txt", encoding="utf-8")
country_tags = set()
for line in tags_file.readlines():
    if re.match(r"\w{3}", line[:3]) != None:
        country_tags.add(line[:3])  # 国家タグを追加

print("Country tags", country_tags)

for flag_type in DIR_STRUCTURE:
    # tgaファイルを格納するフォルダへのパス
    size_path = BASE_PATH + DIR_STRUCTURE[flag_type]["path"]
    template = DIR_STRUCTURE[flag_type]["template"]
    files = os.listdir(size_path)

    for tag in country_tags:  # タグごとにファイルを用意
        file_path = size_path + tag + "_anarchism.tga"
        if os.path.exists(file_path):
            print(tag+"'s flag was skipped")
            continue  # 既にファイルが存在すれば
        shutil.copy(size_path+template, file_path)
        print(f"copied {tag}")
