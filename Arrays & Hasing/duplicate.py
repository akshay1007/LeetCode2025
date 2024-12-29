# This is a simple script that prints some output,
#  for demonstration purposes.

def find_duplicates(nums):
    seen = set()
    duplicates = []
    for num in nums:
        if num in seen:
            duplicates.append(num)
        seen.add(num)
    return duplicates

if __name__ == "__main__":
    nums = [1, 2, 2, 3, 4, 5, 5, 6]
    duplicates = find_duplicates(nums)
    print(f"Duplicate numbers: {duplicates}")
