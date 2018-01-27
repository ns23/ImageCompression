import argparse

def get_arguments():
    parser =  argparse.ArgumentParser(
        description="Image Compression utility in python",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d','--dir', help="Path to the folder")
    group.add_argument('-f','--file',help="Path to file")    

    parser.add_argument(
        '-q','--quality',default=60,type=int,
        help='Image compression value'
    )

    parsed = parser.parse_args()

    return parsed
