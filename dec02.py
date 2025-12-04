def part1(input_str):
    sum_all = 0
    invalid_ids = []

    for range_str in input_str.split(','):
        range_list = [int(i) for i in range_str.split('-')]
        for i in range(range_list[0], range_list[1] +1):
            if len(str(i)) % 2 == 0: # Skip odd numbers
                char_symetric_position = int(len(str(i)) / 2)
                left, right = str(i)[:char_symetric_position], str(i)[char_symetric_position:]
                if left == right:
                    print(f"Found invalid ID: {i}")
                    sum_all += i
                    invalid_ids.append(i)
    
    print("List of invalid IDs:")
    print(*invalid_ids)
    print(f"Sum of all invalid ID is {sum_all}")

def part2(input_str):
    sum_all = 0
    invalid_ids = []

    for range_str in input_str.split(','):
        range_list = [int(i) for i in range_str.split('-')]
        for current_i in range(range_list[0], range_list[1] +1):
            max_char_position = int(len(str(current_i)) / 2)
            for pos in range(1, max_char_position + 1): # Split at starting from every char, to split the string to 2
                split_list = [str(current_i)[i:i+pos] for i in range(0, len(str(current_i)), pos)] # split string to a list
                if (current_i not in invalid_ids # Not already in the invalid_ids
                    and len(split_list)>=2 # Repeat at least twice
                    and all(x == split_list[0] for x in split_list) # all items are the same
                    ): 
                    sum_all += current_i
                    invalid_ids.append(current_i)
    
    print("List of invalid IDs:")
    print(*invalid_ids)
    print(f"Sum of all invalid ID is {sum_all}")

