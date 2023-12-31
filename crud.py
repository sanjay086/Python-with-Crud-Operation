import mysql.connector

# Establish the connection
mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="sanjay_db")

# Create a cursor object to interact with the database
mysqlcursor = mysqldb.cursor()

# Execute the CREATE TABLE statement
# mysqlcursor.execute("CREATE TABLE studentrecord (rollno INT, name VARCHAR(50), marks INT)")

# Insert into Table
'''try:

    mysqlcursor.execute("INSERT INTO studentrecord(rollno, name, marks) Values(2, 'Ayansh Raj', 96)")
    # Commit your changes
    mysqldb.commit()
    print("record inserted into the table")
    
except:
    mysqldb.rollback()

    # Close the connection
    mysqldb.close()
'''

# Display Record

'''try:
    mysqlcursor.execute("SELECT * FROM studentrecord WHERE rollno = 1")
    result = mysqlcursor.fetchall()
    for i in result:
        roll = i[0]
        name = i[1]
        marks = i[2]
        print(roll, name, marks)
except:
    print("Some issue in the code")
mysqlcursor.close()   
'''
# To Update the Record 
'''try:
    mysqlcursor.execute("UPDATE studentrecord SET name = 'Sanjeev' WHERE rollno = 1") 
    mysqldb.commit()
    print("Record Updated Successfully")
except:
    mysqldb.rollback()  
'''
# To Delete the Record 

try:
    mysqlcursor.execute("DELETE FROM studentrecord WHERE rollno = 1") 
    mysqldb.commit()
    print("Record Deleted Successfully")
except:
    mysqldb.rollback()             