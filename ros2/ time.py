from std_msgs.msg import Header

def to_seconds(header: Header) -> float:
    """Get time in seconds from a header."""
    
    return header.stamp.sec + header.stamp.nanosec * 1e-9