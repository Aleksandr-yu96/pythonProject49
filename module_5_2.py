class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        """Возвращает количество этажей здания."""
        return self.number_of_floors

    def __str__(self):
        """Возвращает строку с названием и количеством этажей."""
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def go_to(self, floor):
        """Переходит на указанный этаж."""
        if 1 <= floor <= self.number_of_floors:
            return f"Перешли на этаж {floor} в доме {self.name}."
        else:
            return "Этаж не существует в этом доме."

# Пример использования

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__

print(h1)
print(h2)

# __len__

print(len(h1))
print(len(h2))

# go_to

print(h1.go_to(5))
print(h1.go_to(15))  # Несуществующий этаж
print(h2.go_to(10))
print(h2.go_to(30))  # Несуществующий этаж
