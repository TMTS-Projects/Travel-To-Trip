import DbClasses
from settings import sessionRepo


session=sessionRepo()
Type=DbClasses.type_Repository()
Type.type_name="Classic"
session.add(Type)
session.commit()
session.close()







