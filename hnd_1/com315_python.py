# This is the answer to a question, which is contained in com_315_assignment3.pdf file.

class TowerOfHanoi():
    '''Move Disks from Peg 1 to Peg 2'''
    def __init__(self, num_of_disk, peg1, peg2, peg3):
        for i in range(1, self.num_of_disk+1):
            peg1.append('disk{}'.format(i))
        peg1.reverse()
        
        self.num_of_disk = num_of_disk
        self.peg1 = peg1; self.peg2 = peg2; self.peg3 = peg3

    def move_disks(self):
        # if self.num_of_disk <= 1:
        #     self.peg2.append(self.peg1.pop())
        #     print("1 -> 2")
        #     return
        # elif self.num_of_disk == 2:
        #     self.peg3.append(self.peg1.pop())
        #     print("1 -> 3")
        #     self.peg2.append(self.peg1.pop())
        #     print("1 -> 2")
        #     self.peg2.append(self.peg3.pop())
        #     print("3 -> 2")
        #     return
        # elif self.num_of_disk == 3:
        #     self.peg3.append(self.peg1.pop())
        #     print("1 -> 3")


        for disk in self.peg1:
            if len(self.peg1) == self.num_of_disk and self.num_of_disk > 2:
                while len(self.peg1) != 0:  # while peg1 is not empty.
                    if len(self.peg2) == 0:
                        self.peg2.append(self.peg1.pop())
                        print("1 -> 2")
                    elif len(self.peg3) == 0:
                        self.peg3.append(self.peg1.pop())
                        print("1 -> 3")
                    elif self.peg3[len(self.peg3)-1] > self.peg2[len(self.peg2)-1]:
                        self.peg3.append(self.peg2.pop())
                        print("2 -> 3")
                    elif len(self.peg1) == 1:
                        self.peg2.append(self.peg1.pop())
                        print("1 -> 2")    # peg 1 should be empty after this line here.
                        # TODO checks if the remaining disk in peg3 is more than 2

                        # TODO check if the remaining disk in peg3 is exactly 2
                        self.peg1.append(self.peg2.pop())
                        print("2 -> 1")
                        self.peg3.append(self.peg2.pop())
                        print("2 -> 3")


                    
                    if len(self.peg2) == 0 and len(self.peg3) == 0:
                        

                    else:
                        pass
    
            elif len(self.peg1) == self.num_of_disk and self.num_of_disk == 2:
                self.peg3.append(self.peg1.pop())
                print("1 -> 3")
                self.peg2.append(self.peg1.pop())
                print("1 -> 2")
                self.peg2.append(self.peg3.pop())
                print("3 -> 2")
                return                
            elif len(self.peg1) == self.num_of_disk and self.num_of_disk == 1:
                self.peg2.append(self.peg1.pop())
                print("1 -> 2")
                return                


