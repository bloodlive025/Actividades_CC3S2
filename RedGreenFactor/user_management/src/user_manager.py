import bcrypt,re
import json

class UserAlreadyExistsError(Exception):
    """Excepción lanzada cuando un usuario ya existe."""
    pass

class UserNotFoundError(Exception):
    """Excepción lanzada cuando un usuario no es encontrado."""
    pass

class IncorrectPasswordError(Exception):
    """Excepción lanzada cuando la contraseña proporcionada es incorrecta."""
    pass


class AccountLockedError(Exception):
    """Excepción lanzada cuando la cuenta está bloqueada."""
    pass
class InvalidPasswordError(Exception):
    """Excepción lanzada cuando una contraseña no cumple con las políticas de seguridad."""
    pass

class PermissionError(Exception):
    """Excepción lanzada cuando un usuario no tiene permisos para realizar una acción."""
    pass


class UserManager:
    """Clase para gestionar usuarios con funcionalidades de agregar y autenticar."""
    VALID_ROLES = {"admin", "usuario"}  # Roles permitidos
    def __init__(self,max_failed_attempts=100):
        """Inicializa el gestor de usuarios con un diccionario vacío."""
        self.users = {}
        self.roles = {}  # Diccionario para almacenar roles de usuarios
        self.failed_attempts = {}
        self.locked_accounts = {}
        self.max_failed_attempts = max_failed_attempts
    
    def requires_role(required_role):
        def decorator(func):
            def wrapper(self, actor_username, *args, **kwargs):
                if not self.user_exists(actor_username):
                    raise UserNotFoundError(f"El usuario '{actor_username}' no existe.")
                actor_role = self.get_role(actor_username)
                if actor_role != required_role:
                    print(f"DEBUG: Lanzando PermissionError para {actor_username}")  # Depuración
                    raise PermissionError(f"El usuario '{actor_username}' no tiene permisos para esta acción.")
                return func(self, actor_username, *args, **kwargs)
            return wrapper
        return decorator

    def add_user(self, username, password):
        """
        Agrega un nuevo usuario con nombre de usuario y contraseña.
        
        :param username: Nombre de usuario.
        :param password: Contraseña del usuario.
        :raises UserAlreadyExistsError: Si el usuario ya existe.
        """
        if self.user_exists(username):
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        if not self._is_valid_password(password):
            raise InvalidPasswordError("La contraseña no cumple con los requisitos de seguridad.")
        hashed_password = self._hash_password(password)
        self.users[username] = hashed_password
    
    def authenticate_user(self, username, password):
        """
        Autentica a un usuario verificando su contraseña.
        
        :param username: Nombre de usuario.
        :param password: Contraseña a verificar.
        :return: True si la contraseña es correcta, False de lo contrario.
        :raises UserNotFoundError: Si el usuario no existe.
        """
        if not self.user_exists(username):
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        
        if self.is_account_locked(username):
            raise AccountLockedError(f"La cuenta del usuario '{username}' está bloqueada.")
        if self._check_password(password, self.users[username]):
            self.failed_attempts[username] = 0  # Reiniciar contadores tras éxito
            return True
        else:
            self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1
            if self.failed_attempts[username] == self.max_failed_attempts:
                self.locked_accounts[username] = True
            elif self.failed_attempts[username] >self.max_failed_attempts:
                raise AccountLockedError(f"La cuenta del usuario '{username}' está bloqueada.")
            return False
    
    def user_exists(self, username):
        """
        Verifica si un usuario existe.
        
        :param username: Nombre de usuario.
        :return: True si el usuario existe, False de lo contrario.
        """
        return username in self.users
    
    def _hash_password(self, password):
        """
        Genera un hash seguro para una contraseña.
        
        :param password: Contraseña en texto plano.
        :return: Hash de la contraseña.
        """
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def _check_password(self, password, hashed):
        """
        Verifica si una contraseña coincide con su hash.
        
        :param password: Contraseña en texto plano.
        :param hashed: Hash de la contraseña almacenado.
        :return: True si coincide, False de lo contrario.
        """
        return bcrypt.checkpw(password.encode(), hashed)
     

    def delete_user(self, username):
        """
        Elimina un usuario del sistema.
        
        :param username: Nombre de usuario a eliminar.
        :raises UserNotFoundError: Si el usuario no existe.
        """
        if not self.user_exists(username):
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        del self.users[username]
    
    def list_users(self):
        """
        Retorna una lista de todos los nombres de usuario registrados.
        
        :return: Lista de nombres de usuario.
        """
        return list(self.users.keys())
