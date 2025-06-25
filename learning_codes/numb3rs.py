import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    nums = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    
    if nums:
        nums = nums.groups()
        #nums = int(nums)
        for i in nums:
            i = int(i)
            if  i >= 255 or i <= 0:
                return False
        return True
    else:
        
        return False




...


if __name__ == "__main__":
    main()