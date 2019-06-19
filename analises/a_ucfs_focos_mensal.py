#------------------------------------------------------------------------------#
#                                 Versão: 1.0.2                                #
#                              Autor: Jonatas Leon                             #
#------------------------------------------------------------------------------#
from datetime import timedelta
one_day = timedelta(days=1)

# Buffer do poligono monitorado
obj_buffer = Buffer()

# Nome do dado dinâmico
dynamic_data = "d_focos_ams"

# Filtro a ser aplicado na tabela de dados dinâmicos
# AQUA_M-T é o valor no base para os dados do satélite de referência
filter_by = "satelite = 'AQUA_M-T'"

# Recupera data/hora da análise
exec_date = get_analysis_date()
mday = exec_date.timetuple().tm_mday

if mday == 1:
    # Determina como início da análise o primeiro dia do mês anterior
    analysis_date = (exec_date - one_day).replace(day=1)
    
    # Com os períodos de início e fim da análise devidamente definidos.
    # Cria-se uma formatação em texto (string) para a diferença,
    # em dias (days extended), da data em que a análise é executada e o início
    # do período a ser analisado
    days_amount = (exec_date - analysis_date).days
    days_amount_fmt = "{}d+".format(days_amount)
    
    # Realiza a contagem de ocorrências dos dados adicionais em relação
    # ao objeto monitorado (obj_buffer) com um filtro para focos do satélite de referência
    # a partir do que foi definido como o início do período analisado até a data atual
    nfocos = occurrence.zonal.count(dynamic_data, days_amount_fmt, obj_buffer, filter_by)
    
    # Salva contagem de focos como resultado da análise (nfocos)
    add_value("start_analysis_date", str(analysis_date))
    add_value("end_analysis_date", str(exec_date))
    add_value("nfocos", nfocos)