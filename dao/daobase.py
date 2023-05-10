import sqlite3

class Table:
    def __init__(self, table_name, fields, db_file):
        self.table_name, self.fields, self.db_file = table_name, fields, db_file
        self.func_create_table()
    
    def func_create_table(self):
        query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
        for field, field_type in self.fields.items():
            query += f"{field} {field_type}, "
        query = query[:-2] # remove a ultima virgula e espaço
        query += ")"
        with sqlite3.connect(self.db_file) as conn:
            conn.execute(query)
    
    @classmethod
    def func_database_connect(cls, database):   
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        return cursor, conn
    
    @classmethod
    def func_check_if_exists(cls, data, cpf_or_id, table):
        cursor, conn = Table.func_database_connect("D:\Empresa\dao\database.db")
        query = f"SELECT {cpf_or_id} FROM {table} WHERE {cpf_or_id} = ?"
        cursor.execute(query, (data,))
        tuple_or_none = cursor.fetchone()
        conn.close()
        return tuple_or_none
    
    @classmethod
    def get_all(cls, table: str):
        cursor, conn = Table.func_database_connect("D:\Empresa\dao\database.db")
        query = f'SELECT * FROM {table}'
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data
    
    @classmethod
    def count_records(cls, table: str):
        cursor, conn = Table.func_database_connect("D:\Empresa\dao\database.db")
        query = f'SELECT COUNT(*) FROM {table}'
        count = cursor.execute(query)
        count = count.fetchone()[0]
        return count

   
    @classmethod
    def func_add(cls, table_name, **kwargs):
        cursor, conn = Table.func_database_connect("D:\Empresa\dao\database.db")
        set_clause = ", ".join([key for key in kwargs.keys()])
        values = [f"{value}" for value in kwargs.values()]
        s = (len(values) * "?, ")[:-2] 
        query = f"INSERT INTO {table_name} ({set_clause}) VALUES ({s})"
        cursor.execute(query, values)
        conn.commit()
        conn.close()

        return f'Registro adicionado com sucesso na tabela {table_name}'

    @classmethod    
    def func_display(cls, table):
         cursor, conn = Table.func_database_connect("D:\Empresa\dao\database.db")
         data = list(cursor.execute(f"SELECT * FROM {table};"))
         conn.close()
         return data
    
    @classmethod
    def func_edit(cls, table_name, id, **kwargs):
        cursor, conn = Table.func_database_connect("D:\Empresa\dao\database.db")
        set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE id = ?"
        values = [*kwargs.values(), id]
        cursor.execute(query, values)
        conn.commit()
        conn.close()
        return f'Registro  da tabela {table_name} alterado com sucesso'
       
    @classmethod
    def func_delete(cls, id_number, field, table):
        cursor, conn = Table.func_database_connect("D:\Empresa\dao\database.db")
        cursor.execute(f"DELETE FROM {table} WHERE {field} = ?", (id_number,))
        conn.commit()
        conn.close()
        return 'Registro deletado com sucesso.'

 
if __name__ == "__main__":
    Table.count_records("Client")




