# tests/test_dashboard.py - Pruebas para US-003
# Sistema de Mejora Continua (SMC)

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dashboard import IndicadoresLean, DashboardLean

def test_calcular_oee():
    """Prueba: US-003 - Cálculo de OEE"""
    indicadores = IndicadoresLean()
    oee = indicadores.calcular_oee(85, 90, 95)
    # 0.85 * 0.90 * 0.95 * 100 = 72.675 -> Python redondea a 72.67
    assert oee == 72.67
    print("✅ test_calcular_oee: PASADO")

def test_calcular_takt_time():
    """Prueba: US-003 - Cálculo de Takt Time"""
    indicadores = IndicadoresLean()
    takt = indicadores.calcular_takt_time(28800, 150)
    assert takt == 192.0
    print("✅ test_calcular_takt_time: PASADO")

def test_calcular_cycle_time():
    """Prueba: US-003 - Cálculo de Cycle Time"""
    indicadores = IndicadoresLean()
    cycle = indicadores.calcular_cycle_time(27000, 150)
    assert cycle == 180.0
    print("✅ test_calcular_cycle_time: PASADO")

def test_obtener_nivel_oee():
    """Prueba: US-003 - Nivel de OEE"""
    indicadores = IndicadoresLean()
    
    # Excelente: OEE >= 85%
    indicadores.calcular_oee(92, 95, 98)  # 0.92 * 0.95 * 0.98 * 100 = 85.65%
    nivel = indicadores.obtener_nivel_oee()
    print(f"DEBUG - OEE 85.65% → {nivel}")
    assert "Excelente" in nivel
    
    # Bueno: OEE 70-84%
    indicadores.calcular_oee(85, 90, 92)  # 0.85 * 0.90 * 0.92 * 100 = 70.38%
    nivel = indicadores.obtener_nivel_oee()
    print(f"DEBUG - OEE 70.38% → {nivel}")
    assert "Bueno" in nivel
    
    # Regular: OEE 60-69%
    indicadores.calcular_oee(80, 85, 90)  # 0.80 * 0.85 * 0.90 * 100 = 61.20%
    nivel = indicadores.obtener_nivel_oee()
    print(f"DEBUG - OEE 61.20% → {nivel}")
    assert "Regular" in nivel
    
    # Crítico: OEE < 60%
    indicadores.calcular_oee(70, 80, 85)  # 0.70 * 0.80 * 0.85 * 100 = 47.6%
    nivel = indicadores.obtener_nivel_oee()
    print(f"DEBUG - OEE 47.6% → {nivel}")
    assert "Crítico" in nivel
    
    print("✅ test_obtener_nivel_oee: PASADO")

def test_dashboard_actualizar():
    """Prueba: US-003 - Actualizar dashboard"""
    dashboard = DashboardLean()
    metricas = dashboard.actualizar_indicadores(85, 90, 95, 28800, 150, 27000, 150)
    
    assert "oee" in metricas
    assert "takt_time" in metricas
    assert "cycle_time" in metricas
    assert metricas["oee"] == 72.67
    assert metricas["takt_time"] == 192.0
    assert metricas["cycle_time"] == 180.0
    print("✅ test_dashboard_actualizar: PASADO")

def test_historial():
    """Prueba: US-003 - Historial de métricas"""
    dashboard = DashboardLean()
    
    for i in range(5):
        dashboard.generar_datos_ejemplo()
    
    historial = dashboard.obtener_historial()
    assert len(historial) == 5
    assert "oee" in historial[0]
    assert "fecha" in historial[0]
    print("✅ test_historial: PASADO")

def test_obtener_ultimas_metricas():
    """Prueba: US-003 - Obtener últimas métricas"""
    dashboard = DashboardLean()
    dashboard.actualizar_indicadores(85, 90, 95, 28800, 150, 27000, 150)
    
    metricas = dashboard.obtener_ultimas_metricas()
    assert metricas["oee"] == 72.67
    assert "nivel_oee" in metricas
    print("✅ test_obtener_ultimas_metricas: PASADO")

if __name__ == "__main__":
    print("=" * 50)
    print("🧪 EJECUTANDO PRUEBAS - US-003 Dashboard Lean")
    print("=" * 50)
    test_calcular_oee()
    test_calcular_takt_time()
    test_calcular_cycle_time()
    test_obtener_nivel_oee()
    test_dashboard_actualizar()
    test_historial()
    test_obtener_ultimas_metricas()
    print("=" * 50)
    print("✅ TODAS LAS PRUEBAS PASARON")
    print("=" * 50)