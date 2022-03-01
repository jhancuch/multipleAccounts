from flask import Flask, render_template
from utils import twitter_embed

html_embed = twitter_embed('https://twitter.com/PopularFront_', 'https://twitter.com/TaskandPurpose', 'https://twitter.com/mchancecnn', 'https://twitter.com/KyivIndependent')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
if __name__ == "__main__":
    app.run(debug=True)
