from flask import Flask
from model.predictor import StickerPredictor

sticker_predictor = StickerPredictor()
app = Flask(__name__)

from app import routes
