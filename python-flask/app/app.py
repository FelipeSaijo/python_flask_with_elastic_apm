from flask import Flask, render_template, jsonify

from elasticapm.contrib.flask import ElasticAPM

from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app, group_by='path')
metrics.start_http_server(9999)

app.config['ELASTIC_APM'] = {

  'DEBUG': True,

  'SERVICE_NAME': 'Flask-App',
  'SERVER_URL': '172.18.0.2:8200',
  'ENVIRONMENT': 'dev',

  'CAPTURE_HEADERS': True,
  'CAPTURE_BODY': all,
  'SPAN_COMPRESSION_ENABLED': True,
  
  'EXCLUDE_PATHS': ['/static'],
  'FRAMEWORK_NAME': 'flask',
  'PROMETHEUS_METRICS': True

}

apm = ElasticAPM(app)

@app.route("/")
def hello():
  try:
    return render_template('index.html')
  except:
    apm.capture_exception()
    
@app.route("/error")
def error():
  error_message = "Ocorreu um erro interno no servidor."
  return jsonify({'error': error_message}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')