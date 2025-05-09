import pyodbc

def read_sql_query(sql, server, database, username, password):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'+
        'SERVER=DESKTOP-BOHR9BN\MSSQLSERVER02;'+
        'DATABASE=master;'+
        'Trusted_Connection=True'
    )

    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows
