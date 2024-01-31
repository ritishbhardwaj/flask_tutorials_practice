import mysql.connector
import json

from flask import make_response

class user_model:
    
    def __init__(self) -> None:
        #connections establishment code in order to get data from the db
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Enc@psul@t!0n",database="flaskapitutorial")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connection Successful")
        except:
            print("some error")
    
    def user_getuserwithid(self,id=None):
        try:
            self.cur.execute("SELECT * FROM users where id="+id)
            result=self.cur.fetchone()
            
            print(result)
            
            if len(result)>0: 
                return {'payload':result}    #iske saath hum dictionary ke saare format ko in string format mei change krr dete hai
            #or       
            # return f'{result}'
            else:
                return {'msg': "No Data Found"}
        except Exception as e:
            print(e)
            res=make_response({'msg': "No Data Found"},204).headers["Acess-Control-Allow-Origin"]='*'
            return res
            
    def user_getall_model(self):
        print(">>>>>>>>>>>>")
        #query execution code
        self.cur.execute("SELECT * FROM users")
        result=self.cur.fetchall()
        
        print(result)
        
        if len(result)>0: 
            return json.dumps(result)    #iske saath hum dictionary ke saare format ko in string format mei change krr dete hai
        #or       
        # return f'{result}'
        else:
            return "No Data Found"
    
    def user_addone_model(self,data):
        #query execution code
        # self.cur.execute("SELECT * FROM users")
        # print(data,"model")
        
        self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        
        return "user created succesfully"
    
    def user_update_model(self,data):
        # print(data)
        # print(data['id'])
        # print("hello")
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}', role='{data['role']}', password='{data['password']}' WHERE id='{data['id']}' ")
        
        # to check whether the data is updated or not
        # and for that i have a good technique known as rowcount
        # and if rowcount> 0 it means user is updated successfully
        
        if self.cur.rowcount>0:
            return "user updated succesfully"
        else:
            return "nothing to update"
    
    def user_delete_model(self,id):
        
        self.cur.execute(f"DELETE FROM users WHERE id='{id}'")
        
        if self.cur.rowcount>0:
            return "user deleted successfully"
        else:
            return "nothing to delete"