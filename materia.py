from config import * # linha que importa os comandos da pasta 'config.py'

class Pessoa(db.Model): # Classe que representa uma Pessoa, e adiciona o usuario ao banco de dados (classe do Projeto Integrador)
    id = db.Column(db.Integer, primary_key = True)
    nome_completo = db.Column (db.String(255))
    usuario = db.Column (db.String(255))
    senha = db.Column (db.String(255))
    email = db.Column (db.String(255))
    telefone = db.Column (db.String(20))

    def json(self): # metodo que retorna os dados da classe em formato Json
        return{
            "id": self.id,
            "nome_completo": self.nome_completo,
            "usuario": self.usuario,
            "senha": self.senha,
            "email": self.email,
            "telefone" : self.telefone
        }

#AV3 Programação:
class Materia(db.Model): #Classe que representa Matéria Escolar, e adiciona os dados ao banco de dados
    id = db.Column(db.Integer, primary_key = True)
    disciplina = db.Column (db.String(255)) #chave estrangeira
    titulo = db.Column (db.String(255))
    data_prova = db.Column (db.String(10))

    def json(self): # metodo que retorna os dados da classe em formato Json
        return{
            "id": self.id,
            "disciplina": self.disciplina,
            "titulo": self.titulo,
            "data_prova": self.data_prova
        }


#teste do programa 
if __name__ == "__main__":

    if os.path.exists(arquivobd): # camando que verifica se já existe o banco de dados
        os.remove(arquivobd) # camando que se existe ele os remove

    db.create_all() # camando que cria o banco de dados 'aprovei.db' 

    nova_pessoa = Pessoa(nome_completo = "Mab Fraga", usuario = "mab",
        senha = "4321", email = "mab@gmail.com", telefone = "(47) 9 9874-5612") # camando que insere os dados de um novo usuario
    db.session.add(nova_pessoa) # camando que adiciona o novo usuario ou banco de dados 

    nova_materia = Materia(disciplina = "Geografia", titulo = "Mapas", data_prova = "21/08/2021")# insere os dados de uma nova matéria
    db.session.add(nova_materia) # camando que adiciona a nova matéria ou banco de dados 
    db.session.commit()# camando que salva os dados no banco de dados

    pessoas = db.session.query(Pessoa).all() # camando que carrega os dados da tabela pessoas
    for pessoa in pessoas: # camando que verifica se há informações na tabela
        print(pessoa)
        print(pessoa.json()) # camando que se houver lista todos os dados
    
    materias = db.session.query(Materia).all() # camando que carrega os dados da tabela materia
    for materia in materias:# camando que verifica se há informações na tabela
        print(materia)
        print(materia.json()) # camando que verifica se há informações na tabela
    
