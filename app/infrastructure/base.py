from app.infrastructure.books.models import BookModel
# from app.infrastructure.outra_entidade.models import OutraEntidadeModel
from sqlalchemy.ext.declarative import declarative_base

Base = BookModel.metadata
