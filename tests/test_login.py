# tests/test_login.py - Pruebas para US-001
# Sistema de Mejora Continua (SMC)

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.login import Usuario, validar_email, hashear_password, verificar_password, autenticar, calcular_metricas_mejora

def test_validar_email():
    """Prueba: US-001 - Validación de email"""
    assert validar_email("test@example.com") == True
    assert validar_email("test@example") == False
    assert validar_email("test@.com") == False
    assert validar_email("test@example.") == False
    print("✅ test_validar_email: PASADO")

def test_hashear_password():
    """Prueba: US-001 - Hashing de contraseña"""
    password = "Password123!"
    hash1 = hashear_password(password)
    hash2 = hashear_password(password)
    assert hash1 != hash2
    assert verificar_password(password, hash1) == True
    assert verificar_password("wrong", hash1) == False
    print("✅ test_hashear_password: PASADO")

def test_autenticar():
    """Prueba: US-001 - Autenticación"""
    usuario = Usuario(
        email="test@example.com",
        password_hash=hashear_password("Password123!"),
        nombre="Test User"
    )
    
    exito, mensaje = autenticar(usuario, "Password123!")
    assert exito == True
    assert mensaje == "Autenticación exitosa"
    
    exito, mensaje = autenticar(usuario, "WrongPassword")
    assert exito == False
    assert mensaje == "Credenciales inválidas"
    print("✅ test_autenticar: PASADO")

def test_autenticar_usuario_no_encontrado():
    """Prueba: US-001 - Usuario no encontrado"""
    exito, mensaje = autenticar(None, "Password123!")
    assert exito == False
    assert mensaje == "Usuario no encontrado"
    print("✅ test_autenticar_usuario_no_encontrado: PASADO")

def test_autenticar_contraseña_corta():
    """Prueba: US-001 - Contraseña corta"""
    usuario = Usuario(
        email="test@example.com",
        password_hash=hashear_password("Password123!"),
        nombre="Test User"
    )
    exito, mensaje = autenticar(usuario, "123")
    assert exito == False
    assert mensaje == "Contraseña inválida (mínimo 8 caracteres)"
    print("✅ test_autenticar_contraseña_corta: PASADO")

def test_metricas_mejora():
    """Prueba: US-001 - Métricas de mejora continua"""
    usuario = Usuario(
        email="test@example.com",
        password_hash=hashear_password("Password123!")
    )
    
    for _ in range(5):
        autenticar(usuario, "Password123!")
    
    for _ in range(3):
        autenticar(usuario, "WrongPassword")
    
    metricas = calcular_metricas_mejora(usuario)
    
    assert metricas["mejoras_realizadas"] == 5
    assert metricas["tasa_exito_acceso"] == 0.625
    assert metricas["nivel_madurez"] == "ML1"
    print("✅ test_metricas_mejora: PASADO")

def test_metricas_mejora_nivel_ml2():
    """Prueba: US-001 - Nivel de madurez ML2"""
    usuario = Usuario(
        email="test@example.com",
        password_hash=hashear_password("Password123!")
    )
    
    for _ in range(15):
        autenticar(usuario, "Password123!")
    
    metricas = calcular_metricas_mejora(usuario)
    
    assert metricas["mejoras_realizadas"] == 15
    assert metricas["nivel_madurez"] == "ML2"
    print("✅ test_metricas_mejora_nivel_ml2: PASADO")

if __name__ == "__main__":
    print("=" * 50)
    print("🧪 EJECUTANDO PRUEBAS - US-001 AUTENTICACIÓN")
    print("=" * 50)
    test_validar_email()
    test_hashear_password()
    test_autenticar()
    test_autenticar_usuario_no_encontrado()
    test_autenticar_contraseña_corta()
    test_metricas_mejora()
    test_metricas_mejora_nivel_ml2()
    print("=" * 50)
    print("✅ TODAS LAS PRUEBAS PASARON")
    print("=" * 50)