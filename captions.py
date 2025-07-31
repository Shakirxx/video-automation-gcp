def generate_captions(script_text, voice_file):
    captions_path = "captions.srt"
    with open(captions_path, "w") as f:
        f.write("1\n00:00:00,000 --> 00:00:05,000\n" + script_text)
    return captions_path

