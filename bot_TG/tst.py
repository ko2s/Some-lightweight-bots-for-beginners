from PIL import Image
import pytesseract

# تحديد مسار Tesseract إذا لم يكن مضبوطًا تلقائيًا
pytesseract.pytesseract.tesseract_cmd = r'E:\Program Files\Tesseract-OCR\tesseract.exe'

# تحميل الصورة
image_path = "image.png"  # ضع هنا مسار الصورة
image = Image.open(image_path)

# استخراج النص من الصورة
extracted_text = pytesseract.image_to_string(image, lang='ara+eng')

# طباعة النص المستخرج
print("النص المستخرج:")
print(extracted_text)

# استخراج اسم الطالب ورقم الطالب والتحقق من مادة "برمجة 2"
student_name = None
student_id = None
has_programming_2 = False
# تحليل النص المستخرج
for line in extracted_text.split("\n"):
    if "اسم الطالب" in line:
        student_name = line.split(":")[-1].strip()
    if "رقم الطالب" in line:
        student_id = line.split(":")[-1].strip()
    if "برمجة 2" in line:
        has_programming_2 = True
