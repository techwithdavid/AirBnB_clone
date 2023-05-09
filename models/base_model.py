import uuid
import datetime

class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        inst_to_dict = dict(self.__dict__)

        inst_to_dict['__class__'] = self.__class__.__name__
        inst_to_dict['created_at'] = self.created_at.isoformat()
        inst_to_dict['updated_at'] = self.updated_at.isoformat()
        
        return inst_to_dict


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model.to_dict())
