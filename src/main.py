import argparse
from model.assistant_call import gpt_call

def main(args):
    gpt_call(args.name, args.question)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Example script.")
    parser.add_argument('--name', type=str, default='mr. x', help='Your name')
    parser.add_argument('--question', type=str, default='blahblah', help='Your immigration question')
    
    args = parser.parse_args()
    main(args)
