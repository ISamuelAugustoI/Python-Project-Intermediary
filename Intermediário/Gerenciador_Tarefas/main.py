# Importando Bibliotecas:
import mysql.connector
from mysql.connector import Error

# Conectar ao BD:
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='dbgerenciador_tarefas'
        )
        if(connection.is_connected()):
            print(f'Connecting with sucefully to mysql!')
        return connection
    except Error as e:
        print(f'Error connecting to mysql: {e}')
        return None
# Criar a Tabela de Tarefas, caso não exista
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas(
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    categoria VARCHAR(100),
    prazo DATE,
    status VARCHAR(50) DEFAULT 'Pendente')
    ''')
    connection.commit()

# Adicionar Tarefas:
def add_task(connection):
    description = str(input('Enter the description: '))
    category = str(input('Enter the category: '))
    term = str(input('Enter the date[AAAA-MM-DD]: '))
    status = str(input('Enter the status[Pendente,Concluída,Atrasada]: '))
    cursor = connection.cursor()
    cursor.execute('INSERT INTO tarefas(descricao, categoria, prazo, status) VALUES (%s, %s, %s, %s)',
                   (description,category,term,status))
    connection.commit()
    print(f'Task add with sucefully!')

# Listar Tarefas:
def list_tasks(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tarefas')
    tasks = cursor.fetchall()
    if(tasks):
        print("ID | Descrição | Categoria | Prazo | Status")
        for task in tasks:
            print(f"{task[0]} | {task[1]} | {task[2]} | {task[3]} | {task[4]}")
    else:
        print("None Tasks...")

# Editar Tarefas:
def edit_task(connection):
    list_tasks(connection)
    task_id = input('Enter the ID of task to edit: ')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tarefas WHERE id = %s', (task_id,))
    task = cursor.fetchone()
    if(task):
        print(f"Task found: {task[1]} - {task[2]} - {task[3]} - {task[4]}")
        description = str(input('Enter the new description: '))
        category = str(input('Enter the new category: '))
        term = str(input('Enter the new date: '))
        status = str(input('Enter the new status: '))
        description = (description if description else task[1])
        category = (category if category else task[2])
        term = (term if term else task[3])
        status = (status if status else task[4])
        cursor.execute('''UPDATE tarefas SET descricao = %s, categoria = %s, prazo = %s, status = %s
                        WHERE id = %s''', (description, category, term, status, task_id))
        connection.commit()
        print('Update task sucefully!')
    else:
        print('Task not found.')

# Deletar Tarefas:
def delete_task(connection):
    list_tasks(connection)
    task_id = int(input('Enter the Id of task to delete: '))
    cursor = connection.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id = %s', (task_id,))
    connection.commit()
    print('Task deleted with sucefully!')

# Menu de Tarefas
def main():
    connection = connect_to_database()
    if not connection:
        return
    create_table(connection)
    while True:
        print(f'\n==== Welcome to the Task Manager ====')
        print("Choose an option:")
        print('[1] = Add Task')
        print('[2] = List Tasks')
        print('[3] = Edit Task')
        print('[4] = Delete Task')
        print('[5] = Exit')
        choice = int(input('Enter a number: '))
        if(choice==1):
            add_task(connection)
        elif(choice==2):
            list_tasks(connection)
        elif(choice==3):
            edit_task(connection)
        elif(choice==4):
            delete_task(connection)
        elif(choice==5):
            print("Exit...")
            connection.close()
            break
        else:
            print("Invalid option. Try again...")
if(__name__=="__main__"):
    main()