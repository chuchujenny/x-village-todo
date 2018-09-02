# 模型 - 負責和資料庫互動，儲存資料(網路上也是這樣寫)
## 建立資料表欄位
from app import db


class Record(db.Model):
    # 設定 primary_key
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(120), nullable=True)
    date = db.Column(db.String(120), nullable=True)
