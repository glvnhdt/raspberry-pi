import psycopg2

conn = psycopg2.connect("dbname=project1 user=postgres password=postgres");
cur= conn.cursor();
cur.execute("INSERT INTO logins (login_name, login_time) VALUES ('via scrypt', now());");
conn.commit();

cur.execute("SELECT count(*) from logins");
print(cur.fetchone());

cur.close();
conn.close();

print("ended");
