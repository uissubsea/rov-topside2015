from .. import rov

def main():
    rov_server = rov.RovServer()
    rov_server.start_server()

if __name__ == '__main__':
    main()