# 🗣️ Live Captions on Video Feed using Flask, OpenCV & Speech Recognition

This project creates a **real-time captioning system** that:
- Captures live video using **OpenCV**
- Captures microphone input using **SpeechRecognition**
- Converts speech to text using **Google Web Speech API**
- Overlays the text (captions) on a **semi-transparent black bar** at the bottom of the video
- Streams everything in a **Flask web app** using live video feed

---

## 📸 Preview

<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DhPv1PkjJ-J0&psig=AOvVaw0dLLE8QzSVtaaBt2pPZeSF&ust=1745579850855000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKDs6enF8IwDFQAAAAAdAAAAABAR" alt="Live Captions Demo" style="border-radius: 10px;" />

---

## 🚀 Features

✅ Real-time webcam feed  
✅ Live speech-to-text captions  
✅ Clean UI with centered layout  
✅ Semi-transparent black bar with white text  
✅ Auto ambient noise calibration  
✅ Works in modern browsers  

---

## 🛠️ Requirements

Make sure Python is installed. Then install the dependencies:

```bash
pip install -r requirements.txt
```

**requirements.txt**
```
Flask
opencv-python
SpeechRecognition
```

---

## 🧠 How it works

- `OpenCV` captures video from your webcam.
- `SpeechRecognition` continuously listens in a background thread.
- Captions are updated and drawn directly onto each video frame.
- A Flask route `/video` streams the JPEG frames using MJPEG.

---

## 📂 Project Structure

```
📁 live-caption-app/
│
├── app.py               # Main Flask app
├── templates/
│   └── index.html       # UI for browser
├── static/              # (optional for styling, logos, etc.)
├── requirements.txt     # Python dependencies
└── README.md            # You're here!
```

---

## ▶️ Run the App

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🧪 Tips for Better Accuracy

- Use a good external microphone 🎤  
- Speak clearly and avoid background noise  
- The system uses `recognizer.adjust_for_ambient_noise()` for noise calibration  

---

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 💡 Inspiration

Inspired by accessibility tools like YouTube Live Captions and real-time transcription for hearing-impaired users.

---

## 🙌 Author

Made with ❤️ by [Agneya Pathare](https://www.linkedin.com/in/agneya-pathare)
