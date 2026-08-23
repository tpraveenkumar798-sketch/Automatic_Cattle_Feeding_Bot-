# 🐄 Automatic Cattle Feeding Bot

An AI-based automatic cattle feeding bot developed as a smart farming solution to reduce manual effort and provide consistent feeding through autonomous cattle detection and feed dispensing.

## 📌 Overview

The Automatic Cattle Feeding Bot uses a **Raspberry Pi 5**, **USB webcam**, **OpenCV**, and a **TensorFlow Lite model** trained using **Teachable Machine** to detect cattle and automatically dispense feed.

The bot moves autonomously, detects cattle using the camera, stops when a cattle is detected with sufficient confidence, operates the feeding mechanism using a servo motor, and continues moving to the next cattle.

After feeding the first four cattle, the bot automatically returns to its starting position.

## 🎯 Objectives

- Reduce manual effort involved in cattle feeding.
- Automate the cattle detection and feeding process.
- Provide consistent and controlled feed dispensing.
- Demonstrate the use of AI and computer vision in smart farming.
- Develop a low-cost autonomous agricultural robot.

## ✨ Key Features

- 🐄 AI-based cattle detection
- 📷 Camera-based computer vision
- 🤖 Autonomous movement
- 🍚 Automatic feed dispensing
- 🔄 Automatic return to starting position
- 🧠 TensorFlow Lite inference
- 🖥️ Raspberry Pi-based processing

## 🛠️ Hardware Components

- Raspberry Pi 5 (8 GB RAM)
- USB Webcam
- L298N Motor Driver
- DC Motors
- Servo Motor
- Robot chassis
- Feeding mechanism
- Power supply

## 💻 Software & Technologies

- Python
- OpenCV
- NumPy
- TensorFlow Lite
- Teachable Machine
- GPIO Zero
- Raspberry Pi OS

## ⚙️ Working Principle

1. The Raspberry Pi starts the robot and initializes the motors, servo motor, camera, and TensorFlow Lite model.
2. The USB webcam continuously captures frames.
3. OpenCV resizes and preprocesses each frame.
4. The TensorFlow Lite model analyzes the frame and predicts whether a cattle is detected.
5. When the detection confidence exceeds the defined threshold, the robot stops.
6. The servo motor operates the feeding mechanism and dispenses feed.
7. The robot resumes forward movement.
8. This process continues until four cattle have been fed.
9. The robot reverses for the corresponding duration and returns to the starting position.

## 🧠 AI Model

The cattle detection model was developed using **Teachable Machine** and exported in **TensorFlow Lite** format for deployment on the Raspberry Pi.

The model is used for lightweight, real-time inference suitable for Raspberry Pi-based applications.

## 📁 Project Structure

```text
Automatic-Cattle-Feeding-Bot/
│
├── code/
│   └── main.py
│
├── model/
│   └── cattle_model.zip
│
├── images/
│   ├── project photos
│   ├── block diagram
│   └── flowchart
│
├── docs/
│   └── Report.pdf
|
├── requirements.txt
└── README.md