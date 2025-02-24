import pytest
import tempfile
import os

from user_manager import UserManager, UserAlreadyExistsError, UserNotFoundError,IncorrectPasswordError,AccountLockedError,InvalidPasswordError,PermissionError

def test_agregar_usuario_exitoso():
    # Arrange
    manager = UserManager()
    username = "kapumota"
    password = "Securepassword123."
    
    # Act
    manager.add_user(username, password)
    
    # Assert
    assert manager.user_exists(username)

def test_agregar_usuario_existente():
    # Arrange
    manager = UserManager()
    username = "kapumota"
    password = "Securepassword123."
    manager.add_user(username, password)
    
    # Act & Assert
    with pytest.raises(UserAlreadyExistsError) as exc_info:
        manager.add_user(username, "newpassword")
    assert str(exc_info.value) == "El usuario 'kapumota' ya existe."

def test_autenticar_usuario_exitoso():
    # Arrange
    manager = UserManager()
    username = "chaloZeta"
    password = "Securepassword123."
    manager.add_user(username, password)
    
    # Act
    resultado = manager.authenticate_user(username, password)
    
    # Assert
    assert resultado is True

def test_autenticar_usuario_con_contraseña_incorrecta():
    # Arrange
    manager = UserManager()
    username = "chaloZeta"
    password = "Securepassword123."
    manager.add_user(username, password)
    
    # Act
    resultado = manager.authenticate_user(username, "wrongpassword")
    
    # Assert
    assert resultado is False

def test_autenticar_usuario_inexistente():
    # Arrange
    manager = UserManager()
    username = "ghostuser"
    password = "Securepassword123."
    
    # Act & Assert
    with pytest.raises(UserNotFoundError) as exc_info:
        manager.authenticate_user(username, password)
    assert str(exc_info.value) == "El usuario 'ghostuser' no existe."

#################################################################################################################
#################################################################################################################

def test_eliminar_usuario_exitoso():
    # Arrange
    manager = UserManager()
    username = "usuarioEliminar"
    password = "Securepassword123."
    manager.add_user(username, password)
    
    # Act
    manager.delete_user(username)
    
    # Assert
    assert not manager.user_exists(username)

def test_eliminar_usuario_inexistente():
    # Arrange
    manager = UserManager()
    username = "usuarioInexistente"
    
    # Act & Assert
    with pytest.raises(UserNotFoundError) as exc_info:
        manager.delete_user(username)
    assert str(exc_info.value) == f"El usuario '{username}' no existe."

#########################################################################################################################
#########################################################################################################################

def test_listar_usuarios_con_usuarios():
    # Arrange
    manager = UserManager()
    usuarios = ["usuario1", "usuario2", "usuario3"]
    for usuario in usuarios:
        manager.add_user(usuario, "Securepassword123.")
    
    # Act
    lista = manager.list_users()
    
    # Assert
    assert set(lista) == set(usuarios)

def test_listar_usuarios_sin_usuarios():
    # Arrange
    manager = UserManager()
    
    # Act
    lista = manager.list_users()
    
    # Assert
    assert lista == []


##################################################################################################################

def test_asignar_rol_exitoso():
    # Arrange
    manager = UserManager()
    username = "usuarioConRol"
    password = "Securepassword123."
    manager.add_user(username, password)
    rol = "admin"
    
    # Act
    manager.assign_role(username, rol)
    
    # Assert
    assert manager.get_role(username) == rol

def test_asignar_rol_usuario_inexistente():
    # Arrange
    manager = UserManager()
    username = "usuarioInexistente"
    rol = "admin"
    
    # Act & Assert
    with pytest.raises(UserNotFoundError) as exc_info:
        manager.assign_role(username, rol)
    assert str(exc_info.value) == f"El usuario '{username}' no existe."

def test_obtener_rol_por_defecto():
    # Arrange
    manager = UserManager()
    username = "usuarioSinRol"
    password = "Securepassword123."
    manager.add_user(username, password)
    
    # Act
    rol = manager.get_role(username)
    
    # Assert
    assert rol == "usuario"


