'''
YijunCoin (YC)

tranction 1: Anna sends Bob 2 YC
t2: Bob sends Daniel 4.3 YC
t3: Mark sends Charlie 3.2 YC

Block 1, the initial block, B1("AAA", t1, t2, t3):
B1("AAA", t1, t2, t3) --hash-func--> 7dfh90

B2, will have more transactions
B2("7dfh90", t4, t5, t6) --hash-func--> j83gfn

so we can have more and more blocks, it's like a linkedlist which cannot go backward

the essence is that we cannot change any of the transaction in between
because all the later on hash will be altered.

we can verify the integrity by checking the end of the hash

'''

import hashlib
from typing import List

class CoinBlock:
    def __init__(self, previous_block_hash: str, transaction_list: List[str]) -> None:
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = " AND ".join(transaction_list) + " AFTER " + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

    def __repr__(self) -> str:
        return self.block_data + " \n hash: " + self.block_hash


if __name__ == "__main__":

    t1 = "Anna sends Bob 2 YC"
    t2 = "Bob sends Daniel 4.3 YC"
    t3 = "Mark sends Charlie 3.2 YC"
    t4 = "Yijun sends Willow 20 YC"
    t5 = "Bob sends Yijun 7.5 YC"
    t6 = "Anna sends Mark 0.2 YC"


    b1 = CoinBlock("initial-hash", transaction_list=[t1, t2])
    b2 = CoinBlock(b1.block_hash, transaction_list=[t3, t4])
    b3 = CoinBlock(b2.block_hash, transaction_list=[t5, t6])

    print(b1)
    print(b2)
    print(b3)


