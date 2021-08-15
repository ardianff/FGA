from flask import Flask, render_template, url_for,redirect, request,session

app = Flask(__name__)
app.config["SECRET_KEY"] = "mySecretKey2021"
user_email = "admin@gmail.com"
user_pass = "hai"
@app.route("/", methods=["POST","GET"])
def index():
    if user_email in session :
        return redirect(url_for('sukses'))
    if request.method == "POST": 
        email = request.form['email']
        password = request.form['password']
        # jika email dan password benar
        if email == user_email and password == user_pass: 
            session['email'] = email
            session['password'] = password
            return redirect(url_for("sukses"))
            # jika email atau password salah
        else: 
             return redirect(url_for('index'))
    return render_template("index.html") 
@app.route("/sukses")
def sukses():
    nilai = "Anda sukses login"
    return render_template("sukses.html", nilai=nilai)

@app.route("/about")
def about():
    if user_email in session: 
        return render_template("about.html")
    else: 
        return redirect(url_for('index'))
@app.route("/contact")
def contact():
    if user_email in session: 
        return render_template("contact.html")
    else: 
        return redirect(url_for('index'))
@app.route("/logout")
def logout():
    if "email" in session : 
        session.pop("email")
        session.pop("password")
        return redirect(url_for('index'))
    else: 
        
        return redirect(url_for('index'))


@app.route("/redirect-about")
def ayo_redirect_about():
    return redirect(url_for("about"))
@app.route("/redirect-contact")
def ayo_redirect_contact():
    return redirect(url_for("contact"))

if __name__ == '__main__':
    app.run(debug=True, port=5001)