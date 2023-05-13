from models import base_model

class FileStorage:

    __file_path = 'database.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dic = {}
        for key, value in FileStorage.__objects.items():
            obj_dic[key] = value.to_dict()
        
        path = FileStorage.__file_path
        with open(path, w) as f:
            json.dump(obj_dic, f, indent=2)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = json.load(f)
