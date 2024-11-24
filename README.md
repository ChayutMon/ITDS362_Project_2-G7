# ITDS362_Project_2-G7















#  UI & system testing




# Test Case Login-1 Test caseใช้ในการเช็ครูปแบบการinputต่างๆของการ Login โดยแบ่งออก 5 Test ดังนี้

Test Login with Incorrect Username & Password input
Status: Pass
ระยะเวลารวมในการทดสอบ: 9.939 วินาที Keyword ที่ใช้งาน:
Open browser: สำหรับเปิด Browser
Sleep 2s ทำการตั้ง Delay 2 วิ
Click Button: Click ปุ่มตามที่กำหนด
Sleep 2s ทำการตั้ง Delay 2 วิ
Input Text: สำหรับการ กรอกข้อมูล
Input Text: สำหรับการ กรอกข้อมูล
Click Button: Click ปุ่มตามที่กำหนด
Sleep 2s ทำการตั้ง Delay 2 วิ
Close Browser สำหรับ ปิด Browser ขั้นตอนการทำงาน:
เปิด Browser เพื่อเข้าสู่ Website

Click login

กรอก Usernameที่ไม่ถูกต้อง และ รหัสผ่านที่ถูกต้อง

เข้าสู่ระบบไม่สำเร็จ

Test Login with Incorrect Email & Password input

Status: Pass
ระยะเวลารวมในการทดสอบ: 10.011 วินาที Keyword ที่ใช้งาน:
Open browser: สำหรับเปิด Browser
Sleep 2s ทำการตั้ง Delay 2 วิ
Click Button: Click ปุ่มตามที่กำหนด
Sleep 2s ทำการตั้ง Delay 2 วิ
Input Text: สำหรับการ กรอกข้อมูล
Input Text: สำหรับการ กรอกข้อมูล
Click Button: Click ปุ่มตามที่กำหนด
Sleep 2s ทำการตั้ง Delay 2 วิ
Close Browser สำหรับ ปิด Browser ขั้นตอนการทำงาน:
เปิด Browser เพื่อเข้าสู่ Website

Click login

กรอก Email ที่ไม่ถูกต้อง และ รหัสผ่านที่ถูกต้อง

เข้าสู่ระบบไม่สำเร็จ

Test Login with Correct Username & Incorrect password input

Status: Pass
ระยะเวลารวมในการทดสอบ: 9.955 วินาที Keyword ที่ใช้งาน:
Open browser: สำหรับเปิด Browser
Sleep 2s ทำการตั้ง Delay 2 วิ
Click Button: Click ปุ่มตามที่กำหนด
Sleep 2s ทำการตั้ง Delay 2 วิ
Input Text: สำหรับการ กรอกข้อมูล
Input Text: สำหรับการ กรอกข้อมูล
Click Button: Click ปุ่มตามที่กำหนด
Sleep 2s ทำการตั้ง Delay 2 วิ
Close Browser สำหรับ ปิด Browser ขั้นตอนการทำงาน:
เปิด Browser เพื่อเข้าสู่ Website

Click login

กรอก Username ที่ถูกต้อง และ รหัสผ่านที่ไม่ถูกต้อง

เข้าสู่ระบบไม่สำเร็จ

Test Login with Correct Email & Incorrect password input

Status: Pass
ระยะเวลารวมในการทดสอบ: 9.988 วินาที Keyword ที่ใช้งาน:
Open browser: สำหรับเปิด Browser
Sleep 2s ทำการตั้ง Delay 2 วิ
Click Button: Click ปุ่มตามที่กำหนด
Sleep 2s ทำการตั้ง Delay 2 วิ
Input Text: สำหรับการ กรอกข้อมูล
Input Text: สำหรับการ กรอกข้อมูล
Click Button: Click ปุ่มตามที่กำหนด
Sleep 2s ทำการตั้ง Delay 2 วิ
Close Browser สำหรับ ปิด Browser ขั้นตอนการทำงาน:
เปิด Browser เพื่อเข้าสู่ Website

Click login

กรอก Email ที่ถูกต้อง และ รหัสผ่านที่ไม่ถูกต้อง

เข้าสู่ระบบไม่สำเร็จ

Test Login with Incorrect Email & Incorrect password input

