# The guest enters username and password.
# should receive an ACK msg from the system

from src.main.DomainLayer import Registration


def register(username, password):
    ackMSG = Registration.register(username, password)