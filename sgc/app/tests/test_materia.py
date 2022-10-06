import pytest

from app.models import Materia

@pytest.mark.django_db
def test_crear_materia():
    # valores esperados
    id_esperado = 1
    nombre_esperado = "español"

    materia = Materia()
    materia.id = id_esperado
    materia.nombre = nombre_esperado
    materia.save()

    materia_encontrado = Materia.objects.get(id=id_esperado)

    assert materia_encontrado.id == id_esperado
    assert materia_encontrado.nombre == nombre_esperado
