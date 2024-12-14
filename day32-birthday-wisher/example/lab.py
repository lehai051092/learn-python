import smtplib
from calendar import MONDAY
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from random import choice


def send_email(sender_email, password, receiver_email, subject, body):
    # Tạo đối tượng MIMEMultipart để xử lý email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Thêm nội dung email dưới dạng MIMEText
    # Sử dụng utf-8 để hỗ trợ tiếng Việt
    message.attach(MIMEText(body, "plain", "utf-8"))

    try:
        # Kết nối đến server SMTP của Gmail với port 587
        connection = smtplib.SMTP("smtp.gmail.com", 587)

        # Bắt đầu kết nối TLS để bảo mật
        connection.starttls()

        # Đăng nhập vào tài khoản Gmail
        connection.login(sender_email, password)

        # Chuyển đổi object message thành string
        text = message.as_string()

        # Gửi email
        connection.sendmail(sender_email, receiver_email, text)

        # Đóng kết nối
        connection.quit()

        return True, "Email đã được gửi thành công!"

    except Exception as e:
        return False, f"Lỗi khi gửi email: {str(e)}"


now = datetime.now()
day_of_week = now.weekday()

if day_of_week == MONDAY:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        quote = choice(quotes)

    # Ví dụ sử dụng:
    my_email = "le.thanh.hai051092@gmail.com"
    my_password = "bcwclxmowcmlcmcn"  # Sử dụng App Password, không phải mật khẩu Gmail
    to_address = "bibo051092@gmail.com"

    success, message = send_email(
        my_email,
        my_password,
        to_address,
        "Monday Motivation",
        quote
    )

    print(f"{success}, {message}")
