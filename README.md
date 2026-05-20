# AI-Based Sign Language Detection System

Sistem Computer Vision berbasis Python yang mampu mendeteksi dan mengenali gesture tangan secara real-time menggunakan webcam, MediaPipe, dan OpenCV.

---

## Project Objective

Project ini dibuat untuk:
- Mempelajari implementasi Computer Vision dalam AI
- Mengembangkan sistem deteksi gesture tangan secara real-time
- Mengintegrasikan MediaPipe untuk hand tracking
- Membangun logic recognition berbasis landmark tangan

---

## Features

- Real-time hand detection menggunakan webcam
- Hand landmark tracking menggunakan MediaPipe
- Gesture recognition berbasis rule-based system
- Deteksi gesture:
  - ✊ FIST
  - ✋ OPEN HAND
  - ✌️ PEACE
  - ☝️ POINTING
  - 🤘 ROCK
  - 👍 YES (Thumbs Up)
- Visual output langsung di layar (live feedback)

---

## Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy

---

## How to Run

```bash
pip install -r requirements.txt
py main.py

## Screenshots

### Open Hand
![Open Hand](screenshots/open-hand.png)

### Peace
![Peace](screenshots/peace.png)

### Thumbs Up
![Thumbs Up](screenshots/thumbs-up.png)