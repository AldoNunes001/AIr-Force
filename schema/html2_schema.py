from typing import List

from pydantic import BaseModel, Field


class Endereco(BaseModel):
    """
    Representa os detalhes do endereço de uma empresa.
    """

    logradouro: str = Field(
        ..., alias="endereco.logradouro", description="Logradouro do endereço"
    )
    numero: str = Field(..., alias="endereco.numero", description="Número do endereço")
    bairro: str = Field(..., alias="endereco.bairro", description="Bairro do endereço")
    complemento: str = Field(
        ..., alias="endereco.complemento", description="Complemento do endereço"
    )
    cidade: str = Field(..., alias="endereco.cidade", description="Cidade do endereço")
    cep: str = Field(..., alias="endereco.cep", description="CEP do endereço")
    regiao: str = Field(..., alias="endereco.regiao", description="Região do endereço")
    nome: str = Field(
        ..., alias="endereco.nome", description="Nome relacionado ao endereço"
    )


class Empresa(BaseModel):
    """
    Representa os detalhes de uma empresa.
    """

    nome_fantasia: str = Field(
        ..., alias="empresa.nome_fantasia", description="Nome fantasia da empresa"
    )
    tipo_de_ie: str = Field(
        ...,
        alias="empresa.tipo_de_ie",
        description="Tipo de inscrição estadual da empresa",
    )
    data_inicio_de_atividade: str = Field(
        ...,
        alias="empresa.data_inicio_de_atividade",
        description="Data de início de atividade da empresa",
    )
    cnpj: str = Field(..., alias="empresa.cnpj", description="CNPJ da empresa")
    nire: str = Field(
        ...,
        alias="empresa.nire",
        description="Número de Identificação do Registro de Empresas (NIRE) da empresa",
    )
    data_de_fundacao: str = Field(
        ..., alias="empresa.data_de_fundacao", description="Data de fundação da empresa"
    )
    objeto_social: str = Field(
        ..., alias="empresa.objeto_social", description="Objeto social da empresa"
    )
    capital: str = Field(
        ..., alias="empresa.capital", description="Capital social da empresa"
    )
    endereco: List[Endereco] = Field(
        ...,
        alias="sinapses.Endereco",
        description="Lista de endereços associados à empresa",
    )


class SinapsesEmpresa(BaseModel):
    """
    Representa uma lista de empresas registradas.
    """

    empresa: List[Empresa] = Field(
        ..., alias="sinapses.Empresa", description="Lista de empresas"
    )


class RootHTML2(BaseModel):
    """
    Representa o modelo raiz que contém uma lista de SinapsesEmpresa.
    """

    root_html2: List[SinapsesEmpresa] = Field(
        ..., description="Lista de empresas registradas"
    )

    class Config:
        """
        Configuração da classe RootModel para permitir a popularização por nome.
        """

        populate_by_name = True
