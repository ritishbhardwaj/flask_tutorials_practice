import mysql.connector


class calculating_tool_model:
    
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="Enc@psul@t!0n",database="flaskapitutorial")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("successful")
        
        except:
            print("not successfully connected")
                
    
    
    def convertingSystemLogicModel(self,data:dict):
        
        
        print(data)
        keywords=list(data.keys())[0]
        values=list(data.values())[0]
        
        
        
        return "model"