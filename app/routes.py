import io
from PIL import Image
from flask import request, jsonify

from app import app, sticker_predictor


@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}

    if request.method == "POST":
        if request.files.get("image"):
            # read the image in PIL format
            file = request.files['image']
            img_bytes = file.read()
            image = Image.open(io.BytesIO(img_bytes))

            # prepare the image for classification
            image = sticker_predictor.prepare_image(image)

            # classify the input image
            label, prob = sticker_predictor.predict(image)
            data["predictions"] = {"label": label, "score": float(prob)}

            # indicate that the request was a success
            data["success"] = True

    return jsonify(data)
