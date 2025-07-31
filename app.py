from flask import Flask, render_template, request, send_file
from voiceover import generate_voiceover
from imagegen import generate_images
from captions import generate_captions
from videoedit import render_video
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        script_text = request.form["script"]

        print("Generating voiceover...")
        voice_file = generate_voiceover(script_text)

        print("Generating captions...")
        captions_file = generate_captions(script_text, voice_file)

        print("Generating images...")
        images = generate_images(script_text)

        print("Rendering video...")
        output_path = render_video(images, voice_file, captions_file)

        return send_file(output_path, as_attachment=True, download_name="generated_video.mp4")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


