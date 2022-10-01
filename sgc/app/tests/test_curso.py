import pytest

from app.models import Curso

@pytest.mark.django_db
def test_crear_curso():
    # valores esperados
    id_esperado = 1
    nombre_esperado = "decimo"
    estado_esperado = "activo"

    curso = Curso()
    curso.id = id_esperado
    curso.nombre = nombre_esperado
    curso.estado = estado_esperado
    curso.save()

    curso_encontrado = Curso.objects.get(id=id_esperado)

    assert curso_encontrado.id == id_esperado
    assert curso_encontrado.nombre == nombre_esperado
    assert curso_encontrado.estado == estado_esperado