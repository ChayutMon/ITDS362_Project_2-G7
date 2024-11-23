Automated UI Testing: Sign up Testing

***
UI Testing นี้ประกอบด้วยสคริปต์การทดสอบอัตโนมัติสำหรับทดสอบฟังก์ชันการลงทะเบียน (signup) ของเว็บแอปพลิเคชัน 
โดยใช้ Selenium WebDriver ในภาษา Python และใช้ unittest framework เพื่อจัดการการทดสอบ จุดประสงค์ของการทดสอบนี้คือการตรวจสอบกระบวนการลงทะเบียนของผู้ใช้ว่าเป็นไปตามที่คาดหวังหรือไม่ในกรณีทดสอบที่ไม่มีข้อผิดพลาด
***

ส่วนประกอบหลักของการทดสอบ

การตั้งค่าเริ่มต้น (setUp)

สคริปต์เริ่มต้นโดยการตั้งค่า Edge WebDriver พร้อมกับการเปิดเบราว์เซอร์ในโหมดเต็มหน้าจอ (--start-maximized).
สร้างตัวแปร WebDriverWait สำหรับการรอคอยเพื่อความแน่ใจว่าทุกองค์ประกอบบนหน้าเว็บโหลดเสร็จเรียบร้อยก่อนที่จะทำการโต้ตอบ.
ตั้งค่าข้อมูลการทดสอบที่จำเป็น (เช่น URL, ชื่อผู้ใช้, อีเมล, รหัสผ่าน)

ขั้นตอนการทดสอบหลัก (test_signup_positive)

เริ่มทดสอบจากการเปิดเบราว์เซอร์และนำทางไปยัง URL ของแอปพลิเคชัน

Step 1: คลิกที่ปุ่ม "Sign Up" เพื่อเปิดฟอร์มการสมัครสมาชิก
Step 2: กรอกข้อมูลการสมัครในฟอร์ม (ชื่อผู้ใช้, อีเมล, รหัสผ่าน)
Step 3: กดปุ่ม "Submit" เพื่อส่งข้อมูล
Step 4: ตรวจสอบว่ามีข้อความยืนยันการสมัครที่สำเร็จ (เช่น ข้อความ "Welcome to Flarum") หรือไม่ หากพบว่าไม่มีข้อความยืนยัน จะถือว่าเป็นการทดสอบที่ล้มเหลว และจะทำการถ่ายภาพหน้าจอเพื่อการตรวจสอบเพิ่มเติม

ปิดเบราว์เซอร์หลังการทดสอบ 
หลังจากที่การทดสอบเสร็จสิ้นแล้ว, เบราว์เซอร์จะถูกปิดโดยการใช้ self.driver.quit().
จะมีข้อความพิมพ์ว่า Closing WebDriver... เพื่อให้ทราบว่ากำลังทำการปิดเบราว์เซอร์

ผลลัพธ์ที่คาดหวัง

ผลลัพธ์ที่ผ่านการทดสอบ (Pass):
หากผู้ใช้สมัครสมาชิกได้สำเร็จและเห็นข้อความยืนยันการสมัครจะมีการพิมพ์ข้อความว่า:
Test Result - Pass: User successfully registered

ผลลัพธ์ที่ล้มเหลว (Fail):
หากการสมัครสมาชิกไม่สำเร็จหรือไม่พบข้อความยืนยันการสมัคร, จะมีการพิมพ์ข้อความว่า:
Test Result - Fail: No success message detected
เมื่อทดสอบล้มเหลว, จะทำการบันทึกภาพหน้าจอที่แสดงข้อผิดพลาดเพื่อการตรวจสอบ

อธิบายองค์ประกอบต่างๆของ Code เบื้องต้น

1. Import Libraries และการตั้งค่าเบื้องต้น

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options

ส่วนนี้เป็นการนำเข้า libraries ที่จำเป็นสำหรับการทำ automation test
- webdriver ใช้สำหรับควบคุมเบราว์เซอร์
- By ใช้สำหรับระบุวิธีการค้นหา elements
- WebDriverWait และ EC ใช้สำหรับการรอให้ elements ปรากฏบนหน้าเว็บ
- Options ใช้สำหรับกำหนดค่าต่างๆของเบราว์เซอร์

2. Class setup

@classmethod
def setUpClass(cls):
    print("Initializing WebDriver...")
    edge_options = Options()
    edge_options.add_argument('--start-maximized')
    cls.driver = webdriver.Edge(options=edge_options)
    cls.wait = WebDriverWait(cls.driver, 20)

เป็นเมธอดที่จะทำงานก่อนที่จะเริ่มการทดสอบทั้งหมด
- ตั้งค่า WebDriver สำหรับ Microsoft Edge
- กำหนดให้เบราว์เซอร์เปิดแบบเต็มจอ
- สร้างตัวแปร wait ที่จะรอการโหลดเพจนานสูงสุด 20 วินาที

3. Data Setup

def setUp(self):
    self.test_data = {
        'url': 'http://45.136.236.146:8081/',
        'username': 'testuser19',
        'email': 'test19@example.com',
        'password': 'Test@123',
    }

เป็นการกำหนดข้อมูลที่จะใช้ในการทดสอบ
เก็บค่า URL, username, email และ password
จะทำงานก่อนการทดสอบแต่ละครั้ง

4. Test case หลัก

def test_signup_positive(self):
    # ขั้นตอนที่ 1: คลิกปุ่ม Sign Up
    signup_button = self.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Button--link')]//span[text()='Sign Up']"))
    )
    signup_button.click()

    # ขั้นตอนที่ 2: กรอกข้อมูลในฟอร์ม
    self._fill_form("username", self.test_data['username'])
    self._fill_form("email", self.test_data['email'])
    self._fill_form("password", self.test_data['password'])

    # ขั้นตอนที่ 3: ส่งฟอร์ม
    submit_button = self.wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.Button--primary[type='submit']"))
    )
    submit_button.click()

เป็นการทดสอบการสมัครสมาชิก
มีการรอหน้า browser จนกว่าจะเเสดง UI ต่างๆก่อนเเละกด Sign up
กรอกข้อมูลในฟอร์มทั้งหมดเเละส่งฟอร์มเพื่อทำการสมัครสมาชิก

5. Fill Help 

def _fill_form(self, field_name, value):
    try:
        field = self.wait.until(EC.element_to_be_clickable((By.NAME, field_name)))
        field.clear()
        field.send_keys(value)
    except Exception as e:
        print(f"Error filling '{field_name}' field: {e}")
        raise

เป็นเมธอดช่วยในการกรอกข้อมูลในฟอร์ม
โดยเริ่มจาดรอจนกว่าฟิลด์จะสามารถคลิกได้ก่อน
ลบข้อมูลเดิมในฟิลด์ (ถ้ามี)
กรอกข้อมูลใหม่ลงไป
จัดการข้อผิดพลาดที่อาจเกิดขึ้น        

ุ6. Teardown

@classmethod
def tearDownClass(cls):
    print("Closing WebDriver...")
    if cls.driver:
        cls.driver.quit()

เป็นส่วนที่ทำงานหลังจากการทดสอบทั้งหมดเสร็จสิ้น
โดยทำการปิดเบราว์เซอร์   



