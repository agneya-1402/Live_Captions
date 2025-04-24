from flask import Flask, render_template, Response
import cv2
import threading
import speech_recognition as sr

app = Flask(__name__)

cap = cv2.VideoCapture(1)

caption = ""
lock = threading.Lock()

def listen_and_transcribe():
    global caption
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

    while True:
        with mic as source:
            try:
                audio = recognizer.listen(source, timeout=3)
                text = recognizer.recognize_google(audio)
                with lock:
                    caption = text
            except:
                continue

def generate_frames():
    global caption
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            with lock:
                text_to_show = caption

            # Frame 
            height, width, _ = frame.shape

            # Caption bar + text
            overlay = frame.copy()
            cv2.rectangle(overlay, (0, height - 60), (width, height), (0, 0, 0), -1)
            alpha = 0.6
            frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            thickness = 2
            text_size = cv2.getTextSize(text_to_show, font, font_scale, thickness)[0]
            text_x = (width - text_size[0]) // 2
            text_y = height - 20
            cv2.putText(frame, text_to_show, (text_x, text_y), font, font_scale, 
                        (255, 255, 255), thickness, cv2.LINE_AA)

            # Encode 
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                   


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    audio_thread = threading.Thread(target=listen_and_transcribe)
    audio_thread.daemon = True
    audio_thread.start()

    app.run(debug=True)
