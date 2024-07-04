from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Date,
    PrimaryKeyConstraint,
    ForeignKeyConstraint
)

from db.db_setup import Base

from sqlalchemy.orm import relationship

class Empleado(Base):
    __tablename__ = 'empleado'

    dni = Column(String(8), index=True, primary_key=True)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    fecha_contratacion = Column(Date, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)

class Trabajador(Base):
    __tablename__ = 'trabajador_taller'

    dni = Column(String(8), index=True, primary_key=True)

class Tiempo(Base):
    __tablename__='tiempo'

    dni = Column()
    fecha = Column()
    hora_entrada = Column()
    hora_salida = Column()

class Personal(Base):
    __tablename__='personal_administrativo'

    dni = Column()
    salario = Column()

class Pago(Base):
    __tablename__='pago'

    codigo = Column()
    fecha = Column()

class Deposito(Base):
    __tablename__='deposito_pago'

    codigo = Column()
    pago_codigo = Column()
    dni = Column()

class Pago_Personal(Base):
    __tablename__='pago_personal_administrativo'

    dni = Column()
    codigo = Column()

class Pago_Trabajador(Base):
    __tablename__='pago_trabajador_taller'

    dni = Column()
    codigo = Column()
    horas_semana = Column()
    monto = Column()

class Ubicacion(Base):
    __tablename__='ubicacion'

    codigo = Column()
    direccion = Column()
    estado_provincia = Column()
    pais = Column()
    codigo_postal = Column()

class Cliente(Base):
    __tablename__='cliente'

    rin = Column()
    nombre = Column()
    pais = Column()
    ubicacion_codigo = Column()

class Pedido(Base):
    __tablename__='pedido'

    po = Column()
    fecha_pedido = Column()
    fecha_entrega_propuesta = Column()
    fecha_entrega = Column()
    cliente_rin = Column()

class PA_Pedido(Base):
    __tablename__='personal_administrativo_pedido'

    dni = Column()
    po = Column()

class Empresa(Base):
    __tablename__='empresa'

    ruc = Column()
    ubicacion_facturacion_codigo = Column()
    ubicacion_codigo = Column()

class Etapa(Base):
    __tablename__='etapa'

    po = Column()
    estado = Column()
    fecha_inicio = Column()
    fecha_inicializacion = Column()
    ruc = Column()

class TT_Etapa(Base):
    __tablename__='trabajador_taller_etapa'

    po = Column()
    estado = Column()
    dni = Column()

class Guia_Remision(Base):
    __tablename__='guia_de_remision'

    numero = Column()
    tipo = Column()
    fecha = Column()
    descripcion = Column()
    placa_vehiculo = Column()
    ubicacion_salida_codigo = Column()
    ubicacion_destino_codigo = Column()

class Factura(Base):
    __tablename__='factura'

    numero = Column()
    monto = Column()
    igv = Column()
    descripcion = Column()
    ruc = Column()
    ubicacion_factura_codigo = Column()
    dni = Column()
    guia_de_remision_numero = Column()

class Factura_Guia_Remision(Base):
    __tablename__='factura_guia_de_remision'

    factura_numero = Column()
    guia_numero = Column()
    
class Prenda(Base):
    __tablename__='prenda'

    po = Column()
    color = Column()
    estilo = Column()
    categoria = Column()
    
class Polo(Base):
    __tablename__='polo'

    po = Column()
    color = Column()
    estilo = Column()
    tipo = Column()   

class Vestido(Base):
    __tablename__='vestido'

    po = Column()
    color = Column()
    estilo = Column()
    tipo = Column() 

class Talla(Base):
    __tablename__='talla'

    po = Column()
    color = Column()
    estilo = Column()
    upc = Column()
    tamano = Column()
    precio = Column()
    cantidad = Column()
