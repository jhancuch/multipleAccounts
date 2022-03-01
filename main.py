from flask import Flask, render_template
from utils import twitter_embed

html_embed = twitter_embed('https://twitter.com/PopularFront_', 'https://twitter.com/mchancecnn', 'https://twitter.com/KyivIndependent')
feed1, feed2, feed3 = html_embed[0], html_embed[1], html_embed[2]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", feed1=feed1, feed2=feed2, feed3=feed3)
    
if __name__ == "__main__":
    app.run(debug=True)
