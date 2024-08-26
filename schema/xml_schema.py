from typing import List, Optional

from pydantic import BaseModel, Field


class Telefone(BaseModel):
    """
    Representa os detalhes de um telefone.
    """

    numero_tel: str = Field(
        ..., alias="telefone.numero_tel", description="Número de telefone"
    )
    operadora: str = Field(
        ..., alias="telefone.operadora", description="Operadora do telefone"
    )
    whatsapp: Optional[str] = Field(
        None,
        alias="telefone.whatsapp",
        description="Indica se o número é associado ao WhatsApp",
    )


class Location(BaseModel):
    """
    Representa os detalhes de um endereço ou localização.
    """

    logradouro: str = Field(
        ..., alias="location.logradouro", description="Logradouro do endereço"
    )
    numero: str = Field(..., alias="numero", description="Número do endereço")
    complemento: Optional[str] = Field(
        None, alias="complemento", description="Complemento do endereço"
    )
    bairro: Optional[str] = Field(
        None, alias="location.bairro", description="Bairro do endereço"
    )
    cep: Optional[str] = Field(
        None, alias="location.cep", description="CEP do endereço"
    )
    cidade: Optional[str] = Field(
        None, alias="location.cidade", description="Cidade do endereço"
    )
    estado: str = Field(..., alias="location.estado", description="Estado do endereço")
    label_default_key: Optional[str] = Field(
        None, alias="label_default_key", description="Chave de referência padrão"
    )


class Email(BaseModel):
    """
    Representa os detalhes de um email.
    """

    email: str = Field(..., alias="email.email", description="Endereço de email")


class Pessoa(BaseModel):
    """
    Representa os detalhes de uma pessoa.
    """

    cpf: str = Field(..., alias="pessoa.cpf", description="CPF da pessoa")
    fullname: str = Field(
        ..., alias="pessoa.fullname", description="Nome completo da pessoa"
    )
    cargo_em_sociedade: str = Field(
        ...,
        alias="pessoa.cargo_em_sociedade",
        description="Cargo da pessoa na sociedade",
    )
    participacao: str = Field(
        ...,
        alias="pessoa.participacao",
        description="Participação da pessoa na sociedade",
    )
    location: Optional[List[Location]] = Field(
        None,
        alias="sinapses.location",
        description="Lista de localizações associadas à pessoa",
    )
    label_default_key: Optional[str] = Field(
        None, alias="label_default_key", description="Chave de referência padrão"
    )
    credilink_label: Optional[str] = Field(
        None, alias="credilink_label", description="Etiqueta de credilink"
    )
    reverse: Optional[bool] = Field(
        None, alias="reverse", description="Indicador de reversão"
    )


class Empresa(BaseModel):
    """
    Representa os detalhes de uma empresa.
    """

    cnpj: str = Field(..., alias="empresa.cnpj", description="CNPJ da empresa")
    razao_social: str = Field(
        ..., alias="empresa.razao_social", description="Razão social da empresa"
    )
    status_receita: str = Field(
        ...,
        alias="empresa.status_receita",
        description="Status da empresa na Receita Federal",
    )
    razao_social1: Optional[str] = Field(
        None,
        alias="empresa.razao_social1",
        description="Segunda razão social da empresa",
    )
    porte: str = Field(..., alias="empresa.porte", description="Porte da empresa")
    total_de_funcionarios: str = Field(
        ...,
        alias="empresa.total_de_funcionarios",
        description="Total de funcionários na empresa",
    )
    quantidade_de_funcionarios_acima_de_5_salarios: Optional[str] = Field(
        None,
        alias="empresa.quantidade_de_funcionarios_acima_de_5_salarios",
        description="Quantidade de funcionários com salários acima de 5 salários mínimos",
    )
    quantidade_de_funcionarios_abaixo_de_5_salarios: Optional[str] = Field(
        None,
        alias="empresa.quantidade_de_funcionarios_abaixo_de_5_salarios",
        description="Quantidade de funcionários com salários abaixo de 5 salários mínimos",
    )
    telefone: Optional[List[Telefone]] = Field(
        None,
        alias="sinapses.telefone",
        description="Lista de telefones associados à empresa",
    )
    location: Optional[List[Location]] = Field(
        None,
        alias="sinapses.location",
        description="Lista de localizações associadas à empresa",
    )
    email: Optional[List[Email]] = Field(
        None, alias="sinapses.email", description="Lista de emails associados à empresa"
    )
    pessoa: Optional[List[Pessoa]] = Field(
        None,
        alias="sinapses.pessoa",
        description="Lista de pessoas associadas à empresa",
    )


class SinapsesEmpresa(BaseModel):
    """
    Representa uma lista de empresas registradas.
    """

    empresa: List[Empresa] = Field(
        ..., alias="sinapses.empresa", description="Lista de empresas"
    )


class RootXML(BaseModel):
    """
    Representa o modelo raiz que contém uma lista de SinapsesEmpresa.
    """

    root_xml: List[SinapsesEmpresa] = Field(
        ..., description="Lista de empresas registradas"
    )

    class Config:
        """
        Configuração da classe RootModel para permitir a popularização por nome.
        """

        populate_by_name = True
