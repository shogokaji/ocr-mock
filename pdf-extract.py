from pdf2image import convert_from_path
import pytesseract
import time

# PDFからテキストを抽出する関数を定義
def ocr_from_pdf(file_path):
    # pdfを画像に変換する
    images = convert_from_path(file_path)

    text = ''
    # 各ページの文字を抽出する処理、解析言語にjpnを指定
    for i in range(len(images)):
        text += pytesseract.image_to_string(images[i], lang='jpn')

    return text

# 抽出対象ファイルパス
PDF_FILE_PATH = "./docs/test.pdf"
text = ocr_from_pdf(PDF_FILE_PATH)

# tmp以下に書き出す
f = open(f'./tmp/pdf-{int(time.time())}.txt', 'w')
f.write(text)
f.close()