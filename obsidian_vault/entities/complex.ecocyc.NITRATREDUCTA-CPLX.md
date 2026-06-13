---
entity_id: "complex.ecocyc.NITRATREDUCTA-CPLX"
entity_type: "complex"
name: "nitrate reductase A"
source_database: "EcoCyc"
source_id: "NITRATREDUCTA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "NRA"
  - "quinol:nitrate oxidoreductase"
---

# nitrate reductase A

`complex.ecocyc.NITRATREDUCTA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:NITRATREDUCTA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P09152|protein.P09152]], [[protein.P11349|protein.P11349]], [[protein.P11350|protein.P11350]]

## Enriched Summary

narGHI encodes a membrane bound quinol-nitrate oxidoreductase, known as nitrate reductase A (NRA) in E. coli K-12. Nitrate reductase A is a respiratory enzyme that functions as a terminal reductase in electron transport pathways that operate during anaerobic growth in the presence of nitrate (see reviews by and ). The NRA heterotrimer consists of a molybdenum cofactor containing α subunit (NarG), an Fe-S cluster containing β subunit (NarH) and a heme containing γ subunit (NarI) . The redox active prosthetic groups of NRA form an electron transport chain which uses electrons from the membrane quinone pool for the reduction of cytoplasmic nitrate . Electrons derived from the oxidation of quinol are transferred through two hemes in NarI, one [3Fe-4S] (known as FS4) and three [4Fe-4S] clusters (FS3, FS2 and FS1) in NarH and one [4Fe-4S] (FS0) cluster in NarG to the Mos-bisPGD (molybdo-bis(pyranopterin guanine dinucleotide)) cofactor where nitrate is reduced to nitrite Nitrate reductase A can use both ubiquinol and menaquinol as electron donors . Kinetic studies suggest that menadiol and duroquinol (analogues of menaquinone and ubiquinone respectively) react at different sites on NRA . Nitrate reductase A has a H+/e- ratio of 1 . A crystal structure of the catalytic and electron transfer subunits (NarG and NarH) has been solved at 2...

## Biological Role

Catalyzes RXN-15119 (reaction.ecocyc.RXN-15119), RXN0-3501 (reaction.ecocyc.RXN0-3501), RXN0-7124 (reaction.ecocyc.RXN0-7124). Bound by Heme (molecule.C00032), a [3Fe-4S] iron-sulfur cluster (molecule.ecocyc.3FE-4S), bis(guanylyl molybdopterin) cofactor (molecule.ecocyc.CPD-15873), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

narGHI encodes a membrane bound quinol-nitrate oxidoreductase, known as nitrate reductase A (NRA) in E. coli K-12. Nitrate reductase A is a respiratory enzyme that functions as a terminal reductase in electron transport pathways that operate during anaerobic growth in the presence of nitrate (see reviews by and ). The NRA heterotrimer consists of a molybdenum cofactor containing α subunit (NarG), an Fe-S cluster containing β subunit (NarH) and a heme containing γ subunit (NarI) . The redox active prosthetic groups of NRA form an electron transport chain which uses electrons from the membrane quinone pool for the reduction of cytoplasmic nitrate . Electrons derived from the oxidation of quinol are transferred through two hemes in NarI, one [3Fe-4S] (known as FS4) and three [4Fe-4S] clusters (FS3, FS2 and FS1) in NarH and one [4Fe-4S] (FS0) cluster in NarG to the Mos-bisPGD (molybdo-bis(pyranopterin guanine dinucleotide)) cofactor where nitrate is reduced to nitrite Nitrate reductase A can use both ubiquinol and menaquinol as electron donors . Kinetic studies suggest that menadiol and duroquinol (analogues of menaquinone and ubiquinone respectively) react at different sites on NRA . Nitrate reductase A has a H+/e- ratio of 1 . A crystal structure of the catalytic and electron transfer subunits (NarG and NarH) has been solved at 2.0 Å resolution , and structures of the NarGHI complex both alone and in complex with the quinol binding site (Q-site) inhibitor pentachlorophenol have been solved at 1.9 and 2 Å resolution . NarGH is localised on the cytosolic side of the inner membrane and interacts with the membrane bound NarI subunit through a hydrophobic interface. Eight redox centres form an arc through the centre of the heterotrimer and are suggestive of a pathway for elect

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-15119|reaction.ecocyc.RXN-15119]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3501|reaction.ecocyc.RXN0-3501]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7124|reaction.ecocyc.RXN0-7124]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (7)

- `binds` <-- [[molecule.C00032|molecule.C00032]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.3FE-4S|molecule.ecocyc.3FE-4S]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-15873|molecule.ecocyc.CPD-15873]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P09152|protein.P09152]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P11349|protein.P11349]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P11350|protein.P11350]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:NITRATREDUCTA-CPLX`
- `PDB:1R27`
- `PDB:3IR7`
- `PDB:3IR6`
- `PDB:3IR5`
- `PDB:3EGW`
- `PDB:1Y5N`
- `PDB:1Y5L`
- `PDB:1Y5I`
- `QSPROTEOME:QS00093538`

## Notes

2*protein.P09152|2*protein.P11349|2*protein.P11350
