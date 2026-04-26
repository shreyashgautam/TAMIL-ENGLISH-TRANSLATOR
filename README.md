<div align="center">

<br>

# 🎙️ Tamil ↔ English Speech Translator
### *Speak in Tamil. Hear it in English. And back again.*

> Real-time speech recognition · Bidirectional translation · Voice output · Zero friction

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SpeechRecognition](https://img.shields.io/badge/SpeechRecognition-FF6B6B?style=flat-square&logo=googlepodcasts&logoColor=white)
![gTTS](https://img.shields.io/badge/gTTS-4285F4?style=flat-square&logo=google&logoColor=white)
![Googletrans](https://img.shields.io/badge/Googletrans-34A853?style=flat-square&logo=googletranslate&logoColor=white)

<br>

</div>

---

## 👨‍💻 Developed By

<div align="center">

| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Contribution |
|:----:|:----:|
| **Shreyash Gautam** | Core development · Tamil → English pipeline |
| **Dipsita Rout** | English → Tamil feature · Testing & QA |

</div>

---

## 🧠 About the Project

**Tamil ↔ English Speech Translator** is a real-time, bidirectional speech translation tool built in Python. Speak into your microphone in Tamil and get English output — or flip it, speak English and hear Tamil back. No cloud dashboards, no complex setup — just run the script and start talking.

```
🎤 Speak  →  👂 Recognize  →  🌐 Translate  →  🔊 Play Back
```

Built to bridge the language gap between Tamil and English speakers through simple, accessible voice technology.

---

## ✨ Features

### 🔁 Bidirectional Translation
Full support for both directions — Tamil → English (`TamToEng.py`) and English → Tamil (`EngToTam.py`). Switch between modes based on what you need.

### 🎤 Real-Time Speech Recognition
Powered by the `SpeechRecognition` library — listens to your microphone and transcribes your speech on the fly.

### 🌐 Accurate Translation
Uses `googletrans` and `pygoogletranslation` for high-quality, context-aware translation between Tamil and English.

### 🔊 Voice Output
Translated text is converted back to speech using `gTTS` (Google Text-to-Speech) and played back via `playsound` — a full speech-to-speech experience.

### 🖥️ Cross-Platform
Runs on Windows, macOS, and Linux — anywhere Python runs.

---

## 🛠️ Tech Stack

| Library | Purpose |
|:--------|:--------|
| `SpeechRecognition` | Microphone input & speech-to-text |
| `googletrans` / `pygoogletranslation` | Tamil ↔ English translation |
| `gTTS` | Text-to-speech output |
| `playsound` | Audio playback |
| `translate` | Supplementary translation support |

---

## 📁 Project Structure

```
TAMIL-ENGLISH-TRANSLATOR/
├── TamToEng.py      ← Tamil speech → English text/speech
├── EngToTam.py      ← English speech → Tamil text/speech
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/shreyashgautam/TAMIL-ENGLISH-TRANSLATOR.git
cd TAMIL-ENGLISH-TRANSLATOR
```

### 2. Install Dependencies

```bash
pip install SpeechRecognition googletrans==4.0.0-rc1 pygoogletranslation gTTS playsound translate
```

### 3. Run the Translator

**Tamil → English:**
```bash
python TamToEng.py
```

**English → Tamil:**
```bash
python EngToTam.py
```

---

## 🎯 How to Use

1. Run either script depending on your translation direction
2. When prompted, **speak clearly** into your microphone
3. The app will recognize your speech, translate it, and **play the translated audio**
4. Done — no buttons, no browser, just speak

---

## 🛠️ Troubleshooting

**Microphone not working?**
Check that your mic is connected and that your OS grants microphone permission to Python/terminal.

**Translation inaccurate?**
Speak clearly and at a moderate pace. Background noise significantly reduces recognition accuracy.

**`playsound` errors on macOS/Linux?**
Try installing `ffmpeg` or use `pygame` as an alternative audio backend.

---

## ✅ Conclusion

A lightweight but powerful demonstration of how Python's speech and translation ecosystem can eliminate language barriers in real time. Tamil and English speakers can communicate freely — no app store, no subscription, no setup beyond a single `pip install`.

---

<div align="center">

Built with ❤️ by **Shreyash Gautam**
Special thanks to **Dipsita Rout** for the English → Tamil feature and thorough testing.

</div>
