from PIL import Image
import pytesseract
import time

IMAGE_MODE = 'RGB'
# PDFからテキストを抽出する関数を定義
def ocr_from_image(file_path):
    # pdfを画像に変換する
    image = Image.open(file_path)
    # pytesseractで正常に処理できるモードに変換
    image = image.convert(IMAGE_MODE)
    # 画像から文字列データを抽出
    text = pytesseract.image_to_string(image, lang='jpn')
    
    return text

# 抽出対象ファイルパス
PDF_FILE_PATH = "./docs/test.png"
text = ocr_from_image(PDF_FILE_PATH)

# tmp以下に書き出す
f = open(f'./tmp/images-{int(time.time())}.txt', 'w')
f.write(text)
f.close()
