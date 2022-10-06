import pytest

from app.models import Usuario

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
