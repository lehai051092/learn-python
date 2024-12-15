from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
TO_ADDRESS = "___YOUR_EMAIL_HERE____"
MY_LAT = 21.037762  # Your latitude
MY_LONG = 105.800812  # Your longitude


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


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        success, message = send_email(
            MY_EMAIL,
            MY_PASSWORD,
            TO_ADDRESS,
            "Look Up👆",
            "The ISS is above you in the sky."
        )

        print(f"{success}, {message}")
