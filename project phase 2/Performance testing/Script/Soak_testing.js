import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
    vus: 10, // จำนวนผู้ใช้งานพร้อมกัน
    duration: '5m', // ทดสอบต่อเนื่อง 5 นาที
};

export default function () {
    // Step 1: GET Homepage
    let res1 = http.get('http://45.136.236.146:8081/');
    check(res1, {
        'GET Homepage status is 200': (r) => r.status === 200,
    });
    sleep(1);

    // Step 2: คลิกที่ Search
    let res2 = http.get('http://45.136.236.146:8081');
    check(res2, {
        'Search page loaded': (r) => r.status === 200,
    });
    sleep(1);

    // Step 3: POST Log In
    let loginPayload = JSON.stringify({
        username: `user_${__VU}_${Date.now()}`,
        password: 'password123',
    });

    // Step 4: คลิกที่ Start a Discussion
    let res5 = http.get('http://45.136.236.146:8081/');
    check(res5, {
        'Start a Discussion page loaded': (r) => r.status === 200,
    });
    sleep(1);

    // Step 5: คลิกที่ All Discussions
    let res6 = http.get('http://45.136.236.146:8081/');
    check(res6, {
        'All Discussions page loaded': (r) => r.status === 200,
    });
    sleep(1);

    // Step 6: คลิกที่ Tags
    let res7 = http.get('http://45.136.236.146:8081/tags');
    check(res7, {
        'Tags page loaded': (r) => r.status === 200,
    });
    sleep(1);

}
