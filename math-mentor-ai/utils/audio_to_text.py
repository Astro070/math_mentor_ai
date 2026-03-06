import whisper
import tempfile

model = whisper.load_model("base")

def transcribe_audio(audio_bytes):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name

    result = model.transcribe(temp_audio_path)

    return result["text"]