import django
import pytest

from app.models import Usuario
from app.models import Proyecto

@pytest.mark.django_db
def test_crear_usuario():
    # valores esperados
    id_esperado = "9999"
    tipoIdentificado_esperado = "CC"
    tUsuario_esperado = "admin"
    clave_esperado = "159"
    nombre_esperado = "juan"
    apellidos_esperado = "rios"
    telefono_esperado = "31245"
    correo_esperado = "juan@juan.com"
    genero_esperado = "M"
    estado_esperado = True

    user = Usuario()
    user.id = id_esperado
    user.tipoIdentificado = tipoIdentificado_esperado
    user.tUsuario = tUsuario_esperado
    user.clave = clave_esperado
    user.nombre = nombre_esperado
    user.apellidos = apellidos_esperado
    user.telefono = telefono_esperado
    user.correo = correo_esperado
    user.genero = genero_esperado
    user.estado = estado_esperado
    user.save()

    usuario_encontrado = Usuario.objects.get(id=id_esperado)

    assert usuario_encontrado.id == int(id_esperado)
    assert usuario_encontrado.tipoIdentificado == tipoIdentificado_esperado
    assert usuario_encontrado.tUsuario == tUsuario_esperado
    assert usuario_encontrado.clave == clave_esperado
    assert usuario_encontrado.nombre == nombre_esperado
    assert usuario_encontrado.apellidos == apellidos_esperado
    assert usuario_encontrado.telefono == telefono_esperado
    assert usuario_encontrado.correo == correo_esperado
    assert usuario_encontrado.genero == genero_esperado
    assert bool(usuario_encontrado.estado) == estado_esperado
    assert usuario_encontrado.idProyecto is None

@pytest.mark.django_db
def test_listar_usuarios_all():
    user = Usuario()
    user.id = "5689"
    user.correo = "5689@email.com"
    user.save()

    user2 = Usuario()
    user2.id = "6891"
    user2.correo = "6891@email.com"
    user2.save()

    user3 = Usuario()
    user3.id = "8912"
    user3.correo = "8912@email.com"
    user3.save()

    # hay 2 registros insertados desde el migration
    # más los insertados en esta prueba
    assert 5 == len(Usuario.objects.all())

@pytest.mark.django_db
def test_editar_usuario_por_id():
    # valores esperados
    id = "6523789"
    nombre_original = "pedro"
    nombre_actualizado = "peter"

    user = Usuario()
    user.id = id
    user.nombre = nombre_original
    user.save()

    usuario_encontrado = Usuario.objects.get(id=id)
    assert usuario_encontrado.nombre == nombre_original

    user.nombre = nombre_actualizado
    user.save()

    usuario_encontrado = Usuario.objects.get(id=id)
    assert usuario_encontrado.nombre == nombre_actualizado

    # hay 2 registros insertados desde el migration
    # más este único registro insertado y luego actualizado
    assert 3 == len(Usuario.objects.all())


@pytest.mark.django_db
def test_borrar_usuario_por_id():
    # valores esperados
    id = "6523789"
    nombre = "pedro"

    user = Usuario()
    user.id = id
    user.nombre = nombre
    user.save()

    # hay 3 registros insertados desde el migration
    # más este único registro insertado y luego actualizado
    assert 3 == len(Usuario.objects.all())

    Usuario.objects.filter(id=id).delete()

    assert 2 == len(Usuario.objects.all())

@pytest.mark.django_db
def test_consultar_usuario_no_existente():
    with pytest.raises(django.core.exceptions.ObjectDoesNotExist):
        Usuario.objects.get(id="7979989")


@pytest.mark.django_db
def test_crear_usuario_mismo_correo():
    # valores esperados
    correo = "admin@email.com"

    with pytest.raises(django.db.utils.IntegrityError):
        user = Usuario()
        user.id = "321654852"
        user.correo = correo
        user.save()


@pytest.mark.django_db
def test_matricular_estudiante_proyecto():
    proyecto = Proyecto()
    proyecto.id = "123"
    proyecto.nombre = "proyecto1"
    proyecto.estado = "activo"
    proyecto.save()

    # valores esperados
    id_esperado = "9999"
    tipoIdentificado_esperado = "CC"
    tUsuario_esperado = "admin"
    clave_esperado = "159"
    nombre_esperado = "juan"
    apellidos_esperado = "rios"
    telefono_esperado = "31245"
    correo_esperado = "juan@juan.com"
    genero_esperado = "M"
    estado_esperado = True
    id_proyecto_esperado = proyecto
    nota_proyecto_esperado = 4.5

    user = Usuario()
    user.id = id_esperado
    user.tipoIdentificado = tipoIdentificado_esperado
    user.tUsuario = tUsuario_esperado
    user.clave = clave_esperado
    user.nombre = nombre_esperado
    user.apellidos = apellidos_esperado
    user.telefono = telefono_esperado
    user.correo = correo_esperado
    user.genero = genero_esperado
    user.estado = estado_esperado
    user.idProyecto = id_proyecto_esperado
    user.notaDefinitivaProyecto = nota_proyecto_esperado
    user.save()

    usuario_encontrado = Usuario.objects.get(id=id_esperado)

    assert usuario_encontrado.id == int(id_esperado)
    assert usuario_encontrado.tipoIdentificado == tipoIdentificado_esperado
    assert usuario_encontrado.tUsuario == tUsuario_esperado
    assert usuario_encontrado.clave == clave_esperado
    assert usuario_encontrado.nombre == nombre_esperado
    assert usuario_encontrado.apellidos == apellidos_esperado
    assert usuario_encontrado.telefono == telefono_esperado
    assert usuario_encontrado.correo == correo_esperado
    assert usuario_encontrado.genero == genero_esperado
    assert bool(usuario_encontrado.estado) == estado_esperado
    assert usuario_encontrado.idProyecto is not None