###############################################################################################
###############################################################################################

    def assign_role(self, username, role):
        """
        Asigna un rol a un usuario existente.
        
        :param username: Nombre de usuario.
        :param role: Rol a asignar (e.g., "admin", "usuario").
        :raises UserNotFoundError: Si el usuario no existe.
        """
        if not self.user_exists(username):
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        if role not in self.VALID_ROLES:
            raise ValueError(f"Rol '{role}' no es válido. Roles permitidos: {self.VALID_ROLES}")
        self.roles[username] = role
    
    def get_role(self, username):
        """
        Obtiene el rol asignado a un usuario.
        
        :param username: Nombre de usuario.
        :return: Rol del usuario. Retorna "usuario" por defecto si no se ha asignado ninguno.
        :raises UserNotFoundError: Si el usuario no existe.
        """
        if not self.user_exists(username):
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        return self.roles.get(username, "usuario")
    

############################################################################################################
############################################################################################################
    def reset_password(self, username, old_password, new_password):
        """
        Restablece la contraseña de un usuario.
        
        :param username: Nombre de usuario.
        :param old_password: Contraseña actual.
        :param new_password: Nueva contraseña a establecer.
        :raises UserNotFoundError: Si el usuario no existe.
        :raises IncorrectPasswordError: Si la contraseña actual es incorrecta.
        """
        if not self.user_exists(username):
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        if not self.authenticate_user(username, old_password):
            raise IncorrectPasswordError("La contraseña proporcionada es incorrecta.")
        if not self._is_valid_password(new_password):
            raise InvalidPasswordError("La contraseña no cumple con los requisitos de seguridad.")
        hashed_new_password = self._hash_password(new_password)
        self.users[username] = hashed_new_password

################################################################################################################
################################################################################################################

    def is_account_locked(self, username):
        """
        Verifica si la cuenta de un usuario está bloqueada.
        
        :param username: Nombre de usuario.
        :return: True si está bloqueada, False de lo contrario.
        """
        return self.locked_accounts.get(username, False)
    
    def unlock_account(self, username):
        """
        Desbloquea la cuenta de un usuario.
        
        :param username: Nombre de usuario.
        :raises UserNotFoundError: Si el usuario no existe.
        """
        if not self.user_exists(username):
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        self.locked_accounts[username] = False
        self.failed_attempts[username] = 0

#########################################################################################################
#########################################################################################################
    def _is_valid_password(self, password):
        """
        Verifica si una contraseña cumple con las políticas de seguridad.
        
        Requisitos:
        - Al menos 8 caracteres.
        - Al menos una letra mayúscula.
        - Al menos una letra minúscula.
        - Al menos un número.
        - Al menos un carácter especial.
        
        :param password: Contraseña a verificar.
        :return: True si es válida, False de lo contrario.
        """
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True
    
##########################################################################################################
##########################################################################################################


    def save_to_file(self, filepath):
        """
        Guarda los usuarios y sus datos en un archivo JSON.
        
        :param filepath: Ruta del archivo donde se guardarán los datos.
        """
        data = {
            "users": {username: hashed.decode('utf-8') for username, hashed in self.users.items()},
            "roles": self.roles,
            "failed_attempts": self.failed_attempts,
            "locked_accounts": self.locked_accounts
        }
        with open(filepath, 'w') as f:
            json.dump(data, f)

    def load_from_file(self, filepath):
        """
        Carga los usuarios y sus datos desde un archivo JSON.
        
        :param filepath: Ruta del archivo desde donde se cargarán los datos.
        :raises FileNotFoundError: Si el archivo no existe.
        """
        with open(filepath, 'r') as f:
            data = json.load(f)
            self.users = {username: hashed.encode('utf-8') for username, hashed in data.get("users", {}).items()}
            self.roles = data.get("roles", {})
            self.failed_attempts = data.get("failed_attempts", {})
            self.locked_accounts = data.get("locked_accounts", {})

######################################################################################################################
######################################################################################################################

    @requires_role("admin")
    def delete_user_as(self, actor_username, target_username):
        """
        Elimina un usuario como otro usuario con permisos.
        
        :param actor_username: Nombre de usuario que intenta eliminar.
        :param target_username: Nombre de usuario que será eliminado.
        :raises UserNotFoundError: Si el actor o el objetivo no existen.
        :raises PermissionError: Si el actor no tiene permisos para eliminar usuarios.
        """
        if not self.user_exists(target_username):
            raise UserNotFoundError(f"El usuario '{target_username}' no existe.")
        self.delete_user(target_username)

    
