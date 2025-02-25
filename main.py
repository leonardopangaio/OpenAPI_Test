from flask import Flask, request, jsonify
from datetime import datetime
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/hora', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Retorna a hora atual',
            'schema': {
                'type': 'object',
                'properties': {
                    'hora': {
                        'type': 'string',
                        'example': '14:30:00'
                    }
                }
            }
        }
    }
})
def get_hora():

    hora_atual = datetime.now().strftime("%H:%M:%S")
    return jsonify({'hora': hora_atual})


@app.route('/ola', methods=['POST'])

def post_ola():
    """
    Retorna uma saudação personalizada
    ---
    tags:
      - API de Olá
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            name:
              type: string
              example: "João"
          required:
            - name
    responses:
      200:
        description: Mensagem de saudação.
      400:
        description: Erro na requisição.
    """
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'O campo "name" é obrigatório.'}), 400
    name = data['name']
    return jsonify({'message': f'Olá, {name}!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030, debug=True)
