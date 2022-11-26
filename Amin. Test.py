class Home:
    name = 'M.Rizwan'

    def __init__(self, favouriteCricketer, highestRuns):
        self.favouriteCricketer = favouriteCricketer
        self.highestRuns = highestRuns

    def __str__(self):
        return f'Favourite Cricketer: {self.favouriteCricketer}\nHighest Score: {self.highestRuns}'


Amin = Home('M.Rizwan', '250')
print(Amin)
print(Home.name)
