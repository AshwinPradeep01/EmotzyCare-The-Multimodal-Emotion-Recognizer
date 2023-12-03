
import assemblyai as aai

def transcribe():
    """ Function for simple transcription"""
    try:
        # Replace with your API token
        aai.settings.api_key = f"c6f3e6b96e594fa881ce152c2f6a6072"

        # URL of the file to transcribe
        # FILE_URL = 'D:\\Emotzy\\Emotzy\\uploads\\recorded_audio.wav'
        # You can also transcribe a local file by passing in a file path
        FILE_URL = 'uploads/recorded_audio.wav'
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(FILE_URL)
        print("transcribed:",transcript.text)
    except:
        print("Error Occurred!")  
    return transcript.text

# result=transcribe()
# print(result)


def transcribe_speaker():
    """ Function to transcribe based on the speaker"""
    # Replace with your API token
    aai.settings.api_key = f"c6f3e6b96e594fa881ce152c2f6a6072"

    # URL of the file to transcribe
    FILE_URL = 'audio_recording.wav'

    # You can also transcribe a local file by passing in a file path
    # FILE_URL = './path/to/file.mp3'

    config = aai.TranscriptionConfig(speaker_labels=True)

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(
    FILE_URL,
    config=config
    )

    for utterance in transcript.utterances:
        print(f"Speaker {utterance.speaker}: {utterance.text}")

# transcribe_speaker()
# ------------------------------------------------------------------------

def transcribe_with_highlights():
    """ Function to transcribe as well as get highlighted words """
    # Replace with your API token
    aai.settings.api_key = f"c6f3e6b96e594fa881ce152c2f6a6072"

    # URL of the file to transcribe
    # FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
    FILE_URL = 'D:\\Emotzy\\Emotzy APP\\audio_recording.wav'

    # You can also transcribe a local file by passing in a file path
    # FILE_URL = './path/to/file.mp3'

    config = aai.TranscriptionConfig(auto_highlights=True)

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(
    FILE_URL,
    config=config
    )

    for result in transcript.auto_highlights.results:
        print(f"Highlight: {result.text}, Count: {result.count}, Rank: {result.rank}")