Status: Pass
ระยะเวลารวมในการทดสอบ: 9.953 วินาที Keyword ที่ใช้งาน:
Open browser: สำหรับเปิด Browser
Sleep 2s ทำการตั้ง Delay 2 วิ
Click Button: Click ปุ่มตามที่กำหนด
Sleep 2s ทำการตั้ง Delay 2 วิ
Input Text: สำหรับการ กรอกข้อมูล
Input Text: สำหรับการ กรอกข้อมูล
Click Button: Click ปุ่มตามที่กำหนด
Sleep 2s ทำการตั้ง Delay 2 วิ
Close Browser สำหรับ ปิด Browser ขั้นตอนการทำงาน:
เปิด Browser เพื่อเข้าสู่ Website
Click login
กรอก Email ที่ไม่ถูกต้อง และ รหัสผ่านที่ไม่ถูกต้อง
เข้าสู่ระบบไม่สำเร็จ





//////////////////////////////////////////////////////////////////////////////////////////




# Test Case Post-1 Test case นี้อ้างอิงจาก Systems Test ก่อนหน้า โดยมีการแบ่งเป็น 2 Test ใหญ่ๆ ดังนี้

Test Login with valid Account
Status: Pass
ระยะเวลารวมในการทดสอบ: 8.27 วินาที Keyword ที่ใช้งาน:
Open browser: สำหรับเปิด Browser
Wait until element Is Visible: รอให้ Element ใน Website ทำการ Render
Click Button: Click ปุ่มตามที่กำหนด
Input Text: สำหรับการ กรอกข้อมูล
Element Text should be: สำหรับ check ว่า Element ที่เราต้องการ ควรเป็นตาที่กำหนด
Close Browser สำหรับ ปิด Browser ขั้นตอนการทำงาน:
เปิด Browser เพื่อเข้าสู่ Website

Click login

กรอก Username และ รหัสผ่านที่ถูกต้อง

เข้าสู่ระบบสำเร็จ

Test Post discussion with valid account

Status: Pass
ระยะเวลาในการทดสอบ: 9.378 วินาที Keyword ที่ใช้งาน:
Open browser: สำหรับเปิด Browser
Wait until element Is Visible: รอให้ Element ใน Website ทำการ Render
Wait until element is not visible: เพื่อเช็คให้มั่นใจว่าปุ่มต้องไม่มีตามที่กำหนด
Click Button: Click ปุ่มตามที่กำหนด
Click Element: Click Element ในกรณีที่ Element ไม่ใช่ Button แต่สามารถกดได้
Input Text: สำหรับการ กรอกข้อมูล
Element Text should be: สำหรับ check ว่า Element ที่เราต้องการ ควรเป็นตาที่กำหนด
Close Browser สำหรับ ปิด Browser ขั้นตอนการทำงาน:
เปิด Browser เพื่อเข้าสู่ Website
Click login
กรอก Username และ รหัสผ่านที่ถูกต้อง
เข้าสู่ระบบสำเร็จ
กด Start a discussion
กรอก Discussion Header และ เขียนรายระเอียด Post
กด Post
เลือก Tag ของ Post แล้วกด Ok
ทำการ Post ได้สำเร็จ










# Automated UI Testing: Sign up Testing

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

















# Performance Testing




# //////////////////Avg_result/////////////

X /t/general status is 200

L 2% - v 1423 / X 5409

X /t/general response time < 300ms

L 81% - v 45166 / X 10266

X /t/general?sort=top status is 200

L 2% - ¥ 1132 / X 54101

X /t/general?sort=top response time < 300ms
82% — v 45373 / X 9860

X /t/general?sort=newest status is 200

L 1% - ¥ 1055 / xX 53974

X /t/general?sort=newest response time < 300ms
L 82% - v 45352 / X 9677

X /t/general?sortzoldest status is 200

L 1% - ¥ 983 / X 53817

X /t/general?sort=oldest response time < 300ms
L 83% - v 45536 / X 9264

42.18% 186020 out of 440988
<1 188 MB 369 kB/s
1 22.MB 43 kB/s

checks.
data_received

http_req_blocked..... avg=40.88ms  min=es med=0s p(90)=0s p(95)=05
http_req_connecting. ... avg=40.88ms_min=0s med=0s p(90)=0s p(95)=2s
http_req_duration. avg=997.6ms_ min=0s med=39.43ms max=im@s _ p(9@)=582.39ms p(95)=855.13ms

