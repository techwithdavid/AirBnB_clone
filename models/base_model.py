import uuid
import datetime

class BaseModel:

    def __init__(self, *args, **kwargs):

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    kwargs[key] = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
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
