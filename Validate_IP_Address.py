
def isValid(st):
        
    parts = st.split('.')
    if len(parts) != 4:  
        return False
    return all([pt.isdigit() and str(int(pt)) == pt and 0 <= int(pt) <= 255 for pt in parts])

st = input("Enter the IPv4 Address : ")
print("Is it an Valid IPv4 Address? ",isValid(st))

# Enter the IPv4 Address : 255.255.255.0
# Is it an Valid IPv4 Address?  True

# Enter the IPv4 Address : 020.20.255.0
# Is it an Valid IPv4 Address?  False