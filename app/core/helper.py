from app.core.response_model import ResponseModel
def success(data=None, message='success'):
    return ResponseModel(
        status_code=0,
        msg=message,
        data=data
    )

def error(message='error', code=400):
    return ResponseModel(
        status_code=code,
        msg=message,
        data=None
    )