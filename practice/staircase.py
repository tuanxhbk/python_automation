def create_staircase_a(nums):
  while len(nums) != 0:
    step = 1
    subsets = []
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False

  return subsets

def create_staircase_b(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

if __name__ == "__main__":
    input_1 = [1, 2, 3, 4, 5, 6]
    input_2 = [1, 2, 3, 4, 5, 6, 7]
    
    print(f"Response A: {create_staircase_a(input_1)}")  # Expected: [[1], [2, 3], [4, 5, 6]]
    print(f"Response A: {create_staircase_a(input_2)}")  # Expected: False

    print(f"Response B: {create_staircase_b(input_1)}")  # Expected: [[1], [2, 3], [4, 5, 6]]
    print(f"Response B: {create_staircase_b(input_2)}")  # Expected: False