import os
import random

#The "bcolors" class uses "ANSI escape sequences" for color formatting text in the terminal
class bcolors:
    #This mainly helps for readability of "GREEN" rather then "\u001b[32m"
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    GREY = '\u001b[2m'
    ENDC = '\033[0m'
    RED = '\033[91m'

def CalcSubnet(StartIndex,SubnetBits):
    subnet = 128*int(SubnetBits[StartIndex])+64*int(SubnetBits[1+StartIndex])+32*int(SubnetBits[2+StartIndex])+16*int(SubnetBits[3+StartIndex])+8*int(SubnetBits[4+StartIndex])+4*int(SubnetBits[5+StartIndex])+2*int(SubnetBits[6+StartIndex])+1*int(SubnetBits[7+StartIndex])
    return(subnet)

def GenIPv4(PrefixLength, ipv4Index):
    ipv4Index[0] = random.randint(1,223)
    ipv4Index[1] = random.randint(0,255)
    ipv4Index[2] = random.randint(0,255)
    ipv4Index[3] = random.randint(0,255)
    ipv4 = str(ipv4Index[0])+"."+str(ipv4Index[1])+"."+str(ipv4Index[2])+"."+str(ipv4Index[3])
    
    if ipv4Index[0] == 10:
        NetworkClass = "PA"
    elif ipv4Index[0] < 127:
        NetworkClass = "A"
    elif ipv4Index[0] == 127:
        NetworkClass = "L"
    elif 172 + 16 <= ipv4Index[0] + ipv4Index[1] <= 172 + 31:
        NetworkClass = "PB"
    elif ipv4Index[0] < 192:
        NetworkClass = "B"
    elif ipv4Index[0] + ipv4Index[1] == 192 + 168:
        NetworkClass = "PC"
    elif ipv4Index[0] < 224:
        NetworkClass = "C"
    else:
        NetworkClass = "-1"
        print("Something Went Wrong")
    
    return((f"{ipv4}/{PrefixLength}"), NetworkClass)

def GenSubnetMask(SubnetBits,SubnetIndex):
    
    SubnetIndex[0] = CalcSubnet(0,SubnetBits)
    SubnetIndex[1] = CalcSubnet(8,SubnetBits)
    SubnetIndex[2] = CalcSubnet(16,SubnetBits)
    SubnetIndex[3] = CalcSubnet(24,SubnetBits)

    SubnetMask = f"{SubnetIndex[0]}.{SubnetIndex[1]}.{SubnetIndex[2]}.{SubnetIndex[3]}"
    
    return(SubnetMask)

def CalcIPcount(SubnetIndex):
    
    TotalIPs = (256-SubnetIndex[0])*(256-SubnetIndex[1])*(256-SubnetIndex[2])*(256-SubnetIndex[3])
    UsableIPs = TotalIPs - 2

    return(TotalIPs, UsableIPs)

def CalcNetworkCount(SubnetIndex):
    print()
    if SubnetIndex[3] != 0:
        NetworkCount = 256-SubnetIndex[3]
    elif SubnetIndex[2] != 0:
        NetworkCount = 256-SubnetIndex[2]
    else:
        NetworkCount = 256-SubnetIndex[1]
    
    if NetworkCount == 256:
        NetworkCount = 1
        
    return(NetworkCount)

def main():

    os.system('cls')
    
    SubnetIndex = [None]*4
    ipv4Index = [None]*4
    PrefixLength = random.randint(8,30)
    SubnetBits = (("1"*PrefixLength) + ("0"*(32-PrefixLength)))

    SubnetMask = GenSubnetMask(SubnetBits,SubnetIndex)

    IPv4, NetworkClass = GenIPv4(PrefixLength, ipv4Index)

    TotalIPs, UsableIPs = CalcIPcount(SubnetIndex)

    NetworkCount = CalcNetworkCount(SubnetIndex)

    print("Welcome to the IPv4 Subnet Quiz!")
    print(f"Here is the IP Address: {IPv4}")
    print()
    
    SubnetMaskGuess = input("1.........Subnet mask?:")
    TotalIPsGuess = input("2......Total IP count?:")
    UsableIPsGuess = input("3.....Usable IP count?:")
    NetworkCountGuess = input("4.Total network count?:")
    NetworkClassGuess = input("5.......Network Class?:")
    os.system('cls')

    print("Welcome to the IPv4 Subnet Quiz!")
    print(f"Here is the IP Address: {IPv4}")
    print()

    if str(SubnetMaskGuess) == str(SubnetMask):
        print(f"{bcolors.GREEN}1.........Subnet mask?:{SubnetMaskGuess}{bcolors.ENDC}")
    else:
        print(f"{bcolors.RED}1.........Subnet mask?:{SubnetMaskGuess}{bcolors.ENDC} {bcolors.GREEN}{SubnetMask}{bcolors.ENDC}")

    if str(TotalIPsGuess) == str(TotalIPs):
        print(f"{bcolors.GREEN}2......Total IP count?:{TotalIPsGuess}{bcolors.ENDC}")
    else:
        print(f"{bcolors.RED}2......Total IP count?:{TotalIPsGuess}{bcolors.ENDC} {bcolors.GREEN}{TotalIPs}{bcolors.ENDC}")

    if str(UsableIPsGuess) == str(UsableIPs):
        print(f"{bcolors.GREEN}3.....Usable IP count?:{UsableIPsGuess}{bcolors.ENDC}")
    else:
        print(f"{bcolors.RED}3.....Usable IP count?:{UsableIPsGuess}{bcolors.ENDC} {bcolors.GREEN}{UsableIPs}{bcolors.ENDC}")

    if str(NetworkCountGuess) == str(NetworkCount):
        print(f"{bcolors.GREEN}4.Total network count?:{NetworkCountGuess}{bcolors.ENDC}")
    else:
        print(f"{bcolors.RED}4.Total network count?:{NetworkCountGuess}{bcolors.ENDC} {bcolors.GREEN}{NetworkCount}{bcolors.ENDC}")

    if str(NetworkClassGuess) == str(NetworkClass):
        print(f"{bcolors.GREEN}5.......Network Class?:{NetworkClassGuess}{bcolors.ENDC}")
    else:
        print(f"{bcolors.RED}5.......Network Class?:{NetworkClassGuess}{bcolors.ENDC} {bcolors.GREEN}{NetworkClass}{bcolors.ENDC}")
#This is so we can import the functions in this program in other code without having to run the main function

if __name__ == "__main__":
    main()