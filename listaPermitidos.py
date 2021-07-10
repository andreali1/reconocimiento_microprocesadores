class flabianos:

    def __init__(self):
        self.Invitados=['andree','Luis Sustaita',]

    def TuSiTuNo(self,EllosSi):        
        if EllosSi in self.Invitados:
            print('Bienvenido {}'.format(EllosSi))
        else:
            print('Lo siento {}, aun no trais el omnitrix'.format(EllosSi))
