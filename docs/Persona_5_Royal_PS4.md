
# Persona 5 Royal (PS4)

## Versions

- CUSA17416 (US) v1.02
- CUSA17419 (EU) v1.02

## Patches

- *PS4 FW 5.05 Backport*

- *Content Enabler* - Enables on-disc content

- *Skip DLC Unlock Messages* - Especially useful when using the *Content Enabler* patch together with a mod that skips the title screen and boots directly into a field.

- *Intro Skip* - Skips boot logos and intro movie (can still be viewed in Thieves Den)

- *Mod Support*

  File replacement via (from highest to lowest load priority):
  - Loose files in `/data/p5r/bind/`
  - `/data/p5r/mod.cpk`
  - `/data/p5r/mod1.cpk`
  - `/data/p5r/mod2.cpk`
  - `/data/p5r/mod3.cpk`
  - `USRDIR/mod.cpk` (in pkg)

  When using a language other than English, the game will also try to load (from highest to lowest load priority):
  - Loose files in `/data/p5r/bind_X/`
  - `/data/p5r/mod_X.cpk`
  - `/data/p5r/mod1_X.cpk`
  - `/data/p5r/mod2_X.cpk`
  - `/data/p5r/mod3_X.cpk`
  - `USRDIR/mod_X.cpk` (in pkg)

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
