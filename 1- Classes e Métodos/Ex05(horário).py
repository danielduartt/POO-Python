'''
Crie uma classe para representar um horario (hora, minuto e segundo). Implemente os ´
metodos para fazer as operac¸ ´ oes de incremento (de segundos) no hor ˜ ario e diferenc¸a ´
entre dois horarios.
'''

class Horario():
    def __init__(self, hora, min, seg):
        self.hora = hora
        self.min = min
        self.seg = seg

    def __str__(self):
        return f"{self.hora:02d}:{self.min:02d}:{self.seg:02d}"

    def incremento(self, segAdd):
        total_segundos = self.hora * 3600 + self.min * 60 + self.seg + segAdd
        self.hora = total_segundos // 3600
        self.minuto = (total_segundos % 3600) // 60
        self.segundo = total_segundos % 60

    def __sub__(self, other):
        seg_self = self.hora * 3600 + self.min * 60 + self.seg
        seg_other = other.hora * 3600 + other.min * 60 + other.seg
        subtracao = abs(seg_self - seg_other)
        hora = subtracao // 3600
        min = (subtracao % 3600) // 60
        seg = subtracao % 60
        return Horario(hora, min, seg)


horario1 = Horario(10,30,10)
horario2 = Horario(14, 14, 0)
print(horario2)
print(horario1)
sub = horario2 - horario1
print(sub)
