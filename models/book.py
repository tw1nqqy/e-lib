from schemas import Status
from datetime import datetime


class Book:
    __id = 0

    def __init__(self, title: str, author: str, year: int):
        self.__id = Book.generate_id()
        self.__title = title
        self.__author = author
        self.__year = year
        self.__status = Status.available

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title: str):
        self.__title = new_title

    @property
    def author(self):
        return self.__status.value

    @author.setter
    def author(self, new_author: str):
        self.__author = new_author

    @property
    def year(self):
        return self.__status.value

    @year.setter
    def year(self, new_year: int):
        self.__year = new_year

    @property
    def status(self):
        return self.__status.value

    @status.setter
    def status(self, new_status: Status):
        self.__status = new_status

    @classmethod
    def generate_id(cls):
        book_id = cls.__id
        cls.__id = datetime.now().timestamp()
        return book_id

    def __str__(self):
        return f"{self.__id}: {self.__title} | Author: {self.__author} | Year: {self.__year} | Status: {self.__status.value}"
