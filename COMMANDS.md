# Commands

Place to save some commands related to PyPGLib development, deployment, and maintenance.

## Download PGLib

### Windows (`cmd`)

```plaintext
curl -L https://github.com/power-grid-lib/pglib-opf/archive/refs/tags/v21.07.zip > pglib-opf.zip
tar -xf pglib-opf.zip
ren pglib-opf-21.07 opf
move opf pglib
move pglib-opf.zip backup
```

```plaintext
curl -L https://github.com/power-grid-lib/pglib-uc/archive/refs/tags/v19.08.zip > pglib-uc.zip
tar -xf pglib-uc.zip
ren pglib-uc-19.08 uc
move uc pglib
move pglib-uc.zip backup
```

```plaintext
curl -L https://github.com/power-grid-lib/pglib-opf-hvdc/archive/refs/tags/v19.08.zip > pglib-opf-hvdc.zip
tar -xf pglib-opf-hvdc.zip
ren pglib-opf-hvdc-19.08 hvdc
move hvdc pglib
move pglib-opf-hvdc.zip backup
```

Note: Sometimes it is not working from inside `vscode` terminal, since `vscode` use `powershell` instead of `cmd`. Try use to use windows `cmd` instead.

<!-- 
TODO: 
    1. Powershell command for curl and tar
 -->


## Delete dist

Delete old dist if exist to avoid the unexpected.

```powershell
del dist -Recurse -Force
del pglib.egg-info -Recurse -Force
```

## Tags

```powershell
git tag -a v0.0.1 -m "v0.0.1: Initial PyPGLib"
```
