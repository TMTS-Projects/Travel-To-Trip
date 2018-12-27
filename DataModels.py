
class BaseModel():
    isFailure = False
    message = ""


class List_Menu_Details(BaseModel):
    menuList = ""

    def __init__(self):
        self.isFailure = False
        self.message = ""
        self.menuList = list()



