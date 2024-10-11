import sqlite3

def create_connection():
    connection = sqlite3.connect("memory.db")
    return connection

def get_questions_and_answers():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM quesandans")
    return cur.fetchall()

def insert_question_and_answer(questions,answers):
    con = create_connection()
    cur = con.cursor()
    query = "INSERT INTO quesandans VALUES('"+questions+"','"+answers+"')"
    cur.execute(query)
    con.commit()

def get_answer_from_memory(questions):
    rows = get_questions_and_answers()
    answer = ""
    for row in rows:
        if row[0] is not None and row[0].lower() in questions.lower():
            answer = row[1]
            break
    return answer

def get_name():
    con = create_connection()
    cur = con.cursor()
    query = "select value from memory where name= 'assistant_name'"
    cur.execute(query)
    return cur.fetchall()[0][0]


def update_name(new_name):
    con = create_connection()
    cur = con.cursor()
    query = "update memory set value = '"+new_name+"' where name = 'assistant_name'"
    cur.execute(query)
    con.commit()

def update_last_seen(last_seen_date):
    con = create_connection()
    cur = con.cursor()
    query = "UPDATE memory SET value = ? WHERE name = 'last_seen_date'"
    cur.execute(query, (last_seen_date,))
    con.commit()

def get_last_seen():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM memory WHERE name = 'last_seen_date'"
    cur.execute(query)
    result = cur.fetchone()
    return str(result[0]) if result else None
