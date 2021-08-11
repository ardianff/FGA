from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "mySecretKey2021"

@app.route('/')
def indexku():
    hari = ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
    nilaiku = 100
    suasana = "sedih"
    return render_template('index.html', nilai=nilaiku, value = hari, suasana=suasana)
@app.route('/contact')
def contactku():
    return render_template('contact.html')
@app.route('/about')
def aboutku():
    return render_template('about.html')
@app.route('/parsing/<string:nilaiku>')
def parsing(nilaiku):
    return "nilainya adalah : {}".format(nilaiku)
@app.route('/parsingargument')
def ayo_argument():
    data = request.args.get("nilai")
    return "nilai dari argument parser adalah {}".format(data)
@app.route('/halaman/<int:nilai>')
def session_1(nilai):
    session["nilaiku"] = nilai
    return "Berhasil mengset nilainya"
@app.route('/halaman/lihat')
def view_session_1():
    try :
        data = session["nilaiku"]
        return "Nilai yang telah di save adalah {}".format(data)
    except :
        return "Anda tidak memiliki nilai session lagi"
@app.route('/halaman/logout')
def logout_session_1():
    session.pop("nilaiku")
    return "Berhasil Logout / menghapus session"



if __name__ == '__main__':
    app.run(debug=True)