from passlib.hash import bcrypt
from cryptography.fernet import Fernet

class Psswrd:
    def __init__(self, password):
        if not isinstance(password,str):
            raise ValueError(f"Psswrd most be str: {type(password)}")
        
        if password == "crypt":
            self.clave = Fernet.generate_key()
            self.fernet = Fernet(self.clave)
            with open("clave.key", "wb") as f:
                f.write(self.clave)
        
        if password != 'hashed' and password != 'crypt':
            self.password = password
        self.type = password

    def encrypt(self, name):
        if self.type == "crypt":
            
            self.password = self.fernet.encrypt(name.encode())
            return self.password
        elif self.type == "hashed":
            hash = bcrypt.hash(name)
            self.password = hash
            return hash
        
    
    
    def verify(self, passw):
        
        if self.type == "crypt":
            raise ValueError("Function only works with hashed passwords")
        return bcrypt.verify(passw, self.password)
    @property 
    def fernet(self):
        return self._fernet
    @fernet.setter
    def fernet(self,fernet):
        
        self._fernet = fernet
    @property
    def clave(self):
        return self._clave
    @clave.setter
    def clave(self,clave):
        self._clave = clave

def decrypt(code, fernet_key):
    fernet = Fernet(fernet_key)
    return fernet.decrypt(code).decode()

def main():
    pp = Psswrd("crypt")
    con = pp.encrypt("hola")
    print(con)
    print(pp.fernet)
    print(pp.clave)
    print(decrypt(con, pp.clave))
if __name__ == "__main__":
    main()