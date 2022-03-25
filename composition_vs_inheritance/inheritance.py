from dataclasses import dataclass


@dataclass
class Duck:
    name: str

    def quack(self):
        print("base duck quack")

    def fly(self):
        print("base duck fly")


class JetDuck(Duck):
    def fly(self):
        print("jet duck fly")


class CloudDuck(Duck):

    def quack(self):
        print("cloud duck quack")

    # the problem is, if we use inheritance
    # if the cloudduck and jetduck uses same fly mechanism, there will be duplicated code
    def fly(self):
        print("jet duck fly")



if __name__ == "__main__":
    d = Duck(name="baseduck")
    d.quack()

    jd = JetDuck(name="het")
    jd.fly()

    cd = CloudDuck(name="ddd")
    cd.quack()