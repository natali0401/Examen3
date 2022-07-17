class Tomato:
    states={1:"vshod",2:"buton",3:"cvetok",4:"plod"}

    def __init__(self, _index):
        self._index=_index
        self._state=1


    def grow(self):
        self._change()

    def is_ripe(self):
        if self._state==4:
            return True
        return False


    def _change(self):
        if self._state<4:
            self._state+=1
        self._itog_state()

    def _itog_state(self):
        print(f'Tomato{self._index} is {Tomato.states[self._state]}')


class TomatoBush:


    def __init__(self, colich):
        self.tomatoes=[Tomato(index) for index in range(1,colich)]


    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()


    def all_are_ripe(self):
        return  all([tomato.is_ripe() for tomato in self.tomatoes])


    def give_away_all(self):
        self.tomatoes=[]


class Gardener:

    def __init__(self, name, _plant):
        self.name=name
        self._plant=_plant


    def work(self):
        print("Садовник работает")
        self._plant.grow_all()
        print("Садовник окончил работать")


    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собрали")
        else:
            print("Урожай не готов")


    @staticmethod
    def knowledge_base():
        print('''Температура воздуха в теплице должна составлять 20 °С, ночью — около 18 °С, 
              а грунта — от 15 °С. Необходимо, чтобы влажность составляла 60%. Нужно также 
              периодически поливать и проветривать теплицу, делать листовые подкормки с кремнием.
               Для теплицы подойдут жаростойкие и теневыносливые сорта томатов.''')

Gardener.knowledge_base()
tomat=TomatoBush(5)
gard=Gardener("Ivan", tomat)
gard.work()
gard.work()
gard.harvest()
gard.work()
gard.harvest()