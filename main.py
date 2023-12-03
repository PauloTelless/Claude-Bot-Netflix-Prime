from flask import Flask, render_template, request

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
            resultado = "Código executado com sucesso!"
    except Exception as e:
        resultado = f"Erro durante a execução do código: {str(e)}"

    # Exibe o resultado no console para fins de depuração
    print("Resultado da execução:", resultado)

    # Renderiza o template 'test.html'
    return render_template('netflix_main_bot.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
