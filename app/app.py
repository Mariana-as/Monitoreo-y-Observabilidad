from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Contador que registra las visitas a la página principal
visitas = Counter(
    'webapp_visits_total',
    'Total de visitas a la aplicación web'
)

@app.route('/')
def inicio():
    visitas.inc()
    return '<h1>¡Mi aplicación DevOps funciona!</h1><p>Visitas registradas correctamente.</p>'

@app.route('/metrics')
def metricas():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
