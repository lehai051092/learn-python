# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.


from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas
import random
import smtplib

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


MY_EMAIL = ""
MY_PASSWORD = ""

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    success, message = send_email(
        MY_EMAIL,
        MY_PASSWORD,
        birthday_person["email"],
        "Happy Birthday!",
        contents
    )

    print(f"{success}, {message}")
