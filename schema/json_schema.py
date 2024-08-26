from typing import List

from pydantic import BaseModel, Field, HttpUrl


class PerfilWhatsApp(BaseModel):
    """
    Representa os detalhes do perfil WhatsApp.
    """

    numero: str = Field(
        ...,
        alias="perfil_whats_app.numero",
        description="Número de telefone do perfil WhatsApp",
    )
    status_info: float = Field(
        ...,
        alias="perfil_whats_app.status_info",
        description="Informação de status do perfil WhatsApp em timestamp",
    )
    status: str = Field(
        ...,
        alias="perfil_whats_app.status",
        description="Status atual do perfil WhatsApp",
    )
    imagem_de_perfil: HttpUrl = Field(
        ...,
        alias="perfil_whats_app.imagem_de_perfil",
        description="URL da imagem de perfil do WhatsApp",
    )


class SinapsesPerfilWhatsApp(BaseModel):
    """
    Representa uma lista de perfis WhatsApp.
    """

    perfil_whats_app: List[PerfilWhatsApp] = Field(
        ..., alias="sinapses.PerfilWhatsApp", description="Lista de perfis WhatsApp"
    )


class RootJSON(BaseModel):
    """
    Representa o modelo raiz que contém uma lista de SinapsesPerfilWhatsApp.
    """

    root_json: List[SinapsesPerfilWhatsApp] = Field(
        ..., description="Lista de perfis WhatsApp"
    )

    class Config:
        """
        Configuração da classe RootModel para permitir a popularização por nome.
        """

        populate_by_name = True
