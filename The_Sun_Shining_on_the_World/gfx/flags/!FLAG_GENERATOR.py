import shutil
import os

# これは、イデオロギーを新しく追加した時にとりあえず仮の国旗を追加するプログラムです
# 作者：Y式植林装置

BASE_PATH = "The_Sun_Shining_on_the_World/gfx/flags/"
DIR_STRUCTURE = {"large": {"path": "", "template": "ANARCHISM汎用大.tga"},
                 "medium": {"path": "medium/", "template": "ANARCHISM汎用中.tga"},
                 "small": {"path": "small/", "template": "ANARCHISM汎用小.tga"}}

for flag_type in DIR_STRUCTURE:
    # tgaファイルを格納するフォルダへのパス
    size_path = BASE_PATH + DIR_STRUCTURE[flag_type]["path"]
    template = DIR_STRUCTURE[flag_type]["template"]
    files = os.listdir(size_path)
    country_tags = set()

    for file in files:
        if not os.path.isfile(os.path.join(
                size_path, file)):  # フォルダを除外
            continue
        if not file.endswith(".tga"):  # tgaファイル以外を除外
            continue
        if file.startswith("ANARCHISM"):  # 特殊ファイルなので除外
            continue
        if file.startswith("Great"):  # 特殊ファイルなので除外
            continue
        if file.find("_") != -1:
            country_tags.add(file.split("_")[0])  # _の前までをリストに追加
        else:
            country_tags.add(file.split(".")[0])  # .の前までをリストに追加
    print(country_tags)

    for tag in country_tags:
        file_path = size_path + tag + "_anarchism.tga"
        if os.path.exists(file_path):
            continue  # 既にファイルが存在すれば
        shutil.copy(size_path+template, file_path)
        print(f"copied {tag}")
