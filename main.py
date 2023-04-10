from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalize import normalize


def handle_media(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    archive_folder = target_folder / filename.stem.replace(filename.suffix, '')
    archive_folder.mkdir(exist_ok=True)
    shutil.unpack_archive(str(filename), str(archive_folder))
    filename.unlink()


def handle_folder(folder: Path) -> None:
    try:
        folder.rmdir()
    except OSError:
        print(f"Sorry, i cant delete this {folder}")


def main(folder: Path) -> None:
    parser.scan(folder)
    for file in parser.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')

    for file in parser.AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')
    for file in parser.MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')
    for file in parser.MOV_VIDEO:
        handle_media(file, folder / 'video' / 'MOV')
    for file in parser.MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')

    for file in parser.DOC_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOC')
    for file in parser.DOCX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOCX')
    for file in parser.TXT_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'TXT')
    for file in parser.PDF_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PDF')
    for file in parser.XLSX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'XLSX')
    for file in parser.PPTX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PPTX')

    for file in parser.MP3_MUSIC:
        handle_media(file, folder / 'audio' / 'MP3')
    for file in parser.OGG_MUSIC:
        handle_media(file, folder / 'audio' / 'OGG')
    for file in parser.WAV_MUSIC:
        handle_media(file, folder / 'audio' / 'WAV')
    for file in parser.AMR_MUSIC:
        handle_media(file, folder / 'audio' / 'AMR')

    for file in parser.OTHERS_FILES:
        handle_other(file, folder / 'other_files')

    for file in parser.ZIP_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'ZIP')
    for file in parser.GZ_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'GZ')
    for file in parser.TAR_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'TAR')

    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)


if __name__ == '__main__':
    folder_for_scan = Path(sys.argv[1])
    main(folder_for_scan.resolve())
