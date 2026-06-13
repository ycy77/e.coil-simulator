---
entity_id: "complex.ecocyc.CYT-D-UBIOX-CPLX"
entity_type: "complex"
name: "cytochrome bd-I ubiquinol:oxygen oxidoreductase"
source_database: "EcoCyc"
source_id: "CYT-D-UBIOX-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ubiquinol oxidase (electrogenic, non H<sup>+</sup> transporting)"
  - "cytochrome <i>d</i> complex"
  - "cytochrome <i>bd</i> complex"
  - "cytochrome <i>d</i> ubiquinol oxidase complex"
  - "cytochrome <i>b558-d</i> complex"
  - "ubiquinol:oxygen oxidoreductase"
---

# cytochrome bd-I ubiquinol:oxygen oxidoreductase

`complex.ecocyc.CYT-D-UBIOX-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CYT-D-UBIOX-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ABJ9|protein.P0ABJ9]], [[protein.P0ABK2|protein.P0ABK2]], [[protein.P56100|protein.P56100]], [[protein.A5A618|protein.A5A618]]

## Enriched Summary

The E. coli K-12 genome encodes 3 quinol:oxygen oxidoreductases - CYT-O-UBIOX-CPLX cytochrome bo (cyoABCD), cytochrome bd-I (cydABX-cydH) and APP-UBIOX-CPLX cytochrome bd-II (appCBX). The three enzymes function as the major terminal oxidases in the aerobic respiratory chain of E. coli. Cytochrome bo is expressed when oxygen levels are high while cytochrome bd-I is expressed under oxygen limited conditions. Both enymes contribute to the generation of a proton motive force (PMF), cytochrome bo functions as a proton pump whilst cytochrome bd-I does not. Cytochrome bd-I catalyses ubiquinol oxidation with a H+/e- of 1 . The energetics of cytochrome bd-II are less clear; initial reports suggested that it did not contribute to PMF while later work indicates that it generates PMF with an H+/e- of 0.94 . Cytochrome bd-I catalyses the two electron oxidation of ubiquinol and the four electron reduction of oxygen to water. Oxidation of ubiquinol releases two protons into the periplasmic space and two electrons are transferred through the heme cofactors to the oxygen reducing site. Four protons are taken up from the cytoplasm for oxygen reduction (see review by and references within). The enzyme is a hetero-tetramer consisting of the CydAB core dimer plus two accessory single transmembrane subunits, CydX and CydH...

## Biological Role

Catalyzes RXN-19777 (reaction.ecocyc.RXN-19777), RXN-19778 (reaction.ecocyc.RXN-19778), RXN0-5266 (reaction.ecocyc.RXN0-5266). Bound by Heme (molecule.C00032), heme d (molecule.ecocyc.HEME_D).

## Annotation

The E. coli K-12 genome encodes 3 quinol:oxygen oxidoreductases - CYT-O-UBIOX-CPLX cytochrome bo (cyoABCD), cytochrome bd-I (cydABX-cydH) and APP-UBIOX-CPLX cytochrome bd-II (appCBX). The three enzymes function as the major terminal oxidases in the aerobic respiratory chain of E. coli. Cytochrome bo is expressed when oxygen levels are high while cytochrome bd-I is expressed under oxygen limited conditions. Both enymes contribute to the generation of a proton motive force (PMF), cytochrome bo functions as a proton pump whilst cytochrome bd-I does not. Cytochrome bd-I catalyses ubiquinol oxidation with a H+/e- of 1 . The energetics of cytochrome bd-II are less clear; initial reports suggested that it did not contribute to PMF while later work indicates that it generates PMF with an H+/e- of 0.94 . Cytochrome bd-I catalyses the two electron oxidation of ubiquinol and the four electron reduction of oxygen to water. Oxidation of ubiquinol releases two protons into the periplasmic space and two electrons are transferred through the heme cofactors to the oxygen reducing site. Four protons are taken up from the cytoplasm for oxygen reduction (see review by and references within). The enzyme is a hetero-tetramer consisting of the CydAB core dimer plus two accessory single transmembrane subunits, CydX and CydH . Cytochrome bd-I contains 3 bound hemes: heme b558, heme b595 and heme d, present in a 1:1:1 ratio . Subunit I (CydA) contains all three heme cofactors and the periplasmically exposed quinol binding loop (Q loop); heme b558 acts as the primary electron acceptor and electrons are transferred via heme b595 to heme d where oxygen is reduced to water (see also ). Purified cytochrome bd-I has quinol peroxidase activity which may serve a detoxifying function in vivo; purified cy

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-19777|reaction.ecocyc.RXN-19777]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-19778|reaction.ecocyc.RXN-19778]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5266|reaction.ecocyc.RXN0-5266]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (6)

- `binds` <-- [[molecule.C00032|molecule.C00032]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.HEME_D|molecule.ecocyc.HEME_D]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.A5A618|protein.A5A618]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABJ9|protein.P0ABJ9]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABK2|protein.P0ABK2]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P56100|protein.P56100]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CYT-D-UBIOX-CPLX`
- `PDB:6RX4`
- `PDB:6RKO`
- `PDB:6RX4`
- `PDB:6RKO`
- `QSPROTEOME:QS00196491`

## Notes

1*protein.P0ABJ9|1*protein.P0ABK2|1*protein.P56100|1*protein.A5A618
