from config import *  # linha que importa os comandos da pasta 'config.py'
from materia import *  # linha que importa os comandos da pasta 'materia.py'

@app.route("/") # define a rota padrão do acesso web
def inicio():
    return 'Sistema de cadastro de pessoas. '+\
        '<a href="/listar_pessoas">Operação listar</a>'+\
            '<br>Sistema de cadastro de matéria. '+\
        '<a href="/listar_materias">Operação listar</a>'

@app.route("/listar_pessoas") # define a rota de acesso web para listagem de pessoas
def listar_pessoas():
    pessoas = db.session.query(Pessoa).all() # comando que obtem as pessoas do cadastro
    pessoas_em_json = [ x.json() for x in pessoas ] # comando que aplica o método json que a classe Pessoa possui a cada elemento da lista
    return jsonify(pessoas_em_json)# comando que fornece a lista de pessoas em formato json


@app.route("/listar_materias")# define a rota de acesso web para listagem de materias
def listar_materias():
    materias = db.session.query(Materia).all() # comando que obtem as materias do cadastro
    materias_em_json = [ x.json() for x in materias ] # comando que aplica o método json que a classe Materia possui a cada elemento da lista
    return jsonify(materias_em_json) # comando que fornece a lista de materias em formato json

app.run(debug=True) # roda o aplicativo com debug ativado
