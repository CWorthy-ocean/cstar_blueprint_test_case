# cstar_blueprint_test_case
Minimal test case of C-Star with roms-tools and ROMS-MARBL 

## Namelists and ucla-roms versions

Each directory under `additional_code/` holds the case's run-time files (`runtime_code/namelist.nml`, `runtime_code/marbl_in`) and its compile-time `compile_time_code/cppdefs.opt`. A namelist only works with the ucla-roms releases it was written for, so there is one directory per release line:

| Directory | ucla-roms |
|---|---|
| `additional_code/ROMS` | 0.4.2 and the earlier commits that older C-Star releases pin |
| `additional_code/ROMS-ucla-roms-0.13` | 0.13.0 |

The 0.13 namelist differs from the older one in two ways:

- `nrpf_rst` is gone, and the particle output keys are `nrpf_particles` and `output_period_particles`.
- A new history file has to start at each restart write, which ucla-roms 0.5.0 and later require: the physics and BGC history files now hold 5 records of 120 s each, so a new one starts at the 600 s restart.

`cppdefs.opt` and `marbl_in` are unchanged copies.
