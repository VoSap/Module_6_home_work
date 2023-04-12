import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []

MP3_MUSIC = []
OGG_MUSIC = []
WAV_MUSIC = []
AMR_MUSIC = []
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []
OTHERS_FILES = []

REGISTER_EXTENSION = {
    'JPEG' : JPEG_IMAGES,
    'JPG' : JPG_IMAGES,
    'PNG' : PNG_IMAGES,
    'SVG' : SVG_IMAGES,
    'AVI' : AVI_VIDEO,
    'MP4' : MP4_VIDEO,
    'MOV' : MOV_VIDEO,
    'MKV' : MKV_VIDEO,
    'DOC' : DOC_DOCUMENTS,
    'DOCX' : DOCX_DOCUMENTS,
    'TXT' : TXT_DOCUMENTS,
    'PDF' : PDF_DOCUMENTS,
    'XLSX' : XLSX_DOCUMENTS,
    'PPTX' : PPTX_DOCUMENTS,
    'MP3' : MP3_MUSIC,
    'OGG' : OGG_MUSIC,
    'WAV' : WAV_MUSIC,
    'AMR' : AMR_MUSIC,
    'ZIP' : ZIP_ARCHIVES,
    'GZ' : GZ_ARCHIVES,
    'TAR' : TAR_ARCHIVES
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extensions(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        # Работа с папками
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                FOLDERS.append(item)
                scan(item)  # рекурсия
            continue # переходим к следующему элементу сканируемой папке
        # Работа с файлами
        ext = get_extensions(item.name) # берем расширение файла
        full_name = folder / item.name # берем полный путь до файла
        if ext:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSIONS.add(ext)
                container.append(full_name)
            except KeyError:
                OTHERS_FILES.append(full_name)
                UNKNOWN.add(ext)


        #     container = REGISTER_EXTENSION[ext]
        #     if container is not None:
        #         EXTENSIONS.add(ext)
        #         container.append(full_name)
        #     else:
        #         OTHERS_FILES.append(full_name)
        #         UNKNOWN.add(ext)
        # else:
        #     OTHERS_FILES.append(full_name)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f"Start in folder {folder_for_scan}")
    scan(Path(folder_for_scan))
    print(f"Images jpeg: {JPEG_IMAGES}")
    print(f"Images jpg: {JPG_IMAGES}")
    print(f"Images png: {PNG_IMAGES}")
    print(f"Images svg: {SVG_IMAGES}")
    print(f"Videos avi: {AVI_VIDEO}")
    print(f"Videos mp4: {MP4_VIDEO}")
    print(f"Videos mov: {MOV_VIDEO}")
    print(f"Videos mkv: {MKV_VIDEO}")
    print(f"Docoments doc: {DOC_DOCUMENTS}")
    print(f"Docoments docx: {DOCX_DOCUMENTS}")
    print(f"Docoments txt: {TXT_DOCUMENTS}")
    print(f"Docoments pdf: {PDF_DOCUMENTS}")
    print(f"Docoments xlsx: {XLSX_DOCUMENTS}")
    print(f"Docoments pptx: {PPTX_DOCUMENTS}")
    print(f"Music mp3: {MP3_MUSIC}")
    print(f"Music ogg: {OGG_MUSIC}")
    print(f"Music wav: {WAV_MUSIC}")
    print(f"Music amr: {AMR_MUSIC}")
    print(f"Archive zip: {ZIP_ARCHIVES}")
    print(f"Archive gz: {GZ_ARCHIVES}")
    print(f"Archive tar: {TAR_ARCHIVES}")
    print('*' * 25)
    print(f"Type of file in folder {EXTENSIONS}")
    print(f"UNKNOW: {UNKNOWN}")
