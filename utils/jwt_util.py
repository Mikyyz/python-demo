# 生成token & 解析token
import jwt
from datetime import datetime, timezone
from app.config.settings import SECRET_KEY

# 生成token
def generate_token(user_id):
  payload = {
    "user_id": user_id,
    "exp": datetime.now(timezone.utc) + datetime.timedelta(days=7),
  }
  token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
  return token

# 解析token
def parse_token(token):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return payload
  except jwt.ExpiredSignatureError:
    return None