import _sqlite3

connection = _sqlite3.connect('nedv.db')
cursor = connection.cursor()
cursor.execute("""
    create table offers_v4
    (
        descr text
        , floor text
        , price_1 text
        , per_m2_1 text 
        , price_2 text 
        , per_m2_2 text 
        , opn_dt text
        , lenght text
        , cls_dt text 
    )
    """)
connection.close()