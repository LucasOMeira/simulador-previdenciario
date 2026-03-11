from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Enum as SqlEnum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class ProcessStatus(str, Enum):
    EM_ANALISE = "em_analise"
    AGUARDANDO_DOCUMENTO = "aguardando_documento"
    DEFERIDO = "deferido"
    INDEFERIDO = "indeferido"


class BenefitType(str, Enum):
    APOSENTADORIA_IDADE = "aposentadoria_idade"
    AUXILIO_DOENCA = "auxilio_doenca"
    PENSAO_POR_MORTE = "pensao_por_morte"
    LOAS = "loas"


class Process(Base):
    __tablename__ = "processes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    process_number: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    benefit_type: Mapped[BenefitType] = mapped_column(
        SqlEnum(BenefitType, name="benefit_type"),
        nullable=False,
    )
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[ProcessStatus] = mapped_column(
        SqlEnum(ProcessStatus, name="process_status"),
        nullable=False,
        default=ProcessStatus.EM_ANALISE,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    user = relationship("User", back_populates="processes")