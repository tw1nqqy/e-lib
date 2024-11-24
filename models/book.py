from schemas import Status


class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: Status):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__year = year
        self.__status = status

    def to_json(self) -> dict:
        return {
            "id": self.__id,
            "title": self.__title,
            "author": self.__author,
            "year": self.__year,
            "status": self.__status
        }

    @property
    def id(self) -> int:
        return self.__id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, new_title: str):
        if not new_title:
            raise ValueError("Title cannot be empty.")
        self.__title = new_title

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, new_author: str):
        if not new_author:
            raise ValueError("Author cannot be empty.")
        self.__author = new_author

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, new_year: int):
        if new_year < 0:
            raise ValueError("Year cannot be negative.")
        self.__year = new_year

    @property
    def status(self) -> str:
        return self.__status.value

    @status.setter
    def status(self, new_status: Status):
        if not isinstance(new_status, Status):
            raise ValueError("Status must be an instance of Status enum.")
        self.__status = new_status

    def __str__(self):
        return f"{self.__id}: {self.__title} | Author: {self.__author} | Year: {self.__year} | Status: {self.__status.value}"
