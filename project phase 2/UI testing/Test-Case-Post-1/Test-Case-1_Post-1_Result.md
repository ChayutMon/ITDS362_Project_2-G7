Test Case Post-1
	Test case นี้อ้างอิงจาก Systems Test ก่อนหน้า โดยมีการแบ่งเป็น 2 Test ใหญ่ๆ ดังนี้
 
1.	Test Login with valid Account
-	Status: Pass
-	ระยะเวลารวมในการทดสอบ: 8.27 วินาที
Keyword ที่ใช้งาน:
-	Open browser: สำหรับเปิด Browser
-	Wait until element Is Visible: รอให้ Element ใน Website ทำการ Render
-	Click Button: Click ปุ่มตามที่กำหนด
-	Input Text: สำหรับการ กรอกข้อมูล
-	Element Text should be: สำหรับ check ว่า Element ที่เราต้องการ ควรเป็นตาที่กำหนด
-	Close Browser สำหรับ ปิด Browser
ขั้นตอนการทำงาน:
1.	เปิด Browser เพื่อเข้าสู่ Website
2.	Click login
3.	กรอก Username และ รหัสผ่านที่ถูกต้อง
4.	เข้าสู่ระบบสำเร็จ



 
2.	Test Post discussion with valid account
-	Status: Pass
-	ระยะเวลาในการทดสอบ: 9.378 วินาที
Keyword ที่ใช้งาน:
-	Open browser: สำหรับเปิด Browser
-	Wait until element Is Visible: รอให้ Element ใน Website ทำการ Render
-	Wait until element is not visible: เพื่อเช็คให้มั่นใจว่าปุ่มต้องไม่มีตามที่กำหนด
-	Click Button: Click ปุ่มตามที่กำหนด
-	Click Element: Click Element ในกรณีที่ Element ไม่ใช่ Button แต่สามารถกดได้
-	Input Text: สำหรับการ กรอกข้อมูล
-	Element Text should be: สำหรับ check ว่า Element ที่เราต้องการ ควรเป็นตาที่กำหนด
-	Close Browser สำหรับ ปิด Browser
ขั้นตอนการทำงาน:
1.	เปิด Browser เพื่อเข้าสู่ Website
2.	Click login
3.	กรอก Username และ รหัสผ่านที่ถูกต้อง
4.	เข้าสู่ระบบสำเร็จ
5.	กด Start a discussion
6.	กรอก Discussion Header และ เขียนรายระเอียด Post
7.	กด Post
8.	เลือก Tag ของ Post แล้วกด Ok
9.	ทำการ Post ได้สำเร็จ
