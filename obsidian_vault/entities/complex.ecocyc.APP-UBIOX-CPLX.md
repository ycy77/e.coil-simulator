---
entity_id: "complex.ecocyc.APP-UBIOX-CPLX"
entity_type: "complex"
name: "cytochrome bd-II ubiquinol:oxygen oxidoreductase"
source_database: "EcoCyc"
source_id: "APP-UBIOX-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "CbdAB"
  - "AppCB"
  - "CyxAB"
---

# cytochrome bd-II ubiquinol:oxygen oxidoreductase

`complex.ecocyc.APP-UBIOX-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:APP-UBIOX-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P26459|protein.P26459]], [[protein.P26458|protein.P26458]], [[protein.P24244|protein.P24244]]

## Enriched Summary

The E. coli K-12 genome encodes 3 quinol:oxygen oxidoreductases - CYT-O-UBIOX-CPLX cytochrome bo (cyoABCD) , CYT-D-UBIOX-CPLX cytochrome bd-I (cydABX-cydH) and cytochrome bd-II (appCBX). The three enzymes function as the major terminal oxidases in the aerobic respiratory chain of E. coli. Cytochrome bo is expressed when oxygen levels are high while cytochrome bd-I is expressed under oxygen limited conditions and both enzymes contribute to the generation of a proton motive force (PMF). The energetics of cytochrome bd-II are less clear; initial reports suggested that it did not contribute to PMF , while later work indicates that it generates PMF with an H+/e- of 0.94 . Cytochrome bd-II has quinol oxidase activity in vitro; oxidation of the artifical substrate N,N,N',N'-tetramethyl-p-phenylenediamine dihydrochloride (TMPD) is inhibited by cyanide . Cytochrome bd-II, partially purified from the membranes of an engineered E. coli strain, consists of two subunits, AppC and AppB, which are highly similar to the to the CydA and CydB subunits respectively, of cytochrome bd-I . Both subunits are predicted to be integral inner membrane proteins and absorption spectra of the complex suggests the presence of heme d, heme b595, and heme b (559 nm)...

## Biological Role

Catalyzes RXN0-5266 (reaction.ecocyc.RXN0-5266). Bound by Heme (molecule.C00032), heme d (molecule.ecocyc.HEME_D).

## Annotation

The E. coli K-12 genome encodes 3 quinol:oxygen oxidoreductases - CYT-O-UBIOX-CPLX cytochrome bo (cyoABCD) , CYT-D-UBIOX-CPLX cytochrome bd-I (cydABX-cydH) and cytochrome bd-II (appCBX). The three enzymes function as the major terminal oxidases in the aerobic respiratory chain of E. coli. Cytochrome bo is expressed when oxygen levels are high while cytochrome bd-I is expressed under oxygen limited conditions and both enzymes contribute to the generation of a proton motive force (PMF). The energetics of cytochrome bd-II are less clear; initial reports suggested that it did not contribute to PMF , while later work indicates that it generates PMF with an H+/e- of 0.94 . Cytochrome bd-II has quinol oxidase activity in vitro; oxidation of the artifical substrate N,N,N',N'-tetramethyl-p-phenylenediamine dihydrochloride (TMPD) is inhibited by cyanide . Cytochrome bd-II, partially purified from the membranes of an engineered E. coli strain, consists of two subunits, AppC and AppB, which are highly similar to the to the CydA and CydB subunits respectively, of cytochrome bd-I . Both subunits are predicted to be integral inner membrane proteins and absorption spectra of the complex suggests the presence of heme d, heme b595, and heme b (559 nm) . A later cryo-EM structure of the complex with inhibitor (aurachin D) bound shows a dimer of AppBCX hetero-trimers with the small, single helix AppX subunit forming the major contact between the two heterotrimers . AppC contains all three heme cofactors and the quinol-binding loop (Q loop); heme b558 is the primary electron acceptor from quinol and heme d is the active site . Expression of cytochrome bd-II is induced by anaerobiosis, by phosphate starvation, and upon entry into stationary phase . Cytochrome bd-II may function at very low o

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5266|reaction.ecocyc.RXN0-5266]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.C00032|molecule.C00032]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.HEME_D|molecule.ecocyc.HEME_D]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P24244|protein.P24244]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P26458|protein.P26458]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P26459|protein.P26459]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:APP-UBIOX-CPLX`
- `PDB:7OY2`
- `PDB:7OSE`
- `PDB:7OSE`
- `PDB:7OY2`
- `QSPROTEOME:QS00196927`

## Notes

1*protein.P26459|1*protein.P26458|1*protein.P24244
