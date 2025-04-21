# A python script to do COWSAY
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python fun.py <message>")
        sys.exit(1)
    
    message = " ".join(sys.argv[1:])
    cow = r"""
       {message}
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
    """.format(message=message)
    print(cow)

if __name__ == "__main__":
    main()