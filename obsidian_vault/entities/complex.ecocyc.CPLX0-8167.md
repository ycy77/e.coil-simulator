---
entity_id: "complex.ecocyc.CPLX0-8167"
entity_type: "complex"
name: "hydrogenase 1, oxygen tolerant hydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-8167"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# hydrogenase 1, oxygen tolerant hydrogenase

`complex.ecocyc.CPLX0-8167`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8167`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[complex.ecocyc.FORMHYDROGI-CPLX|complex.ecocyc.FORMHYDROGI-CPLX]]

## Enriched Summary

Hydrogenase I (encoded by the hyaABC genes in E. coli K-12) is an oxygen-tolerant, membrane bound Ni-Fe hydrogenase . The purified enzyme catalyses H2:benzyl viologen oxidoreduction; it also catalyses H2 evolution with methyl viologen as an electron donor . In a strain lacking the hydrogenase 2 enzyme, hydrogenase 1 catalyses nitrate-dependent H2 consumption and DMSO-dependent H2 consumption but is less active with methyl viologen, benzyl viologen and fumarate. This mutant strain also demonstrates H2 consumption in the presence of air (ie. it is active in the Knallgas reaction 2H2 + O2 → 2H2O); hydrogenase 1 donates electrons preferentially to acceptors with higher reduction potential and is active at higher oxygen concentrations than hydrogenase 2 . Purified hydrogenase 1 is a uni-directional, oxygen-tolerant H(2) oxidizer; hydrogenase 1 may function as an energy conserving, H(2) scavenger under conditions of slow growth and fluctuating oxygen levels . Hydrogenase 1 can directly catalyse the 4 electron reduction of oxygen to water using H(2) as donor; when hydrogenase 1 reacts exclusively with H(2) and oxygen, 86% of the water produced arises from this direct reaction |CITS [24715724]|...

## Biological Role

Catalyzes Knallgas reaction (reaction.ecocyc.RXN-16420), hydrogen:menaquinone oxidoreductase (reaction.ecocyc.RXN0-5256). Bound by Heme (molecule.C00032), a [3Fe-4S] iron-sulfur cluster (molecule.ecocyc.3FE-4S), a [4Fe-3S] iron-sulfur cluster (molecule.ecocyc.CPD-17649), NiFe(CO)(CN)2 cofactor (molecule.ecocyc.CPD-24862), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

Hydrogenase I (encoded by the hyaABC genes in E. coli K-12) is an oxygen-tolerant, membrane bound Ni-Fe hydrogenase . The purified enzyme catalyses H2:benzyl viologen oxidoreduction; it also catalyses H2 evolution with methyl viologen as an electron donor . In a strain lacking the hydrogenase 2 enzyme, hydrogenase 1 catalyses nitrate-dependent H2 consumption and DMSO-dependent H2 consumption but is less active with methyl viologen, benzyl viologen and fumarate. This mutant strain also demonstrates H2 consumption in the presence of air (ie. it is active in the Knallgas reaction 2H2 + O2 → 2H2O); hydrogenase 1 donates electrons preferentially to acceptors with higher reduction potential and is active at higher oxygen concentrations than hydrogenase 2 . Purified hydrogenase 1 is a uni-directional, oxygen-tolerant H(2) oxidizer; hydrogenase 1 may function as an energy conserving, H(2) scavenger under conditions of slow growth and fluctuating oxygen levels . Hydrogenase 1 can directly catalyse the 4 electron reduction of oxygen to water using H(2) as donor; when hydrogenase 1 reacts exclusively with H(2) and oxygen, 86% of the water produced arises from this direct reaction |CITS [24715724]|. The oxidase activity of of hydrogenase 1 is low and serves to protect the active site from oxygen attack The membrane bound complex crystallises as a [HyaC(HyaAHyaB)2]2 complex and this is thought to be the physiologically relevant structure. Hydrogenase I is anchored to the membrane by both a HyaA C-terminal helix and an inner membrane b-type cytochome, HyaC; cytochrome b's main role may be anchoring the heterodimer (HyaAB) to the membrane. The small subunit (HyaA) contains a distal [4Fe-4S]cluster, a medial [3Fe-4S] cluster and a unique proximal [4Fe-3S] cluster; the large subunit (Hy

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-16420|reaction.ecocyc.RXN-16420]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5256|reaction.ecocyc.RXN0-5256]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (9)

- `binds` <-- [[molecule.C00032|molecule.C00032]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.3FE-4S|molecule.ecocyc.3FE-4S]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-17649|molecule.ecocyc.CPD-17649]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-24862|molecule.ecocyc.CPD-24862]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.FORMHYDROGI-CPLX|complex.ecocyc.FORMHYDROGI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` <-- [[protein.P0AAM1|protein.P0AAM1]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0ACD8|protein.P0ACD8]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4
- `is_component_of` <-- [[protein.P69739|protein.P69739]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8167`
- `PDB:3UQY`
- `PDB:3USC`
- `PDB:3USE`
- `PDB:4GD3`
- `PDB:4UE3`
- `PDB:5ADU`
- `PDB:5A4M`
- `PDB:5A4I`
- `QSPROTEOME:QS00195517`

## Notes

2*complex.ecocyc.FORMHYDROGI-CPLX
