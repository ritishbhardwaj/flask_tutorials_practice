from app import app 

from model.user_model import user_model
                    # this is filename    # this is class name
                    
obj=user_model()   #creating instance of the class

@app.route('/user/getall/<id>')
@app.route('/user/getall')
def user_getall_controller(id=None):
    print("<<<<<<<<<<<<<<<<",id)
    if id==None:
        return obj.user_getall_model()
    else:
        return obj.user_getuserwithid(id)


from flask import request
@app.route('/user/addone',methods=["POST"])
def user_addone_controller():
    data=request.form
    return obj.user_addone_model(data)


@app.route('/user/update',methods=["PUT"])
def user_update_controller():
    data=request.form
    return obj.user_update_model(data)


@app.route("/user/delete/<id>",methods=["DELETE"])
def user_delete_controller(id):
    
    return obj.user_delete_model(id)
