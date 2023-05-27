CANON_URL = "https://balanca.economia.gov.br/balanca/bd/"

TRADE = {
    "exp": {
        "description": "Exportação",
        "server_dir": CANON_URL + "comexstat-bd/ncm/",
        "server_filename": "EXP_{year}.csv",
        "pkey": [
            "CO_ANO",
            "CO_MES",
            "CO_NCM",
            "CO_UNID",
            "CO_PAIS",
            "SG_UF_NCM",
            "CO_VIA",
            "CO_URF",
        ],
        "name": "",
        "year_range": [1997, None],
    },
    "imp": {
        "description": "Importação",
        "server_dir": CANON_URL + "comexstat-bd/ncm/",
        "server_filename": "IMP_{year}.csv",
        "pkey": [
            "CO_ANO",
            "CO_MES",
            "CO_NCM",
            "CO_UNID",
            "CO_PAIS",
            "SG_UF_NCM",
            "CO_VIA",
            "CO_URF",
        ],
        "name": "",
        "year_range": [1997, None],
    },
    "exp-mun": {
        "description": "Exportação dos municípios",
        "server_dir": CANON_URL + "comexstat-bd/mun/",
        "server_filename": "EXP_{year}_MUN.csv",
        "pkey": [
            "CO_ANO",
            "CO_MES",
            "SH4",
            "CO_PAIS",
            "SG_UF_MUN",
            "CO_MUN",
        ],
        "name": "",
        "year_range": [1997, None],
    },
    "imp-mun": {
        "description": "Importação dos municípios",
        "server_dir": CANON_URL + "comexstat-bd/mun/",
        "server_filename": "IMP_{year}_MUN.csv",
        "pkey": [
            "CO_ANO",
            "CO_MES",
            "SH4",
            "CO_PAIS",
            "SG_UF_MUN",
            "CO_MUN",
        ],
        "name": "",
        "year_range": [1997, None],
    },
    "exp-nbm": {
        "description": "Exportação histórica",
        "server_dir": CANON_URL + "comexstat-bd/nbm/",
        "server_filename": "EXP_{year}_NBM.csv",
        "pkey": [
            "CO_ANO",
            "CO_MES",
            "CO_NBM",
            "CO_PAIS",
            "SG_UF",
        ],
        "name": "",
        "year_range": [1989, 1996],
    },
    "imp-nbm": {
        "description": "Importação histórica",
        "server_dir": CANON_URL + "comexstat-bd/nbm/",
        "server_filename": "IMP_{year}_NBM.csv",
        "pkey": [
            "CO_ANO",
            "CO_MES",
            "CO_NBM",
            "CO_PAIS",
            "SG_UF",
        ],
        "name": "",
        "year_range": [1989, 1996],
    },
}

