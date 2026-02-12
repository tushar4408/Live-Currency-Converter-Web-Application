from flask import Flask, render_template, request
from converter import convert, get_supported_currencies, get_currency_name

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    currencies = get_supported_currencies()

    # Create display dictionary with full names
    currency_display = {
        code: get_currency_name(code)
        for code in currencies
    }

    if request.method == "POST":

        try:
            amt = float(request.form["amount"])
            if amt <= 0:
                raise ValueError
        except:
            return render_template(
                "index.html",
                result="Please enter a valid positive number.",
                currencies=currencies,
                currency_display=currency_display
            )

        frm = request.form["from"].upper()
        to = request.form["to"].upper()

        try:
            converted_amount = convert(amt, frm, to)
            result = f"{amt:,.2f} {frm} = {converted_amount:,.2f} {to}"
        except Exception as e:
            result = f"Error: {e}"

    return render_template(
        "index.html",
        result=result,
        currencies=currencies,
        currency_display=currency_display
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
