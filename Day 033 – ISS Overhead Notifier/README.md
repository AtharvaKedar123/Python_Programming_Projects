# ISS Overhead Notifier 🛰

## 📌 Overview
Tracks the International Space Station (ISS) location and sends a notification when it is visible overhead.

---

## 🎯 Features
- Real-time ISS tracking
- Location comparison
- Email notification

---

## 🧱 System Architecture
- API Layer → ISS & Sunrise-Sunset APIs
- Logic Layer → Visibility calculation
- Notification Layer → Email

---

## 🧠 Concepts Used
- API requests (requests module)
- JSON parsing
- Time comparison

---

## ⚙️ Workflow
1. Fetch ISS coordinates
2. Compare with user location
3. Check if it’s night
4. Send notification if visible

---

## 📍 Learning Outcome
- Integrating multiple APIs
- Building real-time monitoring systems