TABLES = {
    "ncm": {
        "description": "Códigos NCM e descrições.",
        "server_filename": "NCM.csv",
        "pkey": ["CO_NCM"],
        "name": "NCM - Nomenclatura Comum do Mercosul",
    },
    "sh": {
        "description": (
            "Códigos e descrições do Sistema Harmonizado (Seções, "
            "Capítulos-SH2, Posições-SH4 e Subposições-SH6)."
        ),
        "server_filename": "NCM_SH.csv",
        "pkey": ["CO_SH6"],
        "name": "SH - Sistema Harmonizado",
    },
    "cuci": {
        "description": (
            "Códigos e descrições dos níveis da classificação CUCI "
            "(Revisão 4). Pode ser utilizada conjuntamente com ISIC."
        ),
        "server_filename": "NCM_CUCI.csv",
        "pkey": ["CO_CUCI_ITEM"],
        "name": "CUCI - Classificação Uniforme para Comércio Internacional",
    },
    "cgce": {
        "description": (
            "Códigos e descrições dos níveis da classificação CGCE."
        ),
        "server_filename": "NCM_CGCE.csv",
        "pkey": ["CO_CGCE_N3"],
        "name": "CGCE - Classificação por Grandes Categorias Econômicas",
    },
    "isic": {
        "description": (
            "Códigos e descrições da classificação ISIC (Revisão 4)."
        ),
        "server_filename": "NCM_ISIC.csv",
        "pkey": ["CO_ISIC_CLASSE"],
        "name": (
            "ISIC - International Standard Industrial Classification "
            "(Setores Industriais)"
        ),
    },
    "siit": {
        "description": "Códigos e descrições da classificação SIIT.",
        "server_filename": "NCM_SIIT.csv",
        "pkey": ["CO_SIIT"],
        "name": "SIIT - Setores Industriais por Intensidade Tecnológica",
    },
    "fat-agreg": {
        "description": (
            "Códigos e descrições de Fator Agregado das NCMs. Pode ser "
            "utilizada conjuntamente com a tabela de PPI ou PPE."
        ),
        "server_filename": "NCM_FAT_AGREG.csv",
        "pkey": ["CO_FAT_AGREG"],
        "name": "Fator Agregado da NCM - Classificação própria da SECEX",
    },
    "unidade": {
        "description": (
            "Códigos e descrições das unidades estatísticas das NCMs."
        ),
        "server_filename": "NCM_UNIDADE.csv",
        "pkey": ["CO_UNID"],
        "name": "Unidade Estatística da NCM",
    },
    "ppi": {
        "description": (
            "Códigos e descrições da Pauta de Produtos Importados. DEVE SER "
            "UTILIZADA APENAS PARA IMPORTAÇÃO."
        ),
        "server_filename": "NCM_PPI.csv",
        "pkey": ["CO_PPI"],
        "name": (
            "Pauta de Produtos Importados - Classificação própria da SECEX"
        ),
    },
    "ppe": {
        "description": (
            "Códigos e descrições da Pauta de Produtos Exportados. DEVE SER "
            "UTILIZADA APENAS PARA EXPORTAÇÃO."
        ),
        "server_filename": "NCM_PPE.csv",
        "pkey": ["CO_PPE"],
        "name": (
            "Pauta de Produtos Exportados - Classificação própria da SECEX"
        ),
    },
    "grupo": {
        "description": (
            "Códigos e descrições de Grupo de Produtos. DEVE SER UTILIZADA "
            "APENAS PARA EXPORTAÇÃO."
        ),
        "server_filename": "NCM_GRUPO.csv",
        "pkey": ["CO_EXP_SUBSET"],
        "name": "Grupo de Produtos- Classificação própria da SECEX",
    },
    "pais": {
        "description": "Códigos e descrições de países.",
        "server_filename": "PAIS.csv",
        "pkey": ["CO_PAIS"],
        "name": "Países",
    },
    "pais-bloco": {
        "description": (
            "Códigos e descrições das principais agregações de países em "
            "blocos. Deve ser usada em cojunto com a tabela de países."
        ),
        "server_filename": "PAIS_BLOCO.csv",
        "pkey": ["CO_BLOCO"],
        "name": "Blocos de Países",
    },
    "uf": {
        "description": (
            "Códigos e nome das unidades da federação (estados) do Brasil."
        ),
        "server_filename": "UF.csv",
        "pkey": ["CO_UF"],
        "name": "Unidades da Federação",
    },
    "uf-mun": {
        "description": (
            "Códigos e nome dos municípios brasileiros. Pode ser utilizada em "
            "conjunto com a tabela de UF. Fundamental para utilização junto "
            "com o arquivo de dados brutos por municípios domicílio fiscal "
            "das empresas."
        ),
        "server_filename": "UF_MUN.csv",
        "pkey": ["CO_MUN_GEO"],
        "name": "Municípios",
    },
    "via": {
        "description": "Código e descrição da via (modal) de transporte",
        "server_filename": "VIA.csv",
        "pkey": ["CO_VIA"],
        "name": "Via",
    },
    "urf": {
        "description": (
            "Código e descrição da Unidade da Receita Federal "
            "(embarque/despacho)."
        ),
        "server_filename": "URF.csv",
        "pkey": ["CO_URF"],
        "name": "Urf",
    },
    "isic-cuci": {
        "description": (
            "Códigos e descrições dos níveis ISIC e CUCI usados na coletiva "
            "de apresentação da balança comercial brasileira."
        ),
        "server_filename": "ISIC_CUCI.csv",
        "pkey": [],
        "name": "ISIC Seção x CUCI Grupo",
    },
    "nbm": {
        "description": "Códigos NBM e descrições.",
        "server_filename": "NBM.csv",
        "pkey": ["CO_NBM"],
        "name": "NBM (1989-1996) - Nomenclatura Brasileira de Mercadorias",
    },
    "nbm-ncm": {
        "description": "Tabela de conversão entre códigos NBM e NCM.",
        "server_filename": "NBM_NCM.csv",
        "pkey": [],
        "name": "NBMxNCM - Tabela de conversão",
    },
}

AUX_TABLES = {
    name: TABLES[name]["server_filename"] for name in TABLES
}

REPETRO_TABLES = {
    "exp-repetro": {
        "description": "Estatísticas REPETRO contabilizadas em separado",
        "server_filename": "exp_repetro.xlsx",
        "pkey": ["CO_ANO", "CO_MES", "CO_NCM", "CO_PAIS"],
        "name": "REPETRO Exportações",
        "url": CANON_URL + "repetro/exp_repetro.xlsx",
    },
    "imp-repetro": {
        "description": "Estatísticas REPETRO contabilizadas em separado",
        "server_filename": "imp_repetro.xlsx",
        "pkey": ["CO_ANO", "CO_MES", "CO_NCM", "CO_PAIS"],
        "name": "REPETRO Importações",
        "url": CANON_URL + "repetro/imp_repetro.xlsx",
    },
}

