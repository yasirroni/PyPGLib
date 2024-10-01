# Commands

Place to save some commands related to PyPGLib development, deployment, and maintenance.

## Download PGLib

### MacOS (`zsh`)

> **Note**  
> `rm` is required to avoid creating subfolder

```plaintext
curl -L https://github.com/power-grid-lib/pglib-opf/archive/refs/tags/v23.07.zip > pglib-opf.zip
unzip pglib-opf.zip -d temps
rm -r pypglib/opf
mv temps/pglib-opf-23.07 pypglib/opf
mv pglib-opf.zip backup/pglib-opf.zip
```

```plaintext
curl -L https://github.com/power-grid-lib/pglib-uc/archive/refs/tags/v19.08.zip > pglib-uc.zip
unzip pglib-uc.zip -d temps
rm -r pypglib/uc
mv temps/pglib-uc-19.08 pypglib/uc
mv pglib-uc.zip backup/pglib-uc.zip
```

```plaintext
curl -L https://github.com/power-grid-lib/pglib-opf-hvdc/archive/refs/tags/v23.09.zip > pglib-opf-hvdc.zip
unzip pglib-opf-hvdc.zip -d temps
rm -r pypglib/hvdc
mv temps/pglib-opf-hvdc-23.09 pypglib/hvdc
mv pglib-opf-hvdc.zip backup/pglib-opf-hvdc.zip
```

### Windows (`cmd`)

```plaintext
curl -L https://github.com/power-grid-lib/pglib-opf/archive/refs/tags/v21.07.zip > pglib-opf.zip
tar -xf pglib-opf.zip
ren pglib-opf-21.07 opf
move opf pypglib
move pglib-opf.zip backup
```

```plaintext
curl -L https://github.com/power-grid-lib/pglib-uc/archive/refs/tags/v19.08.zip > pglib-uc.zip
tar -xf pglib-uc.zip
ren pglib-uc-19.08 uc
move uc pypglib
move pglib-uc.zip backup
```

```plaintext
curl -L https://github.com/power-grid-lib/pglib-opf-hvdc/archive/refs/tags/v19.08.zip > pglib-opf-hvdc.zip
tar -xf pglib-opf-hvdc.zip
ren pglib-opf-hvdc-19.08 hvdc
move hvdc pypglib
move pglib-opf-hvdc.zip backup
```

Note: Sometimes it is not working from inside `vscode` terminal, since `vscode` use `powershell` instead of `cmd`. Try use to use windows `cmd` instead.

<!-- 
TODO: 
    1. Powershell command for curl and tar
-->

## Copy python scripts

```shell
xcopy /y /s scripts\*.* pypglib\
```

```shell
cp -r scripts/* pypglib/
```

## Delete dist

Delete old dist if exist to avoid the unexpected.

```powershell
del dist -Recurse -Force
del pypglib.egg-info -Recurse -Force
```

## Tags

```powershell
git tag -a v0.0.1 -m "v0.0.1: Initial PyPGLib"
git tag -a v0.0.2 -m "v0.0.2: pglib-opf v23.07 | pglib-opf-hvdc v23.09"
```

## pre-commit

```shell
pre-commit install
pre-commit run --all-files
```
