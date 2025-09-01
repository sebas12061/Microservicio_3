from flask import Flask
from controllers.mapas_controller import mapas_bp

app = Flask(__name__)
app.register_blueprint(mapas_bp)

if __name__ == "__main__":
    app.run(port=5006, debug=True)
