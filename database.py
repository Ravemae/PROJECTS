import sqlite3


def create_table():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            id TEXT PRIMARY KEY,
            name TEXT,    
            role TEXT, 
            gender TEXT,
            status TEXT,
            contact INTEGER,
            email TEXT)''')
    conn.commit()
    conn.close()


def fetch_employees():
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()

    conn.close()
    return employees


def insert_employee(id, name, role, gender, status, contact, email):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Employees (id, name, role, gender, status, contact, email) VALUES (?, ?, ?, ?, ?, ?, ?)',
                   (id, name, role, gender, status, contact, email))
    conn.commit()
    conn.close()


def delete_employee(id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Employees WHERE id = ?', (id,))
    conn.commit()
    conn.close()


def update_employee(new_name, new_role, new_gender, new_status, new_contact, new_email, id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Employees SET name = ?, role = ?, gender = ?, status = ?, contact = ?, WHERE id = ?",
                (new_name, new_role, new_gender, new_status, new_contact, new_email, id))
    conn.commit()
    conn.close() 


def id_exists(id):
    conn = sqlite3.connect('Employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Employees WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0


create_table()
