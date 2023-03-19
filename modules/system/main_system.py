from modules.configs.config import finnance,finnance_db
from modules.configs.config import error,debug
from hashlib import sha256

class Usuario:
    def __init__(self):
        self.ID_user = None
        self.conta = None

    @staticmethod
    def tofloat(valor):
        if len(valor) > 3 and valor[-3] == ',':
            valor = list(valor)
            valor[-3] = "%"
            valor = ''.join(valor)
            valor = valor.replace('.','')
            valor = valor.replace('%','.')
            return valor
        valor = valor.replace('.','')
        return valor

    def login(self,user,password):
        password = password.encode()
        password = sha256(password).hexdigest()
        finnance.execute(f'select * from usuarios where username like "{user}"')
        conta = finnance.fetchall()
        if len(conta) == 0:
            self.ID_user = None
        elif password == conta[0][2]:
            self.ID_user = conta[0][0]
            self.conta = conta[0]
            return self.ID_user
        else: 
            self.ID_user = None

    #Salario
    def update_salario(self,valor):
        valor = float(valor)
        finnance.execute(f'update usuarios set salario = {valor} where ID_user = {self.ID_user}')
        finnance_db.commit()
    def refresh_salario(self):
        finnance.execute(f'select * from usuarios where ID_user like {self.ID_user}')
        conta = finnance.fetchall()
        self.conta = conta[0]

    #Gastos
    def list_gastos(self):
        finnance.execute(f"select * from Gastos join usuarios where Gastos.FID_user = {self.ID_user} and usuarios.ID_user = {self.ID_user}")
        
        return finnance.fetchall()
    def remove_gasto(self,id_gasto):
        try:
            finnance.execute(f"DELETE FROM Gastos WHERE ID_gasto = {id_gasto}")
            finnance_db.commit()
        except OperationalError:
            error("Error with database")
        except Exception as erro:
            error(erro)
    def add_gasto(self,desc,valor,id_user):
        try:
            
            debug(f'Add gasto with value of {valor} in user {id_user}')
            valor = float(valor)
            finnance.execute(f"INSERT INTO Gastos (desc_gasto,valor_gasto,FID_user) VALUES ('{desc}',{valor},{id_user})")
            finnance_db.commit()
        except OperationalError:
            error("Error with database")
        except Exception as erro:
            error(erro)
    #Lucros
    def list_lucros(self):
        try:
            finnance.execute(f"select * from Lucros join usuarios where Lucros.FID_user = {self.ID_user} and usuarios.ID_user = {self.ID_user}")
            return finnance.fetchall()
        except Exception as erro:
            error (erro)
    def remove_lucro(self,id_lucro):
        try:
            finnance.execute(f"DELETE FROM Lucros WHERE ID_lucro = {id_lucro}")
            finnance_db.commit()
        except OperationalError:
            error("Error with database")
        except Exception as erro:
            error(erro)
    def add_lucro(self,desc,valor,id_user):
        try:
            valor = float(valor)
            debug(f'Add lucro with value of {valor} in user {id_user}')
            finnance.execute(f"INSERT INTO Lucros (desc_lucro,valor_lucro,FID_user) VALUES ('{desc}',{valor},{id_user})")
            finnance_db.commit()
        except OperationalError:
            error("Error with database")
        except Exception as erro:
            error(erro)

    
    