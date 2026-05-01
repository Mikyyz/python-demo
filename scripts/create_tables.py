# 创建数据库表
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.database import Base, engine
from app.api.v1.modules.user.model import User

Base.metadata.create_all(bind=engine)