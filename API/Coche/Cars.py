class Cars:

    id=""
    precio=0
    dias=0

    def __init__(self,id, precio, dias):
        self.id=id
        self.precio=precio
        self.dias=dias

    def get_id(self):
        return self.id

    def get_precio(self):
        return self.precio
        
    def get_dias(self):
        return self.dias
