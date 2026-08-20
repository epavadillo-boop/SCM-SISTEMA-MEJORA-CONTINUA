# tests/test_rdm.py
import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.cmmi_rules.rdm_scrum import ModuloRDMScrum
from src.core_app.config import settings


def crear_repositorio_prueba(test_dir):
    test_dir.mkdir(parents=True, exist_ok=True)

    (test_dir / "product_backlog.md").write_text("""# Product Backlog

## US-001: Autenticacion
Como usuario registrado
Quiero iniciar sesion
Para acceder a mis datos

Criterios de Aceptacion:
- El sistema valida email y contrasena

Prioridad: Alta
Aprobado por PO: Si
""", encoding="utf-8")

    (test_dir / "SPRINT_COMMITMENTS.md").write_text("""# Sprint Commitments

## Sprint Goal
Implementar autenticacion
Prioridad: Alta

Compromiso del equipo: Si
""", encoding="utf-8")

    (test_dir / "DOD.md").write_text("""# Definition of Done (DoD)

## Criterios de Verificacion
Prioridad: Alta

- [ ] Codigo implementado
- [ ] Pruebas unitarias pasan (100%)
- [ ] Criterios de aceptacion cumplidos
- [ ] Aprobado por Product Owner
- [ ] Documentacion actualizada

## Checklist de Consistencia
- [ ] Requisito ↔ Codigo: trazable
- [ ] Requisito ↔ Tests: cubierto
- [ ] Requisito ↔ Documentacion: actualizada
""", encoding="utf-8")

    print(f"✅ Archivos de prueba creados en: {test_dir}")


def main():
    parser = argparse.ArgumentParser(description='Auditar un repositorio con CMMI-Auditor')
    parser.add_argument('--repo', type=str, help='Ruta al repositorio a auditar')
    parser.add_argument('--create-test', action='store_true', help='Crear repositorio de prueba')

    args = parser.parse_args()

    if args.create_test:
        test_dir = settings.TEST_REPO_PATH
        crear_repositorio_prueba(test_dir)
        repo_path = test_dir
    elif args.repo:
        repo_path = Path(args.repo)
        if not repo_path.exists():
            print(f"❌ El repositorio '{repo_path}' no existe")
            sys.exit(1)
    else:
        test_dir = settings.TEST_REPO_PATH
        if not test_dir.exists():
            crear_repositorio_prueba(test_dir)
        repo_path = test_dir

    print(f"⏳ Iniciando análisis del Motor de Auditoría sobre: {repo_path}...")

    modulo = ModuloRDMScrum()
    resultado = modulo.evaluar(str(repo_path), verbose=True)

    print('\n' + '='*70)
    print('📊 REPORTE DE AUDITORÍA AUTOMATIZADO RDM ML2')
    print('='*70)
    print(f"Score: {resultado['score']} %")
    print(f"Estado: {resultado['estado']}")
    print(f"Criterios cumplidos: {resultado['criterios_cumplidos']} / {resultado['total_criterios']}")
    print('-'*70)
    for crit, data in resultado['criterios'].items():
        icono = '✅ OK' if data['cumple'] else '❌ NO'
        evidencia = data.get('evidencia', 'Sin evidencia')[:65]
        print(f'   {icono} {crit:<8} : {evidencia}')
    print('='*70)


if __name__ == "__main__":
    main()