{ expected_respons: avg=24.15s 80.03ms met p(90)=37.68s p(95)=45.25s
http_req_failed...... 97.91% 215901 out of 220494
http_req_receiving... avg=212.52us minses med=0s p(98)=418.57us p(95)=734.4us

http_req_sending. . -34us  min=@s med=0s p(90)=0s p(95)=0s
http_req_tls_handshaking. avg=0s min=0s med=0s max=0s p(90)=0s p(95)=0s
http_req_waiting. . avg=997.39ms min=2s med=39.37ms max=im@s _ p(9@)=582.36ms p(95)=854.84ms
http_reqs....... 220494 432.3404/s

iteration_duration 2 avge7.72s p(9@)=16.08s  p(95)=1m1s
iterations 54783 107.417454/s

a2 =1 max=1500
<1 1588 min=1500 max=1500

running (8m30.@s), 0000/1500 VUs, 54783 complete and 667 interrupted iterations
default / @000/1500 VUs 8m@s
----------------------------------------------------------------------------------------------

// to run test "k6 run Average_load_test.js"
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////








# //////////////////Stress_testing/////////////



✗ /t/general status is 200
      ↳  3% — ✓ 1924 / ✗ 48393
     ✗ /t/general response time < 200
      ↳  85% — ✓ 43160 / ✗ 7157
     ✗ Main page status is 200
      ↳  3% — ✓ 1745 / ✗ 48445
     ✗ Main page response time < 200ms
      ↳  86% — ✓ 43360 / ✗ 6830
     ✗ /t/general?sort=top status is 200
      ↳  3% — ✓ 1723 / ✗ 48300
     ✗ /t/general?sort=top response time < 200
      ↳  86% — ✓ 43224 / ✗ 6799
     ✗ /t/general?sort=newest status is 200
      ↳  3% — ✓ 1662 / ✗ 48176
     ✗ /t/general?sort=newest response time < 200
      ↳  86% — ✓ 42998 / ✗ 6840
     ✗ /t/general?sort=oldest status is 200
      ↳  3% — ✓ 1588 / ✗ 48066
     ✗ /t/general?sort=oldest response time < 200
      ↳  86% — ✓ 42931 / ✗ 6723
checks.........................: 44.85% 224315 out of 500044
     data_received..................: 305 MB 678 kB/s
     data_sent......................: 25 MB  56 kB/s
     http_req_blocked...............: avg=28.23ms  min=0s      med=0s      max=15.05s   p(90)=0s       p(95)=0s
     http_req_connecting............: avg=28.22ms  min=0s      med=0s      max=15.05s   p(90)=0s       p(95)=0s
     http_req_duration..............: avg=814.05ms min=0s      med=32.92ms max=51.69s   p(90)=229.93ms p(95)=310.17ms
       { expected_response:true }...: avg=21.41s   min=72.71ms med=25.94s  max=51.69s   p(90)=29.29s   p(95)=29.83s
     http_req_failed................: 96.54% 241380 out of 250022
     http_req_receiving.............: avg=302.06µs min=0s      med=0s      max=100.57ms p(90)=489.1µs  p(95)=853.8µs
     http_req_sending...............: avg=4.06µs   min=0s      med=0s      max=6.01ms   p(90)=0s       p(95)=0s
     http_req_tls_handshaking.......: avg=0s       min=0s      med=0s      max=0s       p(90)=0s       p(95)=0s
     http_req_waiting...............: avg=813.74ms min=0s      med=32.86ms max=51.69s   p(90)=229.88ms p(95)=310.17ms
     http_reqs......................: 250022 555.603967/s
     iteration_duration.............: avg=6.99s    min=1.01s   med=1.29s   max=2m23s    p(90)=27.72s   p(95)=43.09s
     iterations.....................: 49644  110.319905/s
     vus............................: 2      min=2                max=1500
     vus_max........................: 1500   min=1500             max=1500


running (7m30.0s), 0000/1500 VUs, 49644 complete and 674 interrupted iterations
default ✓ [======================================] 0000/1500 VUs  7m0s
-------------------------------------------------------------------------------------------------------

// to run test "k6 run Stress_testing.js"
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

















# รายงานผลการทดสอบ Soak Testing

## รายละเอียดการทดสอบ
การทดสอบ Soak Testing ถูกออกแบบมาเพื่อตรวจสอบความสามารถของระบบในการรองรับโหลดที่ยาวนานและตรวจสอบว่าระบบยังคงทำงานได้โดยไม่มีปัญหา เช่น การใช้งานหน่วยความจำที่เพิ่มขึ้นจนเกิดการล้มเหลวหรือการทำงานช้าลง

### การตั้งค่าการทดสอบ
- **จำนวนผู้ใช้จำลอง (Virtual Users - VUs)**: สูงสุด 10 คน
- **ระยะเวลาการทดสอบ**: 5 นาที + Graceful Stop 30 วินาที
- **จำนวน Iterations**: 528 ครั้ง (เฉลี่ย 1.73 iterations ต่อวินาที)
- **จำนวนคำขอ HTTP ทั้งหมด**: 2,640 คำขอ (เฉลี่ย 8.66 คำขอ/วินาที)

---

## ผลลัพธ์
- **สถานะการตอบสนอง**: หน้าเว็บทุกหน้าตอบสนองสำเร็จ (สถานะ 200)
- **คำขอ HTTP ล้มเหลว**: ไม่มีคำขอล้มเหลว (0%)

---

## การวิเคราะห์ประสิทธิภาพ (ตาม K6 Metrics)

### 1. ความเร็วในการตอบสนอง (Response Time)
- **ค่าเฉลี่ย (http_req_duration)**: 148.24 ms
- **ช่วงเวลาตอบสนอง**:
  - เวลาต่ำสุด: 46.1 ms
  - เวลาสูงสุด: 3.49 วินาที
  - P90 (90% ของคำขอ): 195.84 ms
  - P95 (95% ของคำขอ): 307.44 ms
- **การวิเคราะห์**: 
  - ระบบตอบสนองรวดเร็วในภาพรวม โดยคำขอส่วนใหญ่ใช้เวลาน้อยกว่า 200 ms 
  - มีคำขอบางส่วนที่ใช้เวลานานถึง 3.49 วินาที ซึ่งอาจเกิดจากข้อจำกัดในช่วง Peak Load หรือความล่าช้าจากเครือข่าย

### 2. เวลารอการประมวลผล (Waiting Time)
- **ค่าเฉลี่ย (http_req_waiting)**: 139.07 ms
- **ช่วงเวลา**:
  - เวลาต่ำสุด: 45.32 ms
  - เวลาสูงสุด: 3.48 วินาที
- **การวิเคราะห์**:
  - เวลารอประมวลผลใกล้เคียงกับเวลาตอบสนองรวม แสดงว่าระบบ Backend เป็นปัจจัยหลักของเวลาตอบสนอง

### 3. การเชื่อมต่อและการส่งข้อมูล
- **การเชื่อมต่อ (http_req_connecting)**: 
  - ค่าเฉลี่ย: 142.14 µs (เร็วมาก)
- **การส่งข้อมูล (http_req_sending)**: 
  - ค่าเฉลี่ย: 8.69 µs
- **การรับข้อมูล (http_req_receiving)**:
  - ค่าเฉลี่ย: 9.16 ms
- **การวิเคราะห์**:
  - กระบวนการส่งและรับข้อมูลมีประสิทธิภาพสูง ไม่มีคอขวดในส่วนของเครือข่ายหรือการเชื่อมต่อ

### 4. การใช้งานทรัพยากร
- **ข้อมูลที่รับ (data_received)**: 60 MB (เฉลี่ย 197 kB/s)
- **ข้อมูลที่ส่ง (data_sent)**: 364 kB (เฉลี่ย 1.2 kB/s)
- **จำนวน Virtual Users (vus)**: คงที่ระหว่าง 6-10 ตลอดการทดสอบ

---

## ข้อสรุป
1. **Performance ของระบบ**:
   - ค่าเฉลี่ยของเวลาในการตอบสนองอยู่ที่ **148.24 ms** ซึ่งถือว่าดีสำหรับแอปพลิเคชันทั่วไป
   - ไม่มีคำขอที่ล้มเหลว แสดงถึงความเสถียรของระบบในระยะเวลานาน
   - ระบบสามารถรองรับการโหลดที่ระดับสูง (10 VUs) ได้อย่างมีประสิทธิภาพ
2. **ข้อแนะนำ**:
   - ตรวจสอบคำขอที่ใช้เวลานาน (สูงสุด 3.49 วินาที) เพื่อลดความล่าช้าที่อาจเกิดจากข้อจำกัดในช่วง Peak Load
   - ทดสอบเพิ่มเติมเพื่อดูผลลัพธ์เมื่อเพิ่มจำนวนผู้ใช้จำลองหรือขยายระยะเวลาทดสอบ
  


















# รายงานผลการทดสอบ Spike Testing

## สรุปการทดสอบ
เราได้ทดสอบระบบโดยจำลองการใช้งานของผู้ใช้งานหลายระดับ (Spike Testing) เพื่อดูว่าเมื่อมีคนใช้ระบบเพิ่มขึ้นและลดลง ระบบตอบสนองอย่างไร โดยใช้เครื่องมือ **K6** ในการทดสอบครั้งนี้

### สิ่งที่เราทดสอบ
- **เว็บไซต์ที่ทดสอบ**: `http://45.136.236.146:8081/`
- **จำนวนผู้ใช้งานจำลอง**:
  - เริ่มจาก 10 คน เพิ่มขึ้นเป็น 100 คน และลดลงจนเหลือ 0 คน
- **สิ่งที่วัด**:
  - ความเร็วในการตอบสนอง (Response Time)
  - ปริมาณข้อมูลที่ระบบรับและส่ง
  - สถานะการตอบกลับของระบบ (เช่น 200, 500)

---

## ผลการทดสอบ

### 1. Response Time
- **คำร้องที่ตอบสนองเร็วกว่ามาตรฐาน (< 2000ms)**:
  - General Tab: 39% ผ่าน / 61% ไม่ผ่าน
  - Top Tab: 41% ผ่าน / 59% ไม่ผ่าน
  - Newest Tab: 40% ผ่าน / 60% ไม่ผ่าน
  - Oldest Tab: 40% ผ่าน / 60% ไม่ผ่าน
- **ค่าตอบสนองเฉลี่ย**: 2.78 วินาที
- **ค่าตอบสนองสูงสุด**: 23.91 วินาที
- **เปอร์เซ็นไทล์**:
  - p(90): 4.57 วินาที
  - p(95): 4.93 วินาที

สรุป: ระบบมี Response Time ที่เกินเกณฑ์มาตรฐานในกว่า 59% ของคำร้องขอ

---

### 2. Iteration Duration (เวลาทำงานต่อรอบ)
- **ค่าตอบสนองเฉลี่ย**: 12.12 วินาที
- **ค่าสูงสุด**: 46.37 วินาที

สรุป: ระยะเวลาในแต่ละรอบค่อนข้างนาน อาจเกิดจากปัญหาการจัดการคำขอที่ใช้เวลาสูง

---

### 3. การรับส่งข้อมูล
- **ข้อมูลที่รับ**: 175 MB (~485 kB/s)
- **ข้อมูลที่ส่ง**: 985 kB (~2.7 kB/s)

สรุป: ระบบสามารถจัดการข้อมูลจำนวนมากได้ แต่ยังมีปัญหาเรื่องความเร็วในการตอบสนอง

---

### สถานะ HTTP
- **สถานะการตอบกลับ**: 100% ของคำร้องขอได้รับ HTTP 200 (สำเร็จ)

---

## ปัญหาที่พบ
1. **Response Time สูงเกินเกณฑ์มาตรฐาน**:
   - เวลาตอบสนองเฉลี่ย 2.78 วินาที เกินเกณฑ์มาตรฐาน (< 2 วินาที)
   - ค่าสูงสุดที่พบ 23.91 วินาที
   - สาเหตุที่อาจเป็นไปได้:
     - Server Load: เซิร์ฟเวอร์ไม่สามารถรองรับผู้ใช้งานพร้อมกันจำนวนมาก
     - Database Query: การเรียกใช้งานฐานข้อมูลที่ใช้เวลานาน
     - Network Latency: ปัญหาความล่าช้าของเครือข่าย

---

## สิ่งที่ควรปรับปรุง
1. **เพิ่มประสิทธิภาพเซิร์ฟเวอร์**:
   - เพิ่มทรัพยากร (CPU, RAM)
   - ใช้ Load Balancer ช่วยกระจายการประมวลผล

2. **ปรับปรุงฐานข้อมูล**:
   - ตรวจสอบและปรับปรุง Query ให้เหมาะสม
   - ใช้ระบบ Caching สำหรับข้อมูลที่เรียกใช้บ่อย

3. **ลด Network Latency**:
   - ตรวจสอบการตั้งค่าเครือข่ายและปรับปรุง Bandwidth

4. **วิเคราะห์เพิ่มเติม**:
   - ทดสอบระบบด้วย Stress Testing เพื่อดูความสามารถสูงสุดของระบบ
   - ใช้เครื่องมือ Monitoring เพื่อตรวจหาคอขวด (Bottleneck)



