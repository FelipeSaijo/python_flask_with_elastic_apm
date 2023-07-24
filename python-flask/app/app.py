from flask import Flask, render_template

from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)

app.config['ELASTIC_APM'] = {

  'DEBUG': True,

  'SERVICE_NAME': 'Flask-App',
  'SERVER_URL': '172.20.0.2:8200',
  'ENVIRONMENT': 'dev',

  'CAPTURE_HEADERS': True,
  'CAPTURE_BODY': all,
  'SPAN_COMPRESSION_ENABLED': True,
  
  'EXCLUDE_PATHS': ['\*/static/*']

}

apm = ElasticAPM(app)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')