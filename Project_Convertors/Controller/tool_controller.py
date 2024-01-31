from app import app


from models.tool_models import calculating_tool_model

obj=calculating_tool_model()


from flask import request
@app.route('/convert/kgTogm')
@app.route('/convert',methods=["POST"])
def calculating_tool_controller():
    res=request.form
    # print(res)
    return obj.convertingSystemLogicModel(res)