from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)

@app.route('/')
def home():
    """home"""
    return """
    <h1>home</h1>
    <ul>
        <li><a href="api/json/v1/info">info</a></li>
        <li><a href="api/html/v1/details">hello</a></li>
        <li><a href="api/json/v1/details">json hello</a></li>
        <li><a href="api/json/v1/healthz">health check</a></li>
    </ul>
    """

@app.route('/api/json/v1/info')
def info():
    """get time, hostname and blabla"""
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p on %A %d %B, %Y"),
    	'hostname': socket.gethostname(),
        'fqdn': socket.getfqdn(),
        'message': 'You are doing great, little human! <3',
        'deployed_on': 'localhost 4 the moment'
    })

@app.route('/api/html/v1/details')
def details():    
    """say hello in html"""

    if datetime.datetime.now().hour > 21:
        return '<h1>hello world, good night</1>'
    elif datetime.datetime.now().hour > 19:
        return '<h1>hello world, enjoy the rest of your evening</1>'
    elif datetime.datetime.now().hour > 16:
        return '<h1>hello world, have a pleasant evening</1>'
    elif datetime.datetime.now().hour > 12:
        return '<h1>hello world, good afternoon</1>'
    elif datetime.datetime.now().hour > 11:
        return '<h1>hello world, good noon</1>'
    else:
        return '<h1>hello world, good morning</1>'

@app.route('/api/json/v1/details')
def json_details():
    """say hello in json"""

    if datetime.datetime.now().hour > 19:
        return jsonify({ 'msg' : 'hello world, good night' })
    elif datetime.datetime.now().hour > 16:
        return jsonify({ 'msg' : 'hello world, good evening' })
    elif datetime.datetime.now().hour > 12:
        return jsonify({ 'msg' : 'hello world, good afternoon' })
    elif datetime.datetime.now().hour > 11:
        return jsonify({ 'msg' : 'hello world, good noon' })
    else:
        return jsonify({ 'msg' : 'hello world, good morning' })

@app.route('/api/json/v1/healthz')
def health():
    """get health status"""
	# Do an actual check here
    return jsonify({'status': 'up'}), 200

if __name__ == '__main__':
    #app.run()
    ## from anywhere :]
    app.run(host="0.0.0.0")
