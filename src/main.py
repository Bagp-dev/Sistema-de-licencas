import sqlite3

conexao_banco = sqlite3.connect('banco_de_dados.db')

cursor = conexao_banco.cursor()

cursor.execute("""CREATE TABLE LICENCAS (
ID_Licenca integer primary key autoincrement not null,
Nome_Cliente text not null,
Plano text not null,
Data_Expiracao text date not null,
Ativa boolean not null
)""")

cursor.execute("""INSERT INTO LICENCAS (Nome_Cliente, Plano, Data_Expiracao, Ativa) VALUES
('cliente 1', 'Basico', '2025-12-31', 1),
('cliente 2', 'Premium', '2025-06-30', 1),
('cliente 3', 'Enterprise', '2023-10-05', 0),
('cliente 4', 'Basico', '2024-08-15', 1),
('cliente 5', 'Premium', '2026-01-20', 0)""")

cursor.execute("SELECT * FROM LICENCAS")

registros = cursor.fetchall()

print(registros)

for registro in registros:
    ID_Licenca, Nome_Cliente, Plano, Data_Expiracao, Ativa = registro
    print(f"ID: {ID_Licenca}, Nome: {Nome_Cliente}, Plano: {Plano}, Data Expiração: {Data_Expiracao}, Ativa: {Ativa}")
    print("\n")

#consulta A
cursor.execute("""SELECT * FROM LICENCAS 
WHERE Plano = 'Premium' AND Ativa = 1""")
registros = cursor.fetchall()
print(registros)

#consulta B
cursor.execute("""SELECT * FROM LICENCAS 
WHERE Data_Expiracao < '2025-12-15' """)
registros = cursor.fetchall()
print(registros)

conexao_banco.commit()
