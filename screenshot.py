from docx import Document
from docx.shared import Inches
from datetime import datetime


def save_screenshot(image_path, docx_file):

    with open('user.txt', 'r') as file:
        global user
        user = file.read()
    # Lấy thời gian hiện tại
    current_date = datetime.now().date()
    formatted_date = current_date.strftime("%d/%m/%Y")
    current_time = datetime.now()
    hour = current_time.hour
    minute = current_time.minute

    doc = Document(docx_file)
    time =str(user)+str(hour) + ":" + str(minute) + " ngày " + str(formatted_date)

    # Chèn ảnh và thời gian
    doc.add_paragraph(time)
    doc.add_picture(image_path, width=Inches(6.0))  # 6.0 là kích thước
    doc.save(docx_file)


