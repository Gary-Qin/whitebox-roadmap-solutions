import sys
input = lambda: sys.stdin.readline().strip("\n")

def main():
    num = input()
    final_sum = 0
    
    def subsets(remaining_num, index, subset_sum):
        nonlocal final_sum
        if index == 0:
            final_sum += subset_sum + int(remaining_num)
        else:
            subsets(remaining_num[:index], index - 1, subset_sum + int(remaining_num[index:]))
            subsets(remaining_num, index - 1, subset_sum)
    
    subsets(num, len(num) - 1, 0)

    print(final_sum)

main()