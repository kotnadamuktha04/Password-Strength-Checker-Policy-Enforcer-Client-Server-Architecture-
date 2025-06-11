import sqlite3

conn = sqlite3.connect('password_log.db')
c = conn.cursor()
c.execute('SELECT * FROM password_logs')

rows = c.fetchall()
print("\n🔍 Password Generation Logs:")
for row in rows:
    print(row)

conn.close()
