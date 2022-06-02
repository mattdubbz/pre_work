from math import fabs


fav_nums = {
    "matt": [37, 32, 12],
    "jess": [69, 54, 83],
    "aaron": [35, 67, 80],
    "cornbread": [64, 23, 65],
    "rupid": [98, 54, 26],
}
for name, nums in fav_nums.items():
    print(name + "'s favite number are: ")
    for num in nums:
        print("\t" + str(num))
    print("======================")
