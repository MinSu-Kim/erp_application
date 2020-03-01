class Title:
    def __init__(self, title_no=None, title_name=None):
        self.__title_no = title_no
        self.__title_name = title_name

    @property
    def title_no(self):  # getter
        return self.__title_no

    @title_no.setter
    def title_no(self, title_no):  # setter  getter먼저 선언 후 선언해야 됨.
        self.__title_no = title_no

    @property
    def title_name(self):
        return self.__title_name

    @title_name.setter
    def title_name(self, title_name):
        self.__title_name = title_name

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __iter__(self):
        return (i for i in (self.__title_no, self.__title_name))

    def __repr__(self) -> str:
        return '{}({!r}, {!r})'.format(type(self).__name__, *self)

    def __hash__(self):
        return hash(self.__title_no) ^ hash(self.__title_name)

    def get_to_dict(self):
        return {'title_no': self.__title_no, 'title_name': self.__title_name}


if __name__ == "__main__":
    t1 = Title()
    t1.title_no = None
    t1.title_name = '부장'
    print('t1', t1)
    t1.title_no = 2
    print('t1', t1)

    t2 = Title(**{'title_no': 1, 'title_name': '과장'})
    print('t2', t2)

    t3 = Title(3)
    print(t3)

    t4 = Title(title_no=4, title_name='대리')
    print(t4)

    dict_title = {'title_no': 5}
    t5 = Title(**dict_title)
    print(t5)

    titleList = [Title(), Title(**{'title_no': 1}), Title(**{'title_no': 1, 'title_name': '영업'})]
    for obj in titleList:
        print(obj)

    print(Title(1, '사장') == Title(1))
    print(Title(1, '사장') == Title('사장'))
    print(Title(1, '사장') == Title(1, '사장'))     # __iter__
    print(set([t1, t2, t3]))                      # __hash__

    for title in set([t1, t2, t3]):
        print(title, title.get_to_dict(), tuple(title))