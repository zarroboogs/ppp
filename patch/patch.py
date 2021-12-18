
import sys
import argparse
import subprocess
from pathlib import Path

sys.dont_write_bytecode = True

from xdelta.conf import games, patches

def read_at(f, o, c):
    f.seek(o, 0)
    return f.read(c)

def detect_xdelta():
    try:
        rc = subprocess.run("xdelta -V", stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def detect_format(path):
    with open(path, 'rb') as eboot:
        return eboot.read(4) == b"\x7FELF"

def detect_game(path):
    with open(path, 'rb') as eboot:
        for g in games:
            ok = True
            for c in g['check']:
                ok &= read_at(eboot, c['offset'], len(c['value'])) == c['value']
            if ok:
                return g
        return None

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('path_in', help="path to game eboot (in ELF format)")
    parser.add_argument('path_out', help="path to patched game eboot", nargs='?')
    parser.add_argument('--patch', help="patch ids to apply", nargs='+')
    return parser.parse_args(args)

def apply_patches(path_in, path_out, apply):
    subprocess.run(f"xdelta -vfn merge {' '.join(apply)} ./tmp.xdelta")
    subprocess.run(f"xdelta -vfn -d -s {path_in} ./tmp.xdelta {path_out}")

def main():
    # check for prereqs
    if not detect_xdelta():
        print("xdelta not in path\n")
        exit(1)

    # parse args
    args = parse_args(sys.argv[1:])
    path_in = Path(args.path_in)

    # check for elf
    if not detect_format(args.path_in):
        print("Input not in ELF format\n")
        exit(1)

    # check if supported
    game = detect_game(path_in)
    if not game:
        print("Unsupported game or game version\n")
        exit(1)
    print(f"Found {game['name']} {game['title']} {game['version']}\n")

    # collect available patches
    game_patches = {p['id'] : p for p in patches
        if game['title'] in p['games'] and game['version'] in p['games'][game['title']]}

    # print available patches if no patch input is given
    if not args.patch:
        print("Available patches:")
        w = max([len(gp) for gp in game_patches])
        for gp in game_patches:
            print(f"  {gp:{w + 2}} {game_patches[gp]['name']}")
        print("")
        exit(0)

    # check output path
    path_out = Path(f"{path_in}--patched.bin")
    if args.path_out:
        path_out = Path(args.path_out)
    if path_in == path_out:
        print("Output path can't be identical to input path\n")
        exit(1)

    # generate patch apply list and apply
    apply = []
    apply_pids = []
    for pid in args.patch:
        if pid not in game_patches:
            print(f"Unknown patch id {pid}, skipping...")
            continue
        patch_path = Path("xdelta") / game_patches[pid]['path']
        if not patch_path.is_file():
            print(f"Patch file for id {pid} not found, skipping...")
            continue
        apply.append(patch_path.absolute().as_posix())
        apply_pids.append(pid)

    if not len(apply):
        print("No patches to apply\n")
        exit(1)

    for i in range(0, len(apply) - 1):
        apply[i] = f"-m{apply[i]}"

    print("Applying patches...\n")
    apply_patches(path_in, path_out, apply)
    print("")
    print(f"Applied {' '.join(apply_pids)}")
    print("Done\n")

if __name__ == '__main__':
    main()
