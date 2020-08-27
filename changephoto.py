from flask import Flask

UPLOAD_FOLDER = "static/uploads/"

changephoto = Flask(__name__)

changephoto.secret_key = "mysecretkey"
changephoto.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
changephoto.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
