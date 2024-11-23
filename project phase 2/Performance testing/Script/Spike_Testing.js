import http from 'k6/http';
import { check, sleep, group } from 'k6';

// URL สำหรับการทดสอบ
const baseUrl = 'http://45.136.236.146:8081/';

// กำหนดการเพิ่มและลดจำนวนผู้ใช้งานใน Spike Testing
export const options = {
  stages: [
    { duration: '1m', target: 10 },   // เพิ่มผู้ใช้งานจำลองอย่างช้า ๆ
    { duration: '1m', target: 100 }, // เพิ่มผู้ใช้งานเป็น 100 คนในระยะเวลานานขึ้น
    { duration: '2m', target: 100 }, // คงไว้ที่ 100 คนเป็นเวลา 2 นาที
    { duration: '1m', target: 10 },  // ลดผู้ใช้งานกลับมาที่ 10 คน
    { duration: '1m', target: 0 },   // ลดลงเป็น 0
  ],
};

export default function () {
  group('Spike Testing for Tabs', () => {
    // เข้าใช้งานแท็บ General
    const generalResponse = http.get(baseUrl);
    check(generalResponse, {
      'General page status is 200': (r) => r.status === 200,
      'General response time is < 2000ms': (r) => r.timings.duration < 2000, // เปลี่ยนเป็น 2000ms
    });

    // เข้าใช้งานแท็บ Top
    const topResponse = http.get(`${baseUrl}?sort=top`);
    check(topResponse, {
      'Top tab status is 200': (r) => r.status === 200,
      'Top tab response time is < 2000ms': (r) => r.timings.duration < 2000, // เปลี่ยนเป็น 2000ms
    });

    // เข้าใช้งานแท็บ Newest
    const newestResponse = http.get(`${baseUrl}?sort=newest`);
    check(newestResponse, {
      'Newest tab status is 200': (r) => r.status === 200,
      'Newest tab response time is < 2000ms': (r) => r.timings.duration < 2000, // เปลี่ยนเป็น 2000ms
    });

    // เข้าใช้งานแท็บ Oldest
    const oldestResponse = http.get(`${baseUrl}?sort=oldest`);
    check(oldestResponse, {
      'Oldest tab status is 200': (r) => r.status === 200,
      'Oldest tab response time is < 2000ms': (r) => r.timings.duration < 2000, // เปลี่ยนเป็น 2000ms
    });
  });

  // หน่วงเวลาเล็กน้อยเพื่อจำลองการใช้งานจริง
  sleep(1);
}
