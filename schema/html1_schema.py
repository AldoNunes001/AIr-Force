from typing import List

from pydantic import BaseModel, Field


class EmpresaJucesp(BaseModel):
    """
    Representa os detalhes de uma empresa registrada na JUCESP.
    """

    nome: str = Field(
        ...,
        alias="empresa_jucesp.nome",
        description="Nome da empresa registrada na JUCESP",
    )
    nire: str = Field(
        ...,
        alias="empresa_jucesp.nire",
        description="Número de Identificação do Registro de Empresas (NIRE) na JUCESP",
    )
    uf: str = Field(
        ...,
        alias="empresa_jucesp.uf",
        description="Unidade Federativa onde a empresa está registrada",
    )


class SinapsesEmpresaJucesp(BaseModel):
    """
    Representa uma lista de empresas registradas na JUCESP.
    """

    empresa_jucesp: List[EmpresaJucesp] = Field(
        ...,
        min_items=1,
        max_items=1,
        alias="sinapses.Empresa_Jucesp",
        description="Lista de empresa registrada na JUCESP",
    )


class RootHTML1(BaseModel):
    """
    Representa o modelo raiz que contém uma lista de SinapsesEmpresaJucesp.
    """

    root_html1: List[SinapsesEmpresaJucesp]

    class Config:
        """
        Configuração da classe RootHTML1 para permitir a popularização por nome.
        """

        populate_by_name = True
