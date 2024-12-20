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

---