import pymysql

# db 연결
def dbconnect():
    conn = pymysql.connect(host='codingtest.brique.kr', user='codingtest', password='12brique!@', db='employees',
                               charset='utf8')
    return conn


def search_data(conn):
    cur = conn.cursor()
    sql = "SELECT e.emp_no,e.first_name,e.last_name,e.gender,e.hire_date,d.dept_name,t.title,max(s.salary) FROM employees AS e JOIN dept_emp AS de ON e.emp_no = de.emp_no  JOIN departments AS d ON d.dept_no = de.dept_no  JOIN titles AS t ON t.emp_no = e.emp_no  JOIN salaries AS s ON e.emp_no = s.emp_no where hire_date>='2000-01-01' GROUP BY e.emp_no,e.first_name,e.last_name,e.gender,e.hire_date,d.dept_name,t.title"
    cur.execute(sql)
    results = cur.fetchall()
    
    for i in results:
        print(i)
def main():
    conn = dbconnect() # DB연결
    search_data(conn)


if __name__ == '__main__':
    main()
