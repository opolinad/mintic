import django
import pytest

from app.models import Proyecto

@pytest.mark.django_db
def test_crear_proyecto():
    # valores esperados
    id_esperado = "9999"
    nombre_esperado = "proyecto 1"
    estado_esperado = "activo"

    proyecto = Proyecto()
    proyecto.id = id_esperado
    proyecto.nombre = nombre_esperado
    proyecto.estado = estado_esperado
    proyecto.save()

    proyecto_encontrado = Proyecto.objects.get(id=id_esperado)

    assert proyecto_encontrado.id == int(id_esperado)
    assert proyecto_encontrado.nombre == nombre_esperado
    assert proyecto_encontrado.estado == estado_esperado

@pytest.mark.django_db
def test_listar_proyectos_all():
    proyecto1 = Proyecto()
    proyecto1.id = "123"
    proyecto1.nombre = "proyecto1"
    proyecto1.estado = "activo"
    proyecto1.save()

    proyecto2 = Proyecto()
    proyecto2.id = "345"
    proyecto2.nombre = "proyecto2"
    proyecto2.estado = "activo"
    proyecto2.save()

    proyecto3 = Proyecto()
    proyecto3.id = "567"
    proyecto3.nombre = "proyecto3"
    proyecto3.estado = "activo"
    proyecto3.save()

    # hay 1 registros insertados desde el migration
    # más estos 3 registros
    assert 4 == len(Proyecto.objects.all())

@pytest.mark.django_db
def test_editar_proyecto_por_id():
    # valores esperados
    id = "9999"
    nombre = "proyecto1"
    estado_original = "activo"
    estado_actualizado = "inactivo"

    proyecto = Proyecto()
    proyecto.id = id
    proyecto.nombre = nombre
    proyecto.estado = estado_original
    proyecto.save()

    proyecto_encontrado = Proyecto.objects.get(id=id)

    assert proyecto_encontrado.id == int(id)
    assert proyecto_encontrado.nombre == nombre
    assert proyecto_encontrado.estado == estado_original

    proyecto.estado = estado_actualizado
    proyecto.save()

    proyecto_encontrado = Proyecto.objects.get(id=id)
    assert proyecto_encontrado.estado == estado_actualizado

    assert 2 == len(Proyecto.objects.all())


@pytest.mark.django_db
def test_borrar_proyecto_por_id():
    # valores esperados
    id = "9999"
    nombre = "proyecto1"
    estado = "activo"

    proyecto = Proyecto()
    proyecto.id = id
    proyecto.nombre = nombre
    proyecto.estado = estado
    proyecto.save()

    assert 2 == len(Proyecto.objects.all())

    Proyecto.objects.filter(id=id).delete()

    assert 1 == len(Proyecto.objects.all())


@pytest.mark.django_db
def test_consultar_proyecto_no_existente():
    with pytest.raises(django.core.exceptions.ObjectDoesNotExist):
        Proyecto.objects.get(id="7979989")


@pytest.mark.django_db
def test_crear_proyecto_mismo_nombre():
    nombre = "proyecto1"

    proyecto1 = Proyecto()
    proyecto1.id = "123"
    proyecto1.nombre = nombre
    proyecto1.estado = "activo"
    proyecto1.save()

    with pytest.raises(django.db.utils.IntegrityError):
        proyecto2 = Proyecto()
        proyecto2.id = "345"
        proyecto2.nombre = nombre
        proyecto2.estado = "activo"
        proyecto2.save()