def test_asignar_rol_invalido():
    # Arrange
    manager = UserManager()
    username = "usuarioConRolInvalido"
    password = "Securepassword123."
    manager.add_user(username, password)
    rol = "superadmin"  # Rol no válido
    
    # Act & Assert
    with pytest.raises(ValueError) as exc_info:
        manager.assign_role(username, rol)
    assert str(exc_info.value) == f"Rol '{rol}' no es válido. Roles permitidos: {manager.VALID_ROLES}"
######################################################################################
######################################################################################

def test_restablecer_contraseña_exitoso():
    # Arrange
    manager = UserManager()
    username = "usuarioReset"
    old_password = "Oldpassword123."
    new_password = "Newpassword123."
    manager.add_user(username, old_password)
    
    # Act
    manager.reset_password(username, old_password, new_password)
    
    # Assert
    assert manager.authenticate_user(username, new_password) is True
    assert manager.authenticate_user(username, old_password) is False

def test_restablecer_contraseña_contraseña_incorrecta():
    # Arrange
    manager = UserManager()
    username = "usuarioResetIncorrecto"
    old_password = "Oldpassword123."
    new_password = "Newpassword123."
    manager.add_user(username, old_password)
    
    # Act & Assert
    with pytest.raises(IncorrectPasswordError) as exc_info:
        manager.reset_password(username, "Wrongpassword123.", new_password)
    assert str(exc_info.value) == "La contraseña proporcionada es incorrecta."

def test_restablecer_contraseña_usuario_inexistente():
    # Arrange
    manager = UserManager()
    username = "usuarioInexistenteReset"
    old_password = "Oldpassword123."
    new_password = "Newpassword123."
    
    # Act & Assert
    with pytest.raises(UserNotFoundError) as exc_info:
        manager.reset_password(username, old_password, new_password)
    assert str(exc_info.value) == f"El usuario '{username}' no existe."

######################################################################################################
######################################################################################################
def test_bloquear_cuenta_despues_de_intentos_fallidos():
    # Arrange
    manager = UserManager(max_failed_attempts=3)
    username = "usuarioBloqueo"
    password = "Newpassword123."
    manager.add_user(username, password)
    
    # Act & Assert
    for _ in range(3):
        resultado = manager.authenticate_user(username, "Wrongpassword123.")
        assert resultado is False
    
    with pytest.raises(AccountLockedError) as exc_info:
        print(manager.failed_attempts)
        manager.authenticate_user(username, password)
    assert str(exc_info.value) == f"La cuenta del usuario '{username}' está bloqueada."

def test_no_puede_autenticar_usuario_bloqueado():
    # Arrange
    manager = UserManager(max_failed_attempts=3)
    username = "usuarioBloqueado"
    password = "Newpassword123."
    manager.add_user(username, password)
    for _ in range(3):
        manager.authenticate_user(username, "Wrongpassword123.")
    
    # Act & Assert
    with pytest.raises(AccountLockedError):
        manager.authenticate_user(username, password)

def test_desbloquear_cuenta_exitoso():
    # Arrange
    manager = UserManager(max_failed_attempts=3)
    username = "usuarioDesbloqueo"
    password = "Password123."
    manager.add_user(username, password)
    for _ in range(3):
        manager.authenticate_user(username, "wrongpassword")
    
    # Act
    manager.unlock_account(username)
    
    # Assert
    assert manager.is_account_locked(username) is False
    assert manager.authenticate_user(username, password) is True

def test_desbloquear_cuenta_usuario_inexistente():
    # Arrange
    manager = UserManager()
    username = "usuarioInexistenteDesbloquear"
    
    # Act & Assert
    with pytest.raises(UserNotFoundError) as exc_info:
        manager.unlock_account(username)
    assert str(exc_info.value) == f"El usuario '{username}' no existe."
#############################################################################################
#############################################################################################
def test_agregar_usuario_con_contraseña_valida():
    # Arrange
    manager = UserManager()
    username = "usuarioConPasswordValida"
    password = "ValidPass1!"
    
    # Act
    manager.add_user(username, password)
    
    # Assert
    assert manager.user_exists(username)

