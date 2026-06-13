---
entity_id: "complex.ecocyc.CYT-O-UBIOX-CPLX"
entity_type: "complex"
name: "cytochrome bo3 ubiquinol:oxygen oxidoreductase"
source_database: "EcoCyc"
source_id: "CYT-O-UBIOX-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ubiquinol oxidase (H<sup>+</sup>-transporting)"
  - "cytochrome <i>bo</i> ubiquinol oxidase"
  - "cytochrome <i>o</i> ubiquinol oxidase"
  - "ubiquinol:oxygen oxidoreductase"
  - "cytochrome b562-o complex"
  - "cytochrome <i>bo<sub>3</sub></i>"
  - "cytochrome <i>bo</i><sub>3</sub> terminal oxidase"
---

# cytochrome bo3 ubiquinol:oxygen oxidoreductase

`complex.ecocyc.CYT-O-UBIOX-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CYT-O-UBIOX-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABJ6|protein.P0ABJ6]], [[protein.P0ABJ1|protein.P0ABJ1]], [[protein.P0ABI8|protein.P0ABI8]], [[protein.P0ABJ3|protein.P0ABJ3]]

## Enriched Summary

The E. coli K-12 genome encodes 3 quinol:oxygen oxidoreductases - cytochrome bo (cyoABCD), CYT-D-UBIOX-CPLX cytochrome bd-I (cydABX-cydH) and APP-UBIOX-CPLX cytochrome bd-II (appCBX). The three enzymes function as the major terminal oxidases in the aerobic respiratory chain of E. coli. Cytochrome bo is expressed when oxygen levels are high while cytochrome bd-I is expressed under oxygen limited conditions . Both enymes contribute to the generation of a proton motive force (PMF), cytochrome bo functions as a proton pump whilst cytochrome bd-I does not . The energetics of cytochrome bd-II are less clear; initial reports suggested that it did not contribute to PMF while later work suggests that it generates PMF with an H+/e- (protons translocated per electron) ratio of 0.94 . Cytochrome bo catalyzes the two-electron oxidation of ubiquinol within the membrane and the four-electron reduction of molecular oxygen to water. The enzyme contributes to the PMF (H+/e-=2) through its action as a proton pump (H+/e-=1) and through a redox loop mechanism (H+/e-=1) ( and see review by ). Cytochrome bo consists of four subunits (I - IV) encoded by the cyoB, cyoA, cyoC and cyoD genes respectively , all of which are necessary for enzyme function . The fifth gene of the cyo operon, cyoE encodes a heme O synthase which is essential for correct assembly of the complex...

## Biological Role

Catalyzes RXN0-5268 (reaction.ecocyc.RXN0-5268). Bound by Heme (molecule.C00032), Heme O (molecule.C15672), Cu2+ (molecule.ecocyc.CU_2).

## Annotation

The E. coli K-12 genome encodes 3 quinol:oxygen oxidoreductases - cytochrome bo (cyoABCD), CYT-D-UBIOX-CPLX cytochrome bd-I (cydABX-cydH) and APP-UBIOX-CPLX cytochrome bd-II (appCBX). The three enzymes function as the major terminal oxidases in the aerobic respiratory chain of E. coli. Cytochrome bo is expressed when oxygen levels are high while cytochrome bd-I is expressed under oxygen limited conditions . Both enymes contribute to the generation of a proton motive force (PMF), cytochrome bo functions as a proton pump whilst cytochrome bd-I does not . The energetics of cytochrome bd-II are less clear; initial reports suggested that it did not contribute to PMF while later work suggests that it generates PMF with an H+/e- (protons translocated per electron) ratio of 0.94 . Cytochrome bo catalyzes the two-electron oxidation of ubiquinol within the membrane and the four-electron reduction of molecular oxygen to water. The enzyme contributes to the PMF (H+/e-=2) through its action as a proton pump (H+/e-=1) and through a redox loop mechanism (H+/e-=1) ( and see review by ). Cytochrome bo consists of four subunits (I - IV) encoded by the cyoB, cyoA, cyoC and cyoD genes respectively , all of which are necessary for enzyme function . The fifth gene of the cyo operon, cyoE encodes a heme O synthase which is essential for correct assembly of the complex . Sequence analyses indicate that the complex is similar to the aa3-type family of cytochrome c oxidases . The enzyme contains two heme groups - high spin heme O and low spin heme B - plus a single copper (CuB). The heme O and copper are magnetically coupled and constitute a heme-copper binuclear center which is the site of oxygen reduction. The enzyme lacks a CuA center which is typical of cytochrome c oxidases ( and reviewed b

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5268|reaction.ecocyc.RXN0-5268]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (7)

- `binds` <-- [[molecule.C00032|molecule.C00032]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C15672|molecule.C15672]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ABI8|protein.P0ABI8]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABJ1|protein.P0ABJ1]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABJ3|protein.P0ABJ3]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABJ6|protein.P0ABJ6]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CYT-O-UBIOX-CPLX`
- `PDB:1FFT`
- `PDB:7CUW`
- `PDB:7CUQ`
- `PDB:7CUB`
- `PDB:6WTI`
- `PDB:8F6C`
- `PDB:8F68`
- `PDB:7XMD`
- `QSPROTEOME:QS00101628`

## Notes

1*protein.P0ABJ6|1*protein.P0ABJ1|1*protein.P0ABI8|1*protein.P0ABJ3
