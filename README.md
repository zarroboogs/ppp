
# PS4 Persona Patches

A set of patches for the PS4 Persona games.

## Contents

- [Requirements](#requirements)
- [Usage](#usage)
  - [Listing Available Patches](#listing-available-patches)
  - [Applying Patches](#applying-patches)
- [Available Patches](#available-patches)
  - [Persona 5 (PS4)](#persona-5-ps4)
  - [Persona 5 Royal](#persona-5-royal)
  - [Persona 5 Dancing](#persona-5-dancing)
  - [Persona 3 Dancing](#persona-3-dancing)
  - [Persona 4 Dancing](#persona-4-dancing)
- [Building a Custom PS4 Patch](#building-a-custom-ps4-patch)

## Requirements

- [`xdelta`](https://github.com/jmacd/xdelta-gpl) in `PATH`
- Python 3
- A homebrew enabled PS4
- Some files from the game you'd like to patch:
  - `eboot.bin` - **must be dumped in ELF format** or converted to it from a fake signed ELF,
  e.g. using [ps4_unfself](https://github.com/SocraticBliss/ps4_unfself)
  - `npbind.dat` and `nptitle.dat`
  - When repacking a game update - all other data files that were originally included in said update (e.g. `patch2R.cpk` for P5R v1.02)

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
  0505           PS4 FW 5.05 Backport
  all_dlc        Content Enabler
  dlc_msg        Skip DLC Unlock Messages
  intro_skip     Intro Skip
  mod_support    Mod Support
  mod_support2   Mod Support Alt
  no_trp         Disable Trophies
  p5_save        P5 Save Bonus Enabler
  share_button   Enable Share Button
  square         Global Square Menu
  env            ENV Test
  zzz            Random Tests
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

For CUSA05877 (US) v1.00, CUSA06638 (EU) v1.00

- *Content Enabler* - Enables on-disc content

- *Intro Skip* - Skips boot logos and intro movie

- *Mod Support (PKG)* - File replacement via `USRDIR/mod.cpk` (PKG)

- *Mod Support (FTP)* - File replacement via `/data/p5/mod.cpk` (FTP)

- *Disable Trophies* - Prevents the game from unlocking trophies

- *Enable Share Button* - Enables video recording and screenshots using share button

- *Global Square Menu* - Enables the square menu globally (e.g. in Velvet Room or during events or game sections which disable it)

- *ENV Tests* - Maps all `env/env*.ENV` to `env/env0000_000_000.ENV`

- *Random Tests*
  - Maps all `field/qr/*.dds` to `field/qr/qr_tex0000.dds` (file doesn't exist by default)
  - Maps all `test/zeal_tex/*.dds` to `test/zeal_tex/tex_0000.dds` (file doesn't exist by default)

### Persona 5 Royal

For CUSA17416 (US) v1.02, CUSA17419 (EU) v1.02

- *PS4 FW 5.05 Backport*

- *Content Enabler* - Enables on-disc content

- *Skip DLC Unlock Messages* - Especially useful when using the *Content Enabler* patch together with a mod that skips the title screen and boots directly into a field.

- *Intro Skip* - Skips boot logos and intro movie (can still be viewed in Thieves Den)

- *Mod Support*

  File replacement via (from lowest to highest load priority):
  - `USRDIR/mod.cpk` (PKG)
  - `/data/p5r/mod.cpk` (FTP)
  - Loose files in `/data/p5r/bind/` (FTP HostFS)[^loose]

  When using a language other than English, the game will also try to load (from lowest to highest priority):
  - `USRDIR/mod_X.cpk` (PKG)
  - `/data/p5r/mod_X.cpk` (FTP)
  - Loose files in `/data/p5r/bind_X/` (FTP HostFS)[^loose]

  Replace `X` with `F`, `I`, `G`, or `S` for French, Italian, German or Spanish respectively.

  Language specific files have a higher load priority than base English files.

- *Disable Trophies* - Prevents the game from unlocking trophies

- *P5 Save Bonus Enabler* - Enables P5 save bonus without P5 saves present on system

- *Enable Share Button* - Enables video recording and screenshots using share button

- *Global Square Menu* - Enables the square menu globally (e.g. in Thieves Den and in Velvet Room or during events or game sections which disable it)

- *Randomized Battle BGM* - Plays a different battle BGM track regardless of equipped MC outfit

- *Sequential Battle BGM* - Plays a different battle BGM track regardless of equipped MC outfit

- *ENV Tests* - Maps all `env/env*.ENV` to `env/env0000_000_000.ENV`

- *Random Tests*
  - Maps all `field/qr/*.dds` to `field/qr/qr_tex0000.dds` (file doesn't exist by default)
  - Maps all `test/zeal_tex/*.dds` to `test/zeal_tex/tex_0000.dds` (file doesn't exist by default)

### Persona 5 Dancing

For CUSA12380 (US) v1.00

- *Intro Skip* - Skips boot logos and intro movie

- *Mod Support* - File replacement via (from lowest to highest load priority):
  - `data/mod.cpk` (PKG)
  - `/data/p5d/mod.cpk` (FTP)
  - Loose files in `/data/p5d/bind/` (FTP HostFS)[^loose]

- *Disable Screenshot Overlay* - Removes the annoying copyright overlay from in-game screenshots

- *Disable Trophies* - Prevents the game from unlocking trophies

### Persona 3 Dancing

For CUSA12636 (US) v1.00

- *Intro Skip* - Skips boot logos and intro movie

- *Mod Support* - File replacement via (from lowest to highest load priority):
  - `data/mod.cpk` (PKG)
  - `/data/p3d/mod.cpk` (FTP)
  - Loose files in `/data/p3d/bind/` (FTP HostFS)[^loose]

- *Disable Screenshot Overlay* - Removes the annoying copyright overlay from in-game screenshots

- *Disable Trophies* - Prevents the game from unlocking trophies

### Persona 4 Dancing

For CUSA12811 (EU) v1.00

- *Intro Skip* - Skips boot logos and intro movie

- *Mod Support* - File replacement via (from lowest to highest load priority):
  - `data/mod.cpk` (PKG)
  - `/data/p4d/mod.cpk` (FTP)
  - Loose files in `/data/p4d/bind/` (FTP HostFS)[^loose]

- *Disable Trophies* - Prevents the game from unlocking trophies

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

   If `eboot.bin` is not in ELF format, you must convert it to ELF (e.g. using [ps4_unfself](https://github.com/SocraticBliss/ps4_unfself)) before applying patches.

   Place the patched `eboot.bin` in the provided `patch/` directory.

3. If you've applied a mod support patch, package the mods you'd like to use into a `mod.cpk` file using your preferred method.

   Replace the dummy `mod.cpk` in the in the provided `patch/` directory.

   Alternatively, if you're using the ftp `mod.cpk` method, upload `mod.cpk` to the correct location in the filesystem.

4. Edit `patch.gp4` and set `app_path` to point to your base game package.

5. Build the patch package with your preferred tool, install it and boot the game.

[^loose]: Loose files are loaded via a debug function that might be unstable.