OTHER_TABLES = {
    "tabelas-auxiliares": {
        "description": (
            "Tabelas de Correlações de Códigos e Classificações em Excel"
        ),
        "server_filename": "TABELAS_AUXILIARES.xlsx",
        "pkey": [],
        "name": "Tabelas de Correlações de Códigos e Classificações",
        "url": CANON_URL + "tabelas/TABELAS_AUXILIARES.xlsx",
    },
}


TOTAIS_PARA_VALIDACAO = {
    "exp-validacao": {
        "description": "Totais para validação",
        "server_filename": "EXP_TOTAIS_CONFERENCIA.csv",
        "pkey": [],
        "name": "Totais para validação",
        "url": CANON_URL + "comexstat-bd/ncm/EXP_TOTAIS_CONFERENCIA.csv",
    },
    "imp-validacao": {
        "description": "Totais para validação",
        "server_filename": "IMP_TOTAIS_CONFERENCIA.csv",
        "pkey": [],
        "name": "Totais para validação",
        "url": CANON_URL + "comexstat-bd/ncm/IMP_TOTAIS_CONFERENCIA.csv",
    },
    "exp-mun-validacao": {
        "description": "Totais para validação de exportação município.",
        "server_filename": "EXP_TOTAIS_CONFERENCIA_MUN.csv",
        "pkey": [],
        "name": "Totais para validação de exportação município",
        "url": CANON_URL + "comexstat-bd/mun/EXP_TOTAIS_CONFERENCIA_MUN.csv",
    },
    "imp-mun-validacao": {
        "description": "Totais para validação de importação município.",
        "server_filename": "IMP_TOTAIS_CONFERENCIA_MUN.csv",
        "pkey": [],
        "name": "Totais para validação de importação município.",
        "url": CANON_URL + "comexstat-bd/mun/IMP_TOTAIS_CONFERENCIA_MUN.csv",
    },
}

ARQUIVO_UNICO = {
    "exp-completa": {
        "description": "Arquivo completo de Exportações",
        "server_filename": "EXP_COMPLETA.zip",
        "pkey": [],
        "name": "Arquivo completo de Exportações",
        "url": CANON_URL + "comexstat-bd/ncm/EXP_COMPLETA.zip",
    },
    "imp-completa": {
        "description": "Arquivo completo de Importações",
        "server_filename": "IMP_COMPLETA.zip",
        "pkey": [],
        "name": "Arquivo completo de Importações",
        "url": CANON_URL + "comexstat-bd/ncm/IMP_COMPLETA.zip",
    },
    "exp-mun-completa": {
        "description": "Arquivo completo de Exportações municipais.",
        "server_filename": "EXP_COMPLETA_MUN.zip",
        "pkey": [],
        "name": "Arquivo completo de Exportações municipais.",
        "url": CANON_URL + "comexstat-bd/mun/EXP_COMPLETA_MUN.zip",
    },
    "imp-mun-completa": {
        "description": "Arquivo completo de Importações municipais.",
        "server_filename": "IMP_COMPLETA_MUN.zip",
        "pkey": [],
        "name": "Arquivo completo de Importações municipais.",
        "url": CANON_URL + "comexstat-bd/mun/IMP_COMPLETA_MUN.zip",
    },
}


def get_url(table, **kwargs):
    year = kwargs.get("year", None)
    match table:
        case "exp" | "imp" | "exp-mun" | "imp-mun" | "exp-nbm" | "imp-nbm":
            url = (
                TRADE[table]["server_dir"]
                + TRADE[table]["server_filename"].format(year=year)
            )
        case "exp-completa" | "imp-completa":
            url = ARQUIVO_UNICO[table]["url"]
        case "exp-mun-completa" | "imp-mun-completa":
            url = ARQUIVO_UNICO[table]["url"]
        case "exp-validacao" | "imp-validacao":
            url = TOTAIS_PARA_VALIDACAO[table]["url"]
        case "exp-mun-validacao" | "imp-mun-validacao":
            url = TOTAIS_PARA_VALIDACAO[table]["url"]
        case "exp-repetro" | "imp-repetro":
            url = REPETRO_TABLES[table]["url"]
        case "tabelas-auxiliares":
            url = OTHER_TABLES[table]["url"]
        case _:
            url = CANON_URL + "tabelas/" + AUX_TABLES[table]
    return url
