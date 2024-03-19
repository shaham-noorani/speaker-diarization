import time
import dotenv
import os

dotenv.load_dotenv()

import assemblyai as aai

aai.settings.api_key = os.environ.get("ASSEMBLY_AI_KEY")


def transcribe_audio(audio_url, config):
    return aai.Transcriber().transcribe(audio_url, config)


def process_transcript(transcript, students):
    output = []
    for utterance in transcript.utterances:
        speaker = "Student" if utterance.speaker in students else "Interviewee"
        speaker += f" (Speaker {utterance.speaker})"

        output.append(
            {
                "speaker": speaker,
                "start": utterance.start,
                "end": utterance.end,
                "caption": utterance.text,
            }
        )
    return output


audio_url = "https://togethertechaudio.s3.amazonaws.com/musk_interview.wav"

config = aai.TranscriptionConfig(
    speaker_labels=True,
    speakers_expected=2,
    disfluencies=False,
    audio_start_from=0,
    audio_end_at=100000,
)

print("Transcribing audio...")

process_start_time = time.time()
transcript = transcribe_audio(audio_url, config)

students = ["A"]

output = process_transcript(transcript, students)

print("\nTranscript:")
print(output)

process_end_time = time.time()
total_processs_time = process_end_time - process_start_time
print("\nProcess time:", total_processs_time, "seconds")
