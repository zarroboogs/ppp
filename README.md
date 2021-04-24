# PS4 Persona Patches

A set of patches for the PS4 Persona games.

## Requirements

- [`xdelta`](https://github.com/jmacd/xdelta-gpl) in `PATH`
- `python`
- A homebrew enabled PS4
- `eboot.bin` for the game you'd like to patch (**must be dumped in ELF format** or converted to it from a fake signed ELF, e.g. using [ps4_unfself](https://github.com/SocraticBliss/ps4_unfself))

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
Found Persona 5 Royal US CUSA17416 0102

Available patches:
  0505          PS4 FW 5.05 Backport
  all_dlc       Content Enabler
  intro_skip    Intro Skip
  mod_support   Mod Support
  no_trp        Disable Trophies
  p5_save       P5 Save Bonus Enabler
  square        Global Square Menu
  env           ENV Test
  zzz           Random Tests
```

### Applying Patches

```txt
python .\patch.py .\eboot.bin --patch 0505 all_dlc intro_skip mod_support no_trp p5_save square
```

Example output:

```txt
Found Persona 5 Royal US CUSA17416 0102

Applying patches...

<...>

Applied 0505 all_dlc intro_skip mod_support no_trp p5_save square
Done
```

## Available Patches

### Persona 5 (PS4)

Tested on CUSA06638 (EU v1.00). Requires a custom v1.01 patch (see below).

- *Content Enabler* - Enables on-disc content
- *Intro Skip* - Skips boot logos and intro movie
- *Mod Support* - File replacement via a `mod.cpk` file
- *Disable Trophies* - Prevents the game from unlocking trophies
- *Global Square Menu* - Enables the square menu globally (e.g. in Velvet Room or during events or game sections which disable it)
- *ENV Tests* - Maps all `env/env*.ENV` to `env/env0000_000_000.ENV`
- *Random Tests*
  - Maps all `field/qr/*.dds` to `field/qr/qr_tex0000.dds` (file doesn't exist by default)
  - Maps all `test/zeal_tex/*.dds` to `test/zeal_tex/tex_0000.dds` (file doesn't exist by default)

### Persona 5 Royal

Tested on CUSA17416 (US v1.02).

- *PS4 FW 5.05 Backport*
- *Content Enabler* - Enables on-disc content
- *Intro Skip* - Skips boot logos and intro movie (can still be viewed in Thieves Den)
- *Mod Support* - File replacement via a `mod.cpk` file
- *Disable Trophies* - Prevents the game from unlocking trophies
- *P5 Save Bonus Enabler* - Enables P5 save bonus without P5 saves present on system
- *Global Square Menu* - Enables the square menu globally (e.g. in Thieves Den and in Velvet Room or during events or game sections which disable it)
- *ENV Tests* - Maps all `env/env*.ENV` to `env/env0000_000_000.ENV`
- *Random Tests*
  - Maps all `field/qr/*.dds` to `field/qr/qr_tex0000.dds` (file doesn't exist by default)
  - Maps all `test/zeal_tex/*.dds` to `test/zeal_tex/tex_0000.dds` (file doesn't exist by default)

## Building a Custom Persona 5 (PS4) Patch

1. Dump the following files from your copy of Persona 5:

   ```txt
   sce_sys/npbind.dat
   sce_sys/nptitle.dat
   eboot.bin
   ```

   Place `npbind.dat` and `nptitle.dat` in the provided `patch/sce_sys/` directory.

2. Apply the patches you'd like to use to `eboot.bin`.

   **Note that the mod support patch is required for loading `mod.cpk`.**

   Place the patched `eboot.bin` in the provided `patch/USRDIR/` directory.

3. Package the mods you'd like to use into a `mod.cpk` file using your preferred method.

   Place `mod.cpk` in the `patch/USRDIR/` directory (an empty dummy `mod.cpk` is provided in the patch directory, replace it with your own).

4. Edit `patch.gp4` and set `app_path` to point to your base Persona 5 package.

5. Check that your final `patch/` directory structure matches the following listing:

   ```txt
   patch/sce_sys/changeinfo/changeinfo.xml
   patch/sce_sys/npbind.dat
   patch/sce_sys/nptitle.dat
   patch/sce_sys/param.sfo
   patch/USRDIR/mod.cpk
   patch/eboot.bin
   patch.gp4
   ```

6. Build the patch package with your preferred tool, install it and boot the game.
