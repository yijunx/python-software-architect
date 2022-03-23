from bank import Bank
from controler import BankControler
from commands import Transfer, Deposite, Withdraw, Batch


def main():
    bank = Bank()

    controller = BankControler()

    acc1 = bank.create_account(name="tom1")
    acc2 = bank.create_account(name="tom2")
    acc3 = bank.create_account(name="tom3")

    # deposite
    controller.execute(
        transaction=Batch(
            commands=[
                Deposite(account=acc1, amount=100000),
                Deposite(account=acc2, amount=100000),
                Deposite(account=acc3, amount=100000),
            ]
        )
    )
    controller.undo()
    controller.redo()

    # transker
    controller.execute(
        transaction=Transfer(from_account=acc2, to_account=acc1, amount=50000)
    )

    # withdraw
    controller.execute(transaction=Withdraw(account=acc1, amount=150000))

    controller.undo()

    print(bank)


if __name__ == "__main__":
    main()
