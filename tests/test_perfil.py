# tests/test_perfil.py - Pruebas para US-002
# Sistema de Mejora Continua (SMC)

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.perfil import PerfilUsuario, crear_perfil

def test_crear_perfil():
    """Prueba: US-002 - Creación de perfil"""
    resultado = crear_perfil(1, "Carlos", "Mejora Pérez", "carlos@empresa.com")
    assert resultado["exito"] == True
    assert resultado["perfil"]["nombre"] == "Carlos"
    assert resultado["perfil"]["apellidos"] == "Mejora Pérez"
    assert resultado["perfil"]["email"] == "carlos@empresa.com"
    print("✅ test_crear_perfil: PASADO")

def test_crear_perfil_nombre_invalido():
    """Prueba: US-002 - Creación con nombre inválido"""
    resultado = crear_perfil(1, "a", "Mejora Pérez", "carlos@empresa.com")
    assert resultado["exito"] == False
    assert "nombre" in resultado["mensaje"].lower()
    print("✅ test_crear_perfil_nombre_invalido: PASADO")

def test_crear_perfil_email_invalido():
    """Prueba: US-002 - Creación con email inválido"""
    resultado = crear_perfil(1, "Carlos", "Mejora Pérez", "carlos@empresa")
    assert resultado["exito"] == False
    assert "email" in resultado["mensaje"].lower()
    print("✅ test_crear_perfil_email_invalido: PASADO")

def test_actualizar_nombre():
    """Prueba: US-002 - Actualizar nombre"""
    usuario = PerfilUsuario(1, "Carlos", "Mejora Pérez", "carlos@empresa.com")
    resultado = usuario.actualizar_nombre("Carlos Alberto")
    assert resultado["exito"] == True
    assert usuario.nombre == "Carlos Alberto"
    print("✅ test_actualizar_nombre: PASADO")

def test_actualizar_email():
    """Prueba: US-002 - Actualizar email"""
    usuario = PerfilUsuario(1, "Carlos", "Mejora Pérez", "carlos@empresa.com")
    resultado = usuario.actualizar_email("carlos.alberto@empresa.com")
    assert resultado["exito"] == True
    assert usuario.email == "carlos.alberto@empresa.com"
    print("✅ test_actualizar_email: PASADO")

def test_actualizar_email_invalido():
    """Prueba: US-002 - Actualizar con email inválido"""
    usuario = PerfilUsuario(1, "Carlos", "Mejora Pérez", "carlos@empresa.com")
    resultado = usuario.actualizar_email("carlos@empresa")
    assert resultado["exito"] == False
    assert "email" in resultado["mensaje"].lower()
    print("✅ test_actualizar_email_invalido: PASADO")

def test_cambiar_contraseña():
    """Prueba: US-002 - Cambiar contraseña"""
    usuario = PerfilUsuario(1, "Carlos", "Mejora Pérez", "carlos@empresa.com")
    resultado = usuario.actualizar_contraseña("old123", "new123456", "new123456")
    assert resultado["exito"] == True
    assert resultado["mensaje"] == "Contraseña actualizada correctamente"
    print("✅ test_cambiar_contraseña: PASADO")

def test_cambiar_contraseña_no_coinciden():
    """Prueba: US-002 - Contraseñas no coinciden"""
    usuario = PerfilUsuario(1, "Carlos", "Mejora Pérez", "carlos@empresa.com")
    resultado = usuario.actualizar_contraseña("old123", "new123456", "new12345")
    assert resultado["exito"] == False
    assert "coinciden" in resultado["mensaje"]
    print("✅ test_cambiar_contraseña_no_coinciden: PASADO")

def test_historial_cambios():
    """Prueba: US-002 - Historial de cambios"""
    usuario = PerfilUsuario(1, "Carlos", "Mejora Pérez", "carlos@empresa.com")
    usuario.actualizar_nombre("Carlos Alberto")
    usuario.actualizar_email("carlos.alberto@empresa.com")
    
    historial = usuario.obtener_historial()
    assert len(historial) == 2
    assert historial[0]["campo"] == "nombre"
    assert historial[1]["campo"] == "email"
    print("✅ test_historial_cambios: PASADO")

if __name__ == "__main__":
    print("=" * 50)
    print("🧪 EJECUTANDO PRUEBAS - US-002 Gestión de Perfil")
    print("=" * 50)
    test_crear_perfil()
    test_crear_perfil_nombre_invalido()
    test_crear_perfil_email_invalido()
    test_actualizar_nombre()
    test_actualizar_email()
    test_actualizar_email_invalido()
    test_cambiar_contraseña()
    test_cambiar_contraseña_no_coinciden()
    test_historial_cambios()
    print("=" * 50)
    print("✅ TODAS LAS PRUEBAS PASARON")
    print("=" * 50)