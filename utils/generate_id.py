# 新用户生成随机至少5位最多8位的字符串数字user_id
import random
import string

def generate_id():
  return "".join(random.choices(string.digits, k=random.randint(5, 8)))