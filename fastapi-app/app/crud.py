from sqlalchemy.orm import Session
from sqlalchemy.sql import text

def convert_result(res):
    return [{c:getattr(r,c) for c in res.keys()} for r in res]

def get_fruit(db: Session):
    stmt = f"""
        SELECT * FROM fruit
    """
    res = db.execute(text(stmt))
    print(res)
    # print(res.keys())
    # for r in res:
    #     print(r)
    result = convert_result(res)
    print(result)
    return result

