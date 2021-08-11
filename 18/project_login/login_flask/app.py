from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def indexku():
    hari = ['Senin','Selasa','Rabu','Kamis','Jumat','Sabtu','Minggu']
    nilaiku = 100
    return render_template('index.html', nilai=nilaiku, value = hari)

if __name__ == '__main__':
    app.run(debug=True)