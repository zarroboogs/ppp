
import sys
import argparse
import subprocess
from pathlib import Path

sys.dont_write_bytecode = True

from xdelta.conf import games

def read_at(f, o, c):
    f.seek(o, 0)
    return f.read(c)

def detect_game(path):
    with open(path, 'rb') as eboot:
        if eboot.read(4) != b"\x7FELF":
            print("input not in ELF format")
            return

        for g in games:
            ok = True
            for c in g['check']:
                ok &= read_at(eboot, c['offset'], len(c['value'])) == c['value']
            if ok:
                print(f"Found {g['name']} {g['title']} {g['version']}\n")
                return g

    print("Unsupported game or game version")
    exit(1)

def apply_patches(path_in, path_out, apply):
    subprocess.run(f"xdelta -vfn merge {' '.join(apply)} ./tmp.xdelta")
    subprocess.run(f"xdelta -vfn -d -s {path_in} ./tmp.xdelta {path_out}")

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('path_in', help="path to game eboot (in ELF format)")
    parser.add_argument('path_out', help="path to patched game eboot", nargs='?')
    parser.add_argument('--patch', help="patch ids to apply", nargs='+')
    return parser.parse_args(args)

def check_xdelta():
    try:
        rc = subprocess.run("xdelta -V", stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print("xdelta not in path")
        exit(1)

def main():
    check_xdelta()
    args = parse_args(sys.argv[1:])

    path_in = Path(args.path_in)

    # check if supported
    g = detect_game(path_in)

    # print available patches if not patch input is given
    if not args.patch:
        print("Available patches:")
        w = max([len(x['id']) for x in g['patches']])
        for p in g['patches']:
            print(f"  {p['id']:{w + 2}} {p['name']}")
        print("")
        exit(0)

    # check output path
    path_out = Path(f"{path_in}--patched.bin")
    if args.path_out:
        path_out = Path(args.path_out)
    if path_in == path_out:
        print("Output path can't be identical to input path")
        exit(1)

    # generate patch apply list and apply
    pids = [ x['id'] for x in g['patches'] ]
    path = Path(g['path'])
    apply = []
    apply_pids = []
    for pid in args.patch:
        if pid not in pids:
            print(f"Unknown patch id {pid}, skipping...")
            continue
        patch_path = path / f"{pid}.xdelta"
        if not patch_path.is_file():
            print(f"Patch file for id {pid} not found, skipping...")
            continue
        apply_pids.append(pid)
        apply.append(patch_path.absolute().as_posix())

    if not len(apply):
        print("No patches to apply\n")
        exit(1)

    for i in range(0, len(apply) - 1):
        apply[i] = f"-m{apply[i]}"

    print("Applying patches...\n")
    apply_patches(path_in, path_out, apply)
    print(f"\nApplied {' '.join(apply_pids)}")
    print("Done\n")

if __name__ == '__main__':
    main()
