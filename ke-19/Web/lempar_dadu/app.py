from flask import Flask, render_template
import random 
app = Flask(__name__)

@app.route('/')
def index():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dadu = random.randint(0,len(dice)-1)
    return render_template('index.html',dadu=dice[dadu])
if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0")