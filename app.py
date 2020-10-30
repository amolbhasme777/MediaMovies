from sqlalchemy import  create_engine, Column, Integer, String, Date

import requests
from datetime import datetime

class MediAppDetails():

    def mySqlConnection():
        engine = create_engine('mysql+mysqlconnector://pyuser:root@localhost:3306/sqlalchemy')
        engine.connect()

        __tablename__ = "theater_Movies"
        Title = Column(String(50))
        Release_year = Column(Date(50))
        Geners = Column(String(50))
        Description = Column(String(100))
        Theater = Column(String(100))

        __tablename__ = "tv_Movies"
        Title = Column(String(50))
        Release_year = Column(String(50))
        Geners = Column(String(50))
        Description = Column(String(100))
        Channel= Column(String(100))
    
        def __repr__(self):
            return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                self.name, self.fullname, self.nickname)

        line_up_id="USA-TX42500-X"
        date_time=datetime.now().isoformat()
        print(date_time)

        print(engine)
        req1= requests.get("http://data.tmsapi.com/v1.1/movies/showings?startDate=2020-10-29&zip=78701&api_key=qu2a3vcggtdmxm88c4fjpsmj")
        req2 = requests.get("http://data.tmsapi.com/v1.1/movies/airings?lineupId=USA-TX42500-X&startDateTime=2020-10-29T17%3A30Z&endDateTime=2020-10-29&api_key=qu2a3vcggtdmxm88c4fjpsmj")
        print(req1.status_code)
        if req1.status_code==200:
            data=req1.text
            print(data)
        if req2.status_code==200:
            data=req2.text
            print(data)



mySqlConnection()



