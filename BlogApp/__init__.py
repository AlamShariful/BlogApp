from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"
    #return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)

    #app.run()
