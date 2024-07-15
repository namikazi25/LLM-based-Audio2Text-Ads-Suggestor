import whisper

# model = whisper.load_model("base")

# result = model.transcribe("audiov1.mp3")
# print(result["text"])

def transcribe(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]