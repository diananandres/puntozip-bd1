from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DECIMAL,
    Sequence,
    Date,
    Time,
    ForeignKey,
    CheckConstraint
)

from db.db_setup import Base

from sqlalchemy.orm import relationship

class Empleado(Base):
    __tablename__ = "empleado"

    dni = Column(String(8), primary_key=True, nullable=False)
    nombres = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    fecha_contratacion = Column(Date, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)

class TrabajadorTaller(Base):
    __tablename__ = "trabajador_taller"

    dni = Column(String(8), ForeignKey("empleado.dni"), primary_key=True, nullable=False)
    tarifa = Column(DECIMAL(10, 2), nullable=False)
    CheckConstraint('tarifa between 12 and 15', name='tarifa_tt_rango')

class Tiempo(Base):
    __tablename__ = "tiempo"

    fecha = Column(Date, primary_key=True, nullable=False)
    dni = Column(String(8), ForeignKey("trabajador_taller.dni"), primary_key=True, nullable=False)
    hora_entrada = Column(Time, nullable=False)
    hora_salida = Column(Time, nullable=False)
    CheckConstraint('hora_entrada < hora_salida', name='chk_tiempo_horas')
    CheckConstraint("hora_entrada >= '08:00:00'", name='chk_entrada')
    CheckConstraint("hora_salida <= '22:00:00'", name='chk_salida')

class PersonalAdministrativo(Base):
    __tablename__ = "personal_administrativo"

    dni = Column(String(8), ForeignKey("empleado.dni"), primary_key=True, nullable=False)
    salario = Column(DECIMAL(10, 2), nullable=False)
    CheckConstraint('salario >= 1025', name='chk_pa_salario')

class Pago(Base):
    __tablename__ = "pago"

    codigo = Column(Integer, Sequence('codigo_seq'), primary_key=True, nullable=False)
    empleado_dni = Column(String(8), ForeignKey("empleado.dni"), nullable=False)
    fecha = Column(Date, nullable=False)
    monto = Column(DECIMAL(10, 2), nullable=False)
    CheckConstraint('monto > 0', name='pago_codigo_value')
    CheckConstraint('fecha <= current_date', name='pago_fecha')

class Deposito(Base):
    __tablename__ = "deposito"

    pago_codigo = Column(Integer, ForeignKey("pago.codigo"), primary_key=True, nullable=False)
    administrativo_dni = Column(String(8), ForeignKey("personal_administrativo.dni"), nullable=False)

class Ubicacion(Base):
    __tablename__ = "ubicacion"

    codigo = Column(Integer, Sequence('codigo_ubi_seq'), primary_key=True, nullable=False)
    direccion = Column(String, nullable=False)
    estado_provincia = Column(String, nullable=False)
    pais = Column(String, nullable=False)
    codigo_postal = Column(String, nullable=False)

class Cliente(Base):
    __tablename__ = "cliente"

    rin = Column(String(7), primary_key=True, nullable=False)
    nombre = Column(String, nullable=False)
    pais = Column(String, nullable=False)
    ubicacion_codigo = Column(Integer, ForeignKey("ubicacion.codigo"), nullable=False)

class Pedido(Base):
    __tablename__ = "pedido"

    po = Column(String(20), primary_key=True, nullable=False)
    fecha_pedido = Column(Date, nullable=False)
    fecha_entrega_propuesta = Column(Date, nullable=False)
    fecha_entrega = Column(Date)
    cliente_rin = Column(String(7), ForeignKey("cliente.rin"), nullable=False)
    CheckConstraint('fecha_pedido < fecha_entrega_propuesta and fecha_pedido < fecha_entrega', name='chk_pedido_fechas')

class Supervisa(Base):
    __tablename__ = "supervisa"

    administrativo_dni = Column(String(8), ForeignKey("personal_administrativo.dni"), primary_key=True, nullable=False)
    pedido_po = Column(String(20), ForeignKey("pedido.po"), primary_key=True, nullable=False)

class Empresa(Base):
    __tablename__ = "empresa"

    ruc = Column(String(11), primary_key=True, nullable=False)
    ubicacion_facturacion_codigo = Column(Integer, ForeignKey("ubicacion.codigo"), nullable=False)
    ubicacion_codigo = Column(Integer, ForeignKey("ubicacion.codigo"), nullable=False)

