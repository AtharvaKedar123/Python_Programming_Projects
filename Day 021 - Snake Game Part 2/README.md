# Snake Game (Part 2) 🐍

## 📌 Overview
A fully functional Snake Game built using Python's Turtle graphics module.  
This version introduces dynamic gameplay including food consumption, snake growth, collision detection, and score tracking.

---

## 🎯 Features
- Real-time snake movement
- Food spawning at random locations
- Snake growth mechanism
- Collision detection (wall & self)
- Score tracking system

---

## 🧱 System Design (OOP Structure)
- `Snake` → Controls movement and growth
- `Food` → Handles food placement and respawning
- `Scoreboard` → Tracks and displays score

---

## 🧠 Concepts Used
- Object-Oriented Programming (OOP)
- Game loop logic
- Event handling (keyboard input)
- Collision detection algorithms

---

## ⚙️ How It Works
1. Snake moves continuously on screen
2. When snake eats food:
   - Score increases
   - Snake length increases
3. Game ends when:
   - Snake hits wall
   - Snake collides with itself

---

## ▶️ How to Run
```bash
python main.py
