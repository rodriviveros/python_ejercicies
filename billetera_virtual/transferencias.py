#----------------------------------------------------------------------

MONTO_INVALIDADO = "Rechazada: monto inválido"
SALDO_INSUFICIENTE = "Rechazada: saldo insuficiente"
LIMITE_EXCEDIDO = "Rechazada: límite diario excedido"
APROBADA = "Transferencia Exitosa"
LIMITE_DIARIO = 200000

#----------------------------------------------------------------------

def transferir (saldo, monto, monto_acumulado):
    if monto <= 0:
        return MONTO_INVALIDADO
    if monto > saldo:
        return SALDO_INSUFICIENTE
    if monto_acumulado+monto > LIMITE_DIARIO:
        return LIMITE_EXCEDIDO
    return APROBADA

#----------------------------------------------------------------------
