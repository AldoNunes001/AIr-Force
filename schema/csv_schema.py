from typing import List, Optional

from pydantic import BaseModel, Field


class Vinculo(BaseModel):
    """Representa um vínculo financeiro ou estimável."""

    valor: Optional[float] = Field(None, alias="'valor'")
    data: Optional[str] = Field(None, alias="'data'")
    documento: Optional[str] = Field(None, alias="'documento'")
    recibo: Optional[str] = Field(None, alias="'recibo'")
    especie: Optional[str] = Field(None, alias="'especie'")
    natureza: Optional[str] = Field(None, alias="'natureza'")
    origem: Optional[str] = Field(None, alias="'origem'")
    fonte: Optional[str] = Field(None, alias="'fonte'")
    tipo: Optional[str] = Field(None, alias="'tipo'")
    data_cadastro: Optional[str] = Field(None, alias="'data_cadastro'")
    vinculo_rotulo: Optional[str] = Field(None, alias="'vinculo.rotulo'")
    descricao: Optional[str] = Field(None, alias="'descricao'")
    natureza_estimavel: Optional[str] = Field(None, alias="'natureza_estimavel'")
    vinculo_reverso: Optional[bool] = Field(None, alias="'vinculo.reverso'")

    class Config:
        populate_by_name = True


class Empresa(BaseModel):
    """Detalhes da empresa associada a um candidato."""

    cnpj: Optional[str] = Field(None, alias="'empresa.cnpj'")
    razao_social: Optional[str] = Field(None, alias="'empresa.razao_social'")
    razao_social1: Optional[str] = Field(None, alias="'empresa.razao_social1'")
    cnae: Optional[str] = Field(None, alias="'empresa.cnae'")
    vinculo: Optional[List[Vinculo]] = Field(None, alias="sinapses.vinculo")

    class Config:
        populate_by_name = True


class Pessoa(BaseModel):
    """Informações sobre uma pessoa."""

    pessoa_cpf: Optional[str] = Field(None, alias="'pessoa.cpf'")
    pessoa_fullname: Optional[str] = Field(None, alias="'pessoa.fullname'")
    vinculo: Optional[List[Vinculo]] = Field(None, alias="sinapses.vinculo")
    candidato: Optional[List["Candidato"]] = Field(None, alias="sinapses.candidato")
    empresa: Optional[List[Empresa]] = Field(None, alias="sinapses.empresa")

    class Config:
        populate_by_name = True


class Candidato(BaseModel):
    """Detalhes de um candidato em uma eleição."""

    ano_da_eleicao: Optional[int] = Field(None, alias="'candidato.ano_da_eleicao'")
    tipo_da_eleicao: Optional[str] = Field(None, alias="'candidato.tipo_da_eleicao'")
    descricao_da_eleicao: Optional[str] = Field(
        None, alias="'candidato.descricao_da_eleicao'"
    )
    data_da_eleicao: Optional[str] = Field(None, alias="'candidato.data_da_eleicao'")
    unidade_eleitoral: Optional[str] = Field(
        None, alias="'candidato.unidade_eleitoral'"
    )
    turno_da_eleicao: Optional[int] = Field(None, alias="'candidato.turno_da_eleicao'")
    cargo_eleitoral: Optional[str] = Field(None, alias="'candidato.cargo_eleitoral'")
    numero_do_candidato: Optional[int] = Field(
        None, alias="'candidato.numero_do_candidato'"
    )
    partido_eleitoral: Optional[str] = Field(
        None, alias="'candidato.partido_eleitoral'"
    )
    empresa: Optional[List[Empresa]] = Field(None, alias="sinapses.empresa")
    pessoa: Optional[List[Pessoa]] = Field(None, alias="sinapses.pessoa")

    class Config:
        populate_by_name = True


class RootElement(BaseModel):
    """Elemento raiz que engloba todas as outras estruturas."""

    sinapses_pessoa: Optional[List[Pessoa]] = Field(None, alias="sinapses.pessoa")
    sinapses_candidato: Optional[List[Candidato]] = Field(
        None, alias="sinapses.candidato"
    )

    class Config:
        populate_by_name = True


class RootCSV(BaseModel):
    """Estrutura raiz que contém uma lista de RootElement."""

    root_csv: List[RootElement]

    class Config:
        populate_by_name = True
