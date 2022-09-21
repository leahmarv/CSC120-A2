class Computer:

    # What attributes will it need?

    from typing import Dict, Union

    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.__description = description
        self.__processor_type = processor_type
        self.__hard_drive_capacity = hard_drive_capacity
        self.__memory = memory
        self.__operating_system = operating_system
        self.__year_made = year_made
        self.__price = price

    # What methods will you need?

    def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }