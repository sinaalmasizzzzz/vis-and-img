import requests
import os

def download_image(url, file_name):
    result = requests.get(url)
    
    if result.status_code == 200:  # اگر درخواست موفقیت‌آمیز بود
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")  # پیدا کردن مسیر دسکتاپ
        file_path = os.path.join(desktop_path, file_name)  # مسیر کامل فایل
        with open(file_path, 'wb') as file:
            file.write(result.content)  # محتوای عکس را به صورت باینری ذخیره می‌کند
        print(f"Image successfully downloaded to {file_path}")
    else:
        print("Failed to download image")

# استفاده:
download_image("https://th.bing.com/th/id/OIP.P-fhPeG52vtBHxVkzOy5DAHaE8?w=286&h=191&c=7&r=0&o=5&dpr=1.5&pid=1.7", "install.png")

#این کد رو با استفاده از هوش مصنوعی نوشتم 
