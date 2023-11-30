template = '''Given below are the table structures in employees database raw schema in mysql database
   employees (
      emp_no      INT             NOT NULL,
      birth_date  DATE            NOT NULL,
      first_name  VARCHAR(14)     NOT NULL,
      last_name   VARCHAR(16)     NOT NULL,
      gender      ENUM ("M","F")  NOT NULL,
      hire_date   DATE            NOT NULL
   );
   departments (
      dept_no     CHAR(4)         NOT NULL,
      dept_name   VARCHAR(40)     NOT NULL
   );
   dept_manager (
      emp_no       INT             NOT NULL,
      dept_no      CHAR(4)         NOT NULL,
      from_date    DATE            NOT NULL,
      to_date      DATE            NOT NULL
   ); 
   dept_emp (
       emp_no      INT             NOT NULL,
       dept_no     CHAR(4)         NOT NULL,
       from_date   DATE            NOT NULL,
       to_date     DATE            NOT NULL
   );
   titles (
       emp_no      INT             NOT NULL,
       title       VARCHAR(50)     NOT NULL,
       from_date   DATE            NOT NULL
   ); 
   salaries (
       emp_no      INT             NOT NULL,
       salary      INT             NOT NULL,
       from_date   DATE            NOT NULL,
       to_date     DATE            NOT NULL
   );

        take user questions and response back with sql query.
       example: 
       human: give me the list of employees who are above 18 years of age
       AI: select * from employees.employees where birth_date > DATE_SUB(birth_date, INTERVAL 18 year);
    
       example: 
       human: give me the details of the employee who is the eldest
       AI: select * from employees.employees where birth_date = (select min(birth_date) from employees.employees);
    
       example: 
       human: give me the details of the employee who is the youngest
       AI: select * from employees.employees where birth_date = (select max(birth_date) from employees.employees);
    
       example: 
       human: give me the names of the male employees whose department no is d004
       AI: select e.first_name, e.last_name from employees.employees e join employees.dept_manager dm 
       on e.emp_no = dm.emp_no where e.gender = "M" and dm.dept_no = "d004"
    
      example: 
      human: give me the names of the female employees who work in Development Department
      AI: SELECT e.first_name, e.last_name from employees.employees e join employees.dept_emp de on 
      de.emp_no = e.emp_no join employees.departments d on d.dept_no = de.dept_no 
      where d.dept_name = "Development" and e.gender = "M"
    
      example: 
      human: give me the first name, last name, department name and gender of the employee who was recruited last in the firm
      AI: SELECT d.dept_name, e.first_name, e.last_name, e.gender from employees.departments d 
      join employees.dept_emp de on d.dept_no = de.dept_no join employees.employees e on e.emp_no = de.emp_no
      where e.hire_date = (select max(e.hire_date) from employees.employees);
    
      example: 
      human: give the names of all the departments
      AI: SELECT dept_name from employees.departments;
        
    
    conversation history: {history}
    human: {input}
    AI:
'''
