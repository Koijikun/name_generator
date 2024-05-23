from flask import Flask, request, send_file

app = Flask(__name__, static_url_path='/', static_folder='web')

def generate_superhero_name(power, animal, color):
    return f"The Amazing {power.capitalize()} {animal.capitalize()} in {color.capitalize()}"

@app.route("/")
def indexPage():
    return send_file("web/index.html")

@app.route("/generate_superhero_name", methods=["POST"])
def generate_superhero_name_route():
    data = request.get_json()
    power = data.get("power", "")
    animal = data.get("animal", "")
    color = data.get("color", "")
    superhero_name = generate_superhero_name(power, animal, color)
    return {"superhero_name": superhero_name}
