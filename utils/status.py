from enum import Enum


class Status(Enum):
    CODE200 = "200 OK",
    CODE404 = "404 METHOD NOT FOUND",
    CODE401 = "401 UNAUTHORIZED",
    CODE500 = "500 SERVER ERROR",
    CODE300 = "300 DATABASE ERROR"
