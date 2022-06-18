import sys

def main():
    list_argv = sys.argv
    if len(list_argv) != 2:
        sys.exit(f'Only accept 1 argument as target app name')
    
    __import__(f"services.{list_argv[1]}.main")

    
if __name__ == "__main__":
    # container = Container()
    # container.wire(modules=[__name__])

    main()