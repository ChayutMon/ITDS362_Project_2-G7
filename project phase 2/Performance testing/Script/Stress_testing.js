import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '1m', target: 100 }, // Ramp-up จำนวนผู้ใช้จาก 0 -> 100 ใน 1 นาที
    { duration: '2m', target: 1000 }, // เพิ่มจำนวนผู้ใช้ขึ้นไปที่ 1000 ใน 2 นาที
    { duration: '3m', target: 1500 }, // Stress Test: จำนวนผู้ใช้สูงสุด 1500 คน ใน 3 นาที
    { duration: '1m', target: 1500 }, // ระยะเวลาที่คงที่ที่ 1500 ผู้ใช้
    { duration: '1m', target: 0 },    // Ramp-down จำนวนผู้ใช้ลดลงเป็น 0 ใน 1 นาที
  ],
};

export default function () {
  // ทดสอบ /t/general
  let generalRes = http.get('http://45.136.236.146:8081/t/general');
  check(generalRes, {
    '/t/general status is 200': (r) => r.status === 200,
    '/t/general response time < 300ms': (r) => r.timings.duration < 300,
  });

  // ทดสอบ Endpoint หลัก
  let mainRes = http.get('http://45.136.236.146:8081/');
  check(mainRes, {
    'Main page status is 200': (r) => r.status === 200,
    'Main page response time < 200ms': (r) => r.timings.duration < 200,
  });

  // ทดสอบ /t/general?sort=top
  let sortTopRes = http.get('http://45.136.236.146:8081/t/general?sort=top');
  check(sortTopRes, {
    '/t/general?sort=top status is 200': (r) => r.status === 200,
    '/t/general?sort=top response time < 300ms': (r) => r.timings.duration < 300,
  });

  // ทดสอบ /t/general?sort=newest
  let sortNewestRes = http.get('http://45.136.236.146:8081/t/general?sort=newest');
  check(sortNewestRes, {
    '/t/general?sort=newest status is 200': (r) => r.status === 200,
    '/t/general?sort=newest response time < 300ms': (r) => r.timings.duration < 300,
  });

  // ทดสอบ /t/general?sort=oldest
  let sortOldestRes = http.get('http://45.136.236.146:8081/t/general?sort=oldest');
  check(sortOldestRes, {
    '/t/general?sort=oldest status is 200': (r) => r.status === 200,
    '/t/general?sort=oldest response time < 300ms': (r) => r.timings.duration < 300,
  });

  sleep(1); 
}
//k6 run Stress_testing.js to run test