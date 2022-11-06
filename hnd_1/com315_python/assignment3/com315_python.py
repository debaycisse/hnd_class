from TowerHanoi import HanoiTower

peg1 = peg2 = peg3 = []
num_of_disk = 3

my_pegs = HanoiTower(num_of_disk, peg1, peg2, peg3)

is_all_disk_in_peg2 = False

print("\n" + "-" * 20 + " Moving Hanoi Disk " + "-" * 20 + "\n")  # Display message
print(my_pegs.peg1)

if len(my_pegs.peg3) == 0:
    print(my_pegs.move_1_to_3())
# elif len(my_pegs.peg2) == 0:
#     my_pegs.move_1_to_2()

# print(my_pegs.peg3)
# print(my_pegs.peg1)

# while not is_all_disk_in_peg2:
#     if len(my_pegs.peg1) == 0 and len(my_pegs.peg3) == 0:
#         is_all_disk_in_peg2 = True
#     elif len(my_pegs.peg3) == 0:
#         my_pegs.move_1_to_3()
#     elif len(my_pegs.peg2) == 0:
#         my_pegs.move_1_to_2()
#     elif len(my_pegs.peg1) == 0 and my_pegs.peg3[len(my_pegs.peg3)-1] > my_pegs.peg2[len(my_pegs.peg2)-1]:
#         my_pegs.move_2_to_3()
#     elif len(my_pegs.peg1) == 0 and my_pegs.peg2[len(my_pegs.peg2)-1] > my_pegs.peg3[len(my_pegs.peg3)-1]:
#         my_pegs.move_2_to_1()
#     elif len(my_pegs.peg2) == 0 and my_pegs.peg3[len(my_pegs.peg3)-1] < my_pegs.peg1[len(my_pegs.peg1)-1]:
#         my_pegs.move_3_to_1()
#     elif len(my_pegs.peg2) == 0 and my_pegs.peg3[len(my_pegs.peg3)-1] > my_pegs.peg1[len(my_pegs.peg1)-1]:
#         my_pegs.move_3_to_2()
#     elif len(my_pegs.peg3) == 0 and my_pegs.peg2[len(my_pegs.peg2)-1] > my_pegs.peg1[len(my_pegs.peg1)-1]:
#         my_pegs.move_1_to_3()
#     elif my_pegs.peg2[len(my_pegs.peg2)-1] > my_pegs.peg3[len(my_pegs.peg3)-1] and my_pegs.peg1[len(my_pegs.peg1)-1] > my_pegs.peg3[len(my_pegs.peg3)-1]:
#         my_pegs.move_1_to_2()
#     elif len(my_pegs.peg1) == 0 and my_pegs.peg3[len(my_pegs.peg3)-1] < my_pegs.peg2[len(my_pegs.peg2)-1]:
#         my_pegs.move_3_to_2()
#     elif my_pegs.peg2[len(my_pegs.peg2)-1] > my_pegs.peg3[len(my_pegs.peg3)-1]:
#         my_pegs.move_3_to_2()
#     elif my_pegs.peg3[len(my_pegs.peg3)-1] > my_pegs.peg2[len(my_pegs.peg2)-1]:
#         my_pegs.move_2_to_3()
