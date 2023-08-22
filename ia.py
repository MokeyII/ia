import ipaddress

# Define a function to generate IPv6 subnets
def generate_ipv6_subnets(prefix, subnet_prefix_length):
    # Create an IPv6Network object using the provided prefix
    base_subnet = ipaddress.IPv6Network(prefix, strict=False)
    
    # Generate a list of subnets within the base subnet with the specified prefix length
    subnets = list(base_subnet.subnets(new_prefix=subnet_prefix_length))
    
    # Return the list of generated subnets
    return subnets

# Define the main part of the script
if __name__ == "__main__":
    # Define the base IPv6 prefix
    prefix = "2001:db8:11:1234::/56"
    
    # Define the subnet prefix length
    subnet_prefix_length = 64
    
    # Call the function to generate subnets within the prefix
    subnets = generate_ipv6_subnets(prefix, subnet_prefix_length)
    
    # Print the generated subnets
    for subnet in subnets:
        print(subnet)