def test_agregar_usuario_con_contraseña_invalida():
    # Arrange
    manager = UserManager()
    username = "usuarioConPasswordInvalida"
    password = "short"
    
    # Act & Assert
    with pytest.raises(InvalidPasswordError) as exc_info:
        manager.add_user(username, password)
    assert str(exc_info.value) == "La contraseña no cumple con los requisitos de seguridad."

def test_restablecer_contraseña_valida():
    # Arrange
    manager = UserManager()
    username = "usuarioResetValido"
    old_password = "OldValid1!"
    new_password = "NewValid2@"
    manager.add_user(username, old_password)
    
    # Act
    manager.reset_password(username, old_password, new_password)
    
    # Assert
    assert manager.authenticate_user(username, new_password) is True

def test_restablecer_contraseña_invalida():
    # Arranges
    manager = UserManager()
    username = "usuarioResetInvalido"
    old_password = "OldValid1!"
    new_password = "invalid"
    manager.add_user(username, old_password)
    
    # Act & Assert
    with pytest.raises(InvalidPasswordError) as exc_info:
        manager.reset_password(username, old_password, new_password)
    assert str(exc_info.value) == "La contraseña no cumple con los requisitos de seguridad."

##################################################################################################
##################################################################################################


def test_guardar_y_cargar_usuarios():
    # Arrange
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        filepath = tmp_file.name
    try:
        manager = UserManager()
        usuarios = {
            "usuario1": "Password1!",
            "usuario2": "Password2@"
        }
        for username, password in usuarios.items():
            manager.add_user(username, password)
        
        # Act
        manager.save_to_file(filepath)
        nuevo_manager = UserManager()
        nuevo_manager.load_from_file(filepath)
        
        # Assert
        for username in usuarios:
            assert nuevo_manager.user_exists(username)
            assert nuevo_manager.authenticate_user(username, usuarios[username]) is True
    finally:
        os.remove(filepath)

def test_cargar_usuarios_desde_archivo_inexistente():
    # Arrange
    manager = UserManager()
    filepath = "archivo_inexistente.json"
    
    # Act & Assert
    with pytest.raises(FileNotFoundError):
        manager.load_from_file(filepath)


#######################################################################################################
#######################################################################################################
def test_eliminar_usuario_como_admin():
    # Arrange
    manager = UserManager()
    admin_username = "adminUser"
    admin_password = "AdminPass1!"
    manager.add_user(admin_username, admin_password)
    manager.assign_role(admin_username, "admin")
    
    target_username = "usuarioEliminar"
    target_password = "Password1!"
    manager.add_user(target_username, target_password)
    
    # Act
    manager.delete_user_as(admin_username, target_username)
    
    # Assert
    assert not manager.user_exists(target_username)


def test_usuario_sin_permisos_no_puede_eliminar():
    # Arrange: Configurar el UserManager y agregar usuarios
    manager = UserManager()
    normal_username = "normalUser"
    normal_password = "NormalPass1!"
    manager.add_user(normal_username, normal_password)
    manager.assign_role(normal_username, "usuario")  # 🔹 No tiene rol "admin"
    
    target_username = "usuarioEliminar"
    target_password = "Password1!"
    manager.add_user(target_username, target_password)

    # Act & Assert: Intentar eliminar sin permisos debería lanzar PermissionError
    with pytest.raises(PermissionError) as exc_info:
        manager.delete_user_as(normal_username, target_username)

    # Verificar el mensaje de error
    assert str(exc_info.value) == f"El usuario '{normal_username}' no tiene permisos para esta acción."
def test_eliminar_usuario_como_admin_inexistente():
    # Arrange
    manager = UserManager()
    admin_username = "inexistenteAdmin"
    
    target_username = "usuarioEliminar"
    target_password = "Password1!"
    manager.add_user(target_username, target_password)
    
    # Act & Assert
    with pytest.raises(UserNotFoundError) as exc_info:
        manager.delete_user_as(admin_username, target_username)
    assert str(exc_info.value) == f"El usuario '{admin_username}' no existe."

