from app import app, psql

class Users(object):
    def __init__(self, id_num=None, f_name=None, l_name=None, course=None, year=None, gender=None):
        self.id_num = id_num
        self.f_name = f_name
        self.l_name = l_name
        self.course = course
        self.year = year
        self.gender = gender

    def add(self):
        cursor = psql.connection.cursor()

        sql = "INSERT INTO studentlist(id_num, f_name, l_name, course, year, gender) \
                VALUES('%s','%s','%s','%s','%s','%s')" % \
              (self.id_num, self.f_name, self.l_name, self.course, self.year, self.gender)

        cursor.execute(sql)
        psql.connection.commit()

    def delete(self):
        cursor = psql.connection.cursor()
        sql = "DELETE FROM studentlist WHERE id_num = '%s'" % (self.id_num)
        cursor.execute(sql)
        psql.connection.commit()

    def update(self):
        cursor = psql.connection.cursor()
        sql = "UPDATE studentlist SET f_name = '%s', l_name = '%s', course = '%s', year = '%s', gender = '%s' WHERE id_num = '%s'" % (self.f_name, self.l_name, self.course, self.year, self.gender, self.id_num)
        cursor.execute(sql)
        psql.connection.commit()


    def search(self):
        cursor = psql.connection.cursor()
        sql = "SELECT * FROM studentlist WHERE id_num = '%s'" % (self.id_num)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


    @classmethod
    def all(cls):
        cursor = psql.connection.cursor()
        sql = "SELECT * from studentlist"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

class Course(object):
    def __init__(self, c_id=None, c_name=None, c_college=None):
        self.c_id = c_id
        self.c_name = c_name
        self.c_college = c_college

    def cadd(self):
        cursor = psql.connection.cursor()

        sql = "INSERT INTO courselist(c_id, c_name, c_college) \
                VALUES('%s','%s','%s')" % \
              (self.c_id, self.c_name, self.c_college)

        cursor.execute(sql)
        psql.connection.commit()

    def cdelete(self):
        cursor = psql.connection.cursor()
        sql = "DELETE FROM courselist WHERE c_id = '%s'" % (self.c_id)
        cursor.execute(sql)
        psql.connection.commit()

    def cupdate(self):
        cursor = psql.connection.cursor()
        sql = "UPDATE courselist SET c_id = '%s', c_name = '%s', c_college = '%s' WHERE c_id = '%s'" % (self.c_id, self.c_name, self.c_college, self.c_id)
        cursor.execute(sql)
        psql.connection.commit()


    def csearch(self):
        cursor = psql.connection.cursor()
        sql = "SELECT * FROM courselist WHERE c_id = '%s'" % (self.c_id)
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


    @classmethod
    def all(cls):
        cursor = psql.connection.cursor()
        sql = "SELECT * from courselist"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


