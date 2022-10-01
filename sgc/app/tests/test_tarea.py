import pytest

from app.models import Tarea

@pytest.mark.django_db
def test_crear_tarea():
    # valores esperados
    id_esperado = 1
    calificacion_esperada = 4
    estado_esperado = "calicada"
    nombre_esperado = "taller"

    tarea = Tarea()
    tarea.id = id_esperado
    tarea.calificacion = calificacion_esperada
    tarea.estado = estado_esperado
    tarea.nombre = nombre_esperado
    tarea.save()

    tarea_encontrada = Tarea.objects.get(id=id_esperado)

    assert tarea_encontrada.id == id_esperado
    assert tarea_encontrada.estado == estado_esperado
    assert tarea_encontrada.nombre == nombre_esperado
