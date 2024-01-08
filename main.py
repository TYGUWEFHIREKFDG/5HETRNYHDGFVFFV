import dns.resolver
import json
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route('/', methods=['POST', 'GET'])


def index():
    if request.method == 'POST':
        try:
            def checkmx(domain):
                for x in dns.resolver.resolve(domain, 'MX'):
                    result = json.dumps(x.to_text())
                    return result

            domain = str(request.form.get('domain'))

            mx = checkmx(domain)
            return mx
        except:
            return 'Priest(e)'
    else:
        return 'Priest(e)'


if __name__ == '__main__':
    #app.debug = True
    app.run(host='0.0.0.0', port=8000)