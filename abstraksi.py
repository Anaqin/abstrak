class cupang:
    def __init__(naqi, q):
        naqi.quest = q
        naqi.jaw = []
        naqi.isi = []
        naqi.nilai = 0

    def otot(self):
        if self.quest == "M":
            print("_ _ _ _ _")
            self.isi = [int(x) for x in input("jawaban: ").split()]
            print("jawaban yang bener: ", self.jaw)
            print("skor", self.nilai)


    def kawat(self):
        import random

        x = [1, 2, 3, 4, 5]
        y = ["n", "a", "q", "i"]

        for i in range(len(x)):
            k = random.choice(x)
            self.jaw.append(k)
            x.remove(k)

    def skor(self):
        if self.jaw[0] == self.isi:
            self.nilai += 20
        elif self.jaw[1] == self.isi[1]:
            self.nilai += 20
        elif self.jaw[2] == self.isi[2]:
            self.nilai += 20
        elif self.jaw[3] == self.isi[3]:
            self.nilai += 20
        elif self.jaw[4] == self.isi[4]:
            self.nilai += 20

def output():
    print("selamat datamg")
    q = cupang(input("ketik [M] jika sudah siap bermain :"))
    q.otot()

if __name__ == "__main__":
    while True:
        output()