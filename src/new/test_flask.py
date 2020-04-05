from flask import Flask
app=Flask(__name__)
@app.route('/aaa')
def hello() -> str:
	return "hi.nice to meet you!"
app.run()