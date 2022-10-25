# Moving Disk Class
class HanoiTower:
    def __init__(self, num_of_disk, peg1, peg2, peg3):
        # Generate disks
        for disk in range(1, num_of_disk+1):
            peg1.append(disk)
        # Initialize each peg
        peg1.reverse()  # To have biggest number (disk) at the bottom
        self.num_of_disk = num_of_disk
        self.peg1 = peg1
        self.peg2 = peg2
        self.peg3 = peg3

    # Moving disk logics
    def move_1_to_2(self):
        self.peg2.append(self.peg1.pop())
        print("1 -> 2")

    def move_1_to_3(self):
        self.peg3.append(self.peg1.pop())
        print("1 -> 3")
    
    def move_2_to_1(self):
        self.peg1.append(self.peg2.pop())
        print("2 -> 1")

    def move_2_to_3(self):
        self.peg3.append(self.peg2.pop())
        print("2 -> 3")

    def move_3_to_1(self):
        self.peg1.append(self.peg3.pop())
        print("3 -> 1")

    def move_3_to_2(self):
        self.peg2.append(self.peg3.pop())
        print("3 -> 2")

