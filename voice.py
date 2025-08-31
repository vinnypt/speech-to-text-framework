import speech_recognition as sr
import numpy as np
import noisereduce as nr
import librosa
import io
import scipy.io.wavfile as wav

def preprocess_audio(audio_data, sample_rate=16000):
    audio_bytes = audio_data.get_wav_data()
    audio_buffer = io.BytesIO(audio_bytes)
    sr_wav, y = wav.read(audio_buffer)
    y = y.astype(np.float32)
    y = y / np.max(np.abs(y))
    y_denoised = nr.reduce_noise(y=y, sr=sr_wav)
    mfccs = librosa.feature.mfcc(y=y_denoised, sr=sr_wav, n_mfcc=13)
    print("MFCCs shape:", mfccs.shape)
    print("MFCCs (first frame):", mfccs[:, 0])
    return y_denoised, sr_wav, mfccs

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio_mic = r.listen(source)
    try:
        y_denoised, sr_wav, mfccs = preprocess_audio(audio_mic)
        # (Optional) Use mfccs for further processing or ML models
        y_int16 = np.int16(y_denoised / np.max(np.abs(y_denoised)) * 32767)
        buf = io.BytesIO()
        wav.write(buf, sr_wav, y_int16)
        buf.seek(0)
        audio_processed = sr.AudioData(buf.read(), sr_wav, 2)
        text_mic = r.recognize_google(audio_processed)
        print("Microphone: " + text_mic)
        return text_mic.lower()
    except sr.UnknownValueError:
        print("Microphone: Could not understand audio")
    except sr.RequestError as e:
        print(f"Microphone: Could not request results; {e}")
    return None