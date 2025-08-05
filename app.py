from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    bmi_rounded = round(bmi, 1)

    if bmi < 18.5:
        category = "Nën peshë"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Mbipeshe"
    else:
        category = "Obez"

    return {"bmi": bmi_rounded, "category": category}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            age = int(request.form["age"])
            weight = float(request.form["weight"])
            height = float(request.form["height"])

            # Shtro validime themelore nëse do
            if weight <= 0 or height <= 0:
                result = {"bmi": "N/A", "category": "Vlera joadekuate"}
            else:
                result = calculate_bmi(weight, height)
        except Exception as e:
            result = {"bmi": "N/A", "category": "Gabim në të dhëna"}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
