from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/netflixvoice', methods=['POST'])
def get_netflix_main():
    try:
        with open('main_play.py', 'r') as file:
            codigo_python = file.read()
            exec(codigo_python)
            
    except Exception as e:
        resultado = f"Erro durante a execução do código: {str(e)}"
        print(resultado)

    # Retorne uma resposta vazia
    return make_response('Código executado com sucesso', 200)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
