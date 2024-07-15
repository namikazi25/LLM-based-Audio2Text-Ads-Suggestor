from transcribe import transcribe
from llmadsranking import generate_ad_recommendations

transcribed_text = transcribe("audiov1.mp3")

print(transcribed_text)

ad_recommendations = generate_ad_recommendations(transcribed_text)
print("Ad Recommendations:" + ad_recommendations)