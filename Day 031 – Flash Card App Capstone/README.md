# Flash Card App 📚

## 📌 Overview
A GUI-based flashcard application designed to help users learn vocabulary using spaced repetition techniques.  
The app displays a word, flips it after a delay, and shows its meaning.

---

## 🎯 Features
- Flashcard flipping after timer
- Random word selection
- Progress tracking (removes known words)
- Data persistence

---

## 🧱 System Architecture
- UI Layer → Tkinter interface
- Data Layer → CSV file (word pairs)
- Logic Layer → Timer-based card switching

---

## 🧠 Concepts Used
- Tkinter (GUI)
- Pandas (data handling)
- File persistence
- Event scheduling (`after()` method)

---

## ⚙️ Workflow
1. Load dataset from CSV
2. Display random word
3. Flip card after delay
4. If user knows word → remove from dataset

---

## ▶️ How to Run
```bash
python main.py
