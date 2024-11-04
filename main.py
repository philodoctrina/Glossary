import sqlite3

def edit():
    exit_edit = False
    while (False == exit_edit):
        edit = input('edit: ')

        if ('' == edit):
            exit_edit = True
            continue

        defn = input('defn: ')
        print()

        if ('' == defn):
            cursor.execute(f'DELETE FROM glossary WHERE word = "{edit}";')
            continue
    
        else:
            cursor.execute(f'UPDATE glossary SET defn = "{defn}" WHERE word = "{edit}";')

    return

connection = sqlite3.connect('bookshelf.db', autocommit=True)
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS glossary(word TEXT PRIMARY KEY, defn TEXT NOT NULL);')

exit_main = False
while (False == exit_main):
    word = input('word: ')
    
    if ('^' == word):
        edit()
        continue

    elif ('' == word):
        exit_main = True
        continue

    defn = cursor.execute(f'SELECT defn FROM glossary WHERE word = "{word}"').fetchone()
    
    if (None != defn):
        print(f'defn: {defn[0]}')
        print()
        continue

    else:
        defn = input('defn: ')
        print()

        if ('' == defn):
            continue

        cursor.execute(f'INSERT INTO glossary (word,defn) VALUES("{word}","{defn}");')

cursor.close()
connection.close()

print()
