def generate_employee_id(prefix='EMP', length=8):
    """
    Generate a random employee ID with the specified prefix and length.
    
    Args:
        prefix (str): Prefix for the employee ID (default: 'EMP')
        length (int): Length of the random part of the ID (default: 8)
        
    Returns:
        str: A unique employee ID in the format PREFIX_RANDOM
    """
    # Generate a random string of uppercase letters and digits
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    
    # Combine with timestamp for additional uniqueness
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    
    return f"{prefix}_{timestamp}_{random_part}"

# Example usage
if __name__ == "__main__":
    # Generate sample employee IDs
    print("Sample Employee IDs:")
    for _ in range(5):

        print(generate_employee_id())
