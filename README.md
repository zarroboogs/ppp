
# PS Persona Patches

A set of patches for the PSV/PS4 Persona games.

## Contents

- [Requirements](#requirements)
- [Usage](#usage)
  - [Listing Available Patches](#listing-available-patches)
  - [Applying Patches](#applying-patches)
- [Available Patches](#available-patches)
- [Building a Custom PS4 Patch](#building-a-custom-ps4-patch)
- [Patching PS Vita Games](#patching-ps-vita-games)

## Requirements

- [`xdelta`][xdelta_url] in `PATH`
- Python 3

## Usage

Clone or download this repository, then use `patch.py` to apply patches:

```txt
patch.py [-h] [--patch [PATCH]] path_in [path_out]

positional arguments:
  path_in          path to game eboot (in ELF format)
  path_out         path to patched game eboot

optional arguments:
  -h, --help       show this help message and exit
  --patch [PATCH]  patch ids to apply
```

### Listing Available Patches

```txt
python .\patch.py .\eboot.bin
```

Example output:

```txt
Found Persona 5 Royal US v1.02 CUSA17416 0102

Available patches:
  intro_skip   Intro Skip
  mod          Mod Support
  no_trp       Disable Trophies
```

### Applying Patches

```txt
python .\patch.py .\eboot.bin --patch intro_skip mod
```

Example output:

```txt
Found Persona 5 Royal US CUSA17416 0102

Applying patches...

<...>

Applied intro_skip mod
Done
```

## Available Patches

- Persona 5 ([PS4][p5_ps4])
- Persona 5 Royal ([PS4][p5r_ps4])
- Persona 4 Dancing ([PS4][p4d_ps4]/[PSV][p4d_psv])
- Persona 3 Dancing ([PS4][p3d_ps4]/[PSV][p3d_psv])
- Persona 5 Dancing ([PS4][p5d_ps4]/[PSV][p5d_psv])

## Building a Custom PS4 Patch

The [pkg](pkg) directory in this repo contains some templates you can use to build a custom patch package.

You may need to edit some files to match your version (e.g. `param.sfo`, `patch.gp4`, etc.)

The general process is:

1. Dump the following files from your game:

   ```txt
   sce_sys/npbind.dat
   sce_sys/nptitle.dat
   eboot.bin
   ```

   Replace the dummy `npbind.dat` and `nptitle.dat` in the provided `patch/sce_sys/` directory.

2. Apply the patches you'd like to use to `eboot.bin`.

   If `eboot.bin` is not in ELF format, you must convert it to ELF (e.g. using [ps4_unfself][ps4_unfself_url] before applying patches.

   Place the patched `eboot.bin` in the provided `patch/` directory.

3. If you've applied a mod support patch, package the mods you'd like to use into a `mod.cpk` file using your preferred method.

   Replace the dummy `mod.cpk` in the in the provided `patch/` directory.

   Alternatively, if you're using the ftp `mod.cpk` method, upload `mod.cpk` to the correct location on the PS4 filesystem.

4. Edit `patch.gp4` and set `app_path` to point to your base game package.

5. Build the patch package with your preferred tool. When repacking a game update, make sure to also include all other data files that were originally included in said update (e.g. `patch2R.cpk` for P5R v1.02).

6. Install the package on your PS4 and boot the game.

## Patching PS Vita Games

1. Dump a **decrypted** `eboot.bin` and `eboot.elf` for your game:

   - On PS Vita, use [FAGDec][fagdec_url] and decrypt to SELF **and** ELF.
   - On PC, using Vita3K:
     - Install the game (and any game patches) - the decrypted `eboot.bin` should then be in the game folder.
     - Convert `eboot.bin` from SELF to ELF format using [`vita-unmake-self`][vufself_url].

2. Patch `eboot.elf`.

3. Backup the original `eboot.bin`.

4. Inject the patched `eboot.elf` back into the original `eboot.bin` using [`vita-elf-inject`][veinject_url].

5. Replace the original `eboot.bin`:

   - On PS Vita, use [rePatch][repatch_url].
   - On PC, using Vita3K, overwrite the original `eboot.bin`.

[xdelta_url]: https://github.com/jmacd/xdelta-gpl

[p5_ps4]: docs/Persona_5_PS4.md
[p5r_ps4]: docs/Persona_5_PS4.md
[p4d_ps4]: docs/Persona_4_Dancing_PS4.md
[p4d_psv]: docs/Persona_4_Dancing_PSV.md
[p3d_ps4]: docs/Persona_3_Dancing_PS4.md
[p3d_psv]: docs/Persona_3_Dancing_PSV.md
[p5d_ps4]: docs/Persona_5_Dancing_PS4.md
[p5d_psv]: docs/Persona_5_Dancing_PSV.md

[ps4_unfself_url]: https://github.com/SocraticBliss/ps4_unfself

[fagdec_url]: https://github.com/CelesteBlue-dev/PSVita-RE-tools/tree/master/FAGDec/build
[vufself_url]: https://github.com/CelesteBlue-dev/PSVita-RE-tools/tree/master/vita-unmake-fself/release
[veinject_url]: https://github.com/CelesteBlue-dev/PSVita-RE-tools/tree/master/elf_injector/build
[repatch_url]: https://github.com/dots-tb/rePatch-reDux0
