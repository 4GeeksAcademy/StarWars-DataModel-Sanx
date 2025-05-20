from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    lastname: Mapped[str] = mapped_column(String(120), nullable=False)
    suscription_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorite_planets: Mapped[list["FavoritePlanet"]] = relationship(back_populates="user")
    favorite_characters: Mapped[list["FavoriteCharacter"]] = relationship(back_populates="user")



    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "lastname": self.lastname,
            "subscription_date": self.subscription_date.isoformat(), 
        }

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    size: Mapped[int] = mapped_column(Integer, nullable=False)
    material: Mapped[str] = mapped_column(String(120), nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=False)
    favorite_planets_associations: Mapped[list["FavoritePlanet"]] = relationship(back_populates="planet")


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "material": self.material,
            "population": self.population,
        }
    
class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    genre: Mapped[str] = mapped_column(String(120), nullable=False)
    affiliation: Mapped[str] = mapped_column(String(120), nullable=False)
    favorite_characters_associations: Mapped[list["FavoriteCharacter"]] = relationship(back_populates="character")


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "genre": self.genre,
            "affiliation": self.affiliation,
        }
    
class FavoritePlanet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"))
    user: Mapped["User"] = relationship(back_populates="favorite_planets")
    planet: Mapped["Planet"] = relationship(back_populates="favorite_planets_associations")

class FavoriteCharacter(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))
    user: Mapped["User"] = relationship(back_populates="favorite_characters")
    character: Mapped["Character"] = relationship(back_populates="favorite_characters_associations")
