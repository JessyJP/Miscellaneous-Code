A1 = [1, 1, 1, 1, 2 ,1 ,1 , 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 2, 0, 4,  0, 0, 3, 12, 0, 0, 0, 0, 10, 0, 0, 0]
A2 = [0, 1, 1, 1, 1, 2 ,1 ,1 , 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 2, 0, 4,  0, 0, 3, 12, 0, 0, 0, 0, 10, 0, 0, 0]
A3 = [0, 0, 1, 1, 1, 2 ,1 ,1 , 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 2, 0, 4,  0, 0, 3, 12, 0, 0, 0, 0, 10, 0, 0, 0]



def sort_zero(A):
    i_swap_left = 0
    i_check_right = 0
    SYMB = 0
    while (i_swap_left<len(A)):
        if(A[i_swap_left] == SYMB):

            # print(f"i_swap_left={i_swap_left} i_check_right={i_check_right}  array={A}")
            if i_swap_left > i_check_right:
                i_check_right = i_swap_left
                print(f"MOVE IND ===> Start check to from the swap: i_check_right={i_check_right}")
            
            # Find non-zero from the check position
            while (i_check_right<len(A)):
                if(A[i_check_right] != SYMB):
                    break;
                i_check_right+= 1
            # print(f"Find non-zero ind = {i_check_right}")

            # Exit condition
            if not( i_check_right < len(A)):
                print(f"End: i_swap_left={i_swap_left} array={A}")
                break

            # Swap
            print(f"swap A[{i_swap_left}] <==> A[{i_check_right}]")     
            # tmp = A[i_swap_left]
            A[i_swap_left] = A[i_check_right]
            A[i_check_right] = SYMB
            # print("")

        i_swap_left+=1


sort_zero(A1)
print("\n\n\n\n")
sort_zero(A2)
print("\n\n\n\n")
sort_zero(A3)