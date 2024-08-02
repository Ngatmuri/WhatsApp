from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Setup opsi untuk ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Opsional, jalankan di background
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inisialisasi WebDriver
service = Service('/data/data/com.termux/files/home/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://web.whatsapp.com/')

# Tunggu pengguna untuk memindai QR code
input('Scan QR Code dan tekan Enter setelah selesai')

def send_message(contact_name, message):
    # Cari dan pilih kontak
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(contact_name)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    
    # Siapkan area pesan
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
    message_box.click()
    
    # Meniru mengetik
    for char in message:
        message_box.send_keys(char)
        time.sleep(0.1)  # Waktu delay per karakter (dapat diubah sesuai kebutuhan)
    message_box.send_keys(Keys.RETURN)

contact = 'Nama Kontak Anda'
message = 'Pesan otomatis dari Termux yang meniru aktivitas mengetik!'

# Kirim pesan
send_message(contact, message)

# Tutup browser setelah beberapa detik
time.sleep(10)
driver.quit()