class Etapa(Base):
    __tablename__ = "etapa"

    pedido_po = Column(String(20), ForeignKey("pedido.po"), primary_key=True, nullable=False)
    estado = Column(String(20), primary_key=True, nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_finalizacion = Column(Date)
    empresa_ruc = Column(String(11), ForeignKey("empresa.ruc"), nullable=False)
    CheckConstraint("estado in ('Compra hilo', 'Tejeduría', 'Teñido', 'Corte', 'Confección', 'Acabados', 'Listo para despacho', 'Despachado')", name='chk_etapa_estado')

class Trabaja(Base):
    __tablename__ = "trabaja"

    etapa_po = Column(String(20), ForeignKey("etapa.pedido_po"), primary_key=True, nullable=False)
    etapa_estado = Column(String(20), ForeignKey("etapa.estado"), primary_key=True, nullable=False)
    trabajador_dni = Column(String(8), ForeignKey("trabajador_taller.dni"), primary_key=True, nullable=False)

class GuiaDeRemision(Base):
    __tablename__ = "guia_de_remision"

    numero = Column(String(6), primary_key=True, nullable=False)
    tipo = Column(String(4), nullable=False)
    fecha = Column(Date, nullable=False)
    descripcion = Column(String, nullable=False)
    placa_vehiculo = Column(String(7), nullable=False)
    ubicacion_salida_codigo = Column(Integer, ForeignKey("ubicacion.codigo"), nullable=False)
    ubicacion_destino_codigo = Column(Integer, ForeignKey("ubicacion.codigo"), nullable=False)
    CheckConstraint("tipo in ('T001', 'T002', 'T003', 'T004')", name='guia_tipo')

class Factura(Base):
    __tablename__ = "factura"

    numero = Column(String(6), primary_key=True, nullable=False)
    monto = Column(DECIMAL(10, 2), nullable=False)
    igv = Column(DECIMAL(10, 2), nullable=False)
    descripcion = Column(String, nullable=False)
    empresa_ruc = Column(String(11), ForeignKey("empresa.ruc"), nullable=False)
    ubicacion_codigo = Column(Integer, ForeignKey("ubicacion.codigo"), nullable=False)
    administrativo_dni = Column(String(8), ForeignKey("personal_administrativo.dni"), nullable=False)
    guia_numero = Column(String, ForeignKey("guia_de_remision.numero"), nullable=False)
    CheckConstraint('igv > 0', name='factura_igv')

class Contiene(Base):
    __tablename__ = "contiene"

    factura_numero = Column(String(6), ForeignKey("factura.numero"), primary_key=True, nullable=False)
    guia_numero = Column(String(6), ForeignKey("guia_de_remision.numero"), primary_key=True, nullable=False)

class Prenda(Base):
    __tablename__ = "prenda"

    pedido_po = Column(String(20), ForeignKey("pedido.po"), primary_key=True, nullable=False)
    color = Column(String(20), primary_key=True, nullable=False)
    estilo = Column(String, nullable=False)

class Polo(Base):
    __tablename__ = "polo"

    pedido_po = Column(String(20), ForeignKey("prenda.pedido_po"), primary_key=True, nullable=False)
    color = Column(String(20), ForeignKey("prenda.color"), primary_key=True, nullable=False)
    talla = Column(String(4), primary_key=True, nullable=False)
    CheckConstraint("talla in ('XS', 'S', 'M', 'L', 'XL')", name='chk_polo_talla')

class Vestido(Base):
    __tablename__ = "vestido"

    pedido_po = Column(String(20), ForeignKey("prenda.pedido_po"), primary_key=True, nullable=False)
    color = Column(String(20), ForeignKey("prenda.color"), primary_key=True, nullable=False)
    talla = Column(String(4), primary_key=True, nullable=False)
    CheckConstraint("talla in ('XS', 'S', 'M', 'L', 'XL')", name='chk_vestido_talla')

class Talla(Base):
    __tablename__ = "talla"

    pedido_po = Column(String(20), ForeignKey("prenda.pedido_po"), primary_key=True, nullable=False)
    color = Column(String(20), ForeignKey("prenda.color"), primary_key=True, nullable=False)
    talla = Column(String(4), primary_key=True, nullable=False)
    CheckConstraint("talla in ('XS', 'S', 'M', 'L', 'XL')", name='chk_talla_talla')

