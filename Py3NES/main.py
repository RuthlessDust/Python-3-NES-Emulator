import argparse
from cpu import CPU

def main():
    #set up command line argument parser
    parser = argparse.ArgumentParser(description='NES Emulator')
    parser.add_argument('rom_path',
                        metavar='R',
                        type=str,
                        help='path to nes rom')
    args = parser.parse_args()

    # TODO: validate rom path is correct
    print(args.rom_path)

    #loading rom
    with open(args.rom_path, 'rb') as rom:
        lines = rom.readlines()

    #create CPU
    cpu = CPU()

    cpu.process_instruction(lines[0][0:3])

if __name__ == "__main__":
    main()
