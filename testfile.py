from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
     return "Test code is working!!!"


@app.route('/next')
def next():
     return "showing the next page!!!"

if __name__ =='__main__':
     app.run()
