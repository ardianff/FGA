from flask import Flask, render_template, url_for, redirect, request, session, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "iniSecretKeyKu2019"

user_email = "admin@gmail.com"
user_pass = "12345"
@app.route("/", methods=["POST", "GET"])
def index():
    if "email" in session:
        return redirect(url_for('sukses'))
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        if email == user_email and password == user_pass:
            session['email'] = email
            session['password'] = password
            return redirect(url_for('sukses'))

        # jika email atau password salah
        else:
            flash("Username atau Password yang anda masukkan salah")
            return redirect(url_for('index'))
    
    return render_template("index.html")
@app.route("/home")
def sukses():
    return render_template("home.html")

# @app.route("/about")
# def about():
#     if "email" in session:
#         return render_template("about.html")
#     else:
#         return redirect(url_for('index'))


# @app.route("/contact")
# def contact():
#     # jika dia sedang login
#     if "email" in session:
#         return render_template("contact.html")
#     else :
#     # jia dia tidak sedang login
#         return redirect(url_for('index'))


@app.route("/logout")
def logout_akun():
    if "email" in session:
        session.pop("email")
        session.pop("password")
        return redirect(url_for('index'))
    else:    
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0")