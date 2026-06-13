---
entity_id: "complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX"
entity_type: "complex"
name: "ribonucleoside-diphosphate reductase 1"
source_database: "EcoCyc"
source_id: "RIBONUCLEOSIDE-DIP-REDUCTI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ribonucleotide reductase I"
  - "RDPR-I"
  - "RNR"
---

# ribonucleoside-diphosphate reductase 1

`complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:RIBONUCLEOSIDE-DIP-REDUCTI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[complex.ecocyc.B1-CPLX|complex.ecocyc.B1-CPLX]], [[complex.ecocyc.B2-CPLX|complex.ecocyc.B2-CPLX]]

## Enriched Summary

Ribonucleoside-diphosphate reductase (RDPR, or RNR) catalyzes the conversion of nucleotides to deoxynucleotides, an essential step in DNA synthesis. All four ribonucleoside diphosphates are reduced by RDPR. Glutaredoxin may substitute for thioredoxin in the reaction. The enzyme consists of two non-identical subunits, proteins R1 and R2 (also called α and β, or B1 and B2, respectively). Separately the subunits are catalytically inactive, but in the presence of Mg2+ they combine to form the enzymatically active complex. The substrate specificity is regulated by allosteric effectors (dATP, ATP, dTTP, dGTP) which bind to the R1 protein. The R1 protein also contains the redox-active thiols in each of its two active sites and five cysteine residues required for activity. The R2 subunit contains a unique cofactor, a binuclear iron center and organic free radical which arises from the oxidation of a single tyrosine residue of the subunit. The tyrosyl radical is essential for activity. A multienzyme complex is needed to activate the tyrosyl radical. The activating system is composed of three proteins: FMN reductase, superoxide dismutase and protein fraction named fraction b whose function is poorly defined Numerous crystal structures of wild-type, mutant, or derivatized NrdA and NrdB have been determined...

## Biological Role

Catalyzes ADP reductase (reaction.ecocyc.ADPREDUCT-RXN), CDPREDUCT-RXN (reaction.ecocyc.CDPREDUCT-RXN), GDPREDUCT-RXN (reaction.ecocyc.GDPREDUCT-RXN), RIBONUCLEOSIDE-DIP-REDUCTI-RXN (reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-RXN), UDPREDUCT-RXN (reaction.ecocyc.UDPREDUCT-RXN). Bound by Magnesium cation (molecule.C00305), Fe2+ (molecule.C14818).

## Annotation

Ribonucleoside-diphosphate reductase (RDPR, or RNR) catalyzes the conversion of nucleotides to deoxynucleotides, an essential step in DNA synthesis. All four ribonucleoside diphosphates are reduced by RDPR. Glutaredoxin may substitute for thioredoxin in the reaction. The enzyme consists of two non-identical subunits, proteins R1 and R2 (also called α and β, or B1 and B2, respectively). Separately the subunits are catalytically inactive, but in the presence of Mg2+ they combine to form the enzymatically active complex. The substrate specificity is regulated by allosteric effectors (dATP, ATP, dTTP, dGTP) which bind to the R1 protein. The R1 protein also contains the redox-active thiols in each of its two active sites and five cysteine residues required for activity. The R2 subunit contains a unique cofactor, a binuclear iron center and organic free radical which arises from the oxidation of a single tyrosine residue of the subunit. The tyrosyl radical is essential for activity. A multienzyme complex is needed to activate the tyrosyl radical. The activating system is composed of three proteins: FMN reductase, superoxide dismutase and protein fraction named fraction b whose function is poorly defined Numerous crystal structures of wild-type, mutant, or derivatized NrdA and NrdB have been determined. These structures, along with accompanying physicochemical and biochemical studies, have aided in elucidating details of the reaction mechanism . A cryo-EM structure of RNR trapped in the active state has been solved. Contrary to the previously proposed docking model and consistent with prior evidence for half-sites reactivity, the α2 and β2 subunits form an asymmetric complex, where one α subunit interacts with β2. While the β2-interacting α subunit is in the pre-turnover state

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.ADPREDUCT-RXN|reaction.ecocyc.ADPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CDPREDUCT-RXN|reaction.ecocyc.CDPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.GDPREDUCT-RXN|reaction.ecocyc.GDPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-RXN|reaction.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.UDPREDUCT-RXN|reaction.ecocyc.UDPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (6)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.B1-CPLX|complex.ecocyc.B1-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[complex.ecocyc.B2-CPLX|complex.ecocyc.B2-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P00452|protein.P00452]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P69924|protein.P69924]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:RIBONUCLEOSIDE-DIP-REDUCTI-CPLX`
- `PDB:1R1R`
- `PDB:2R1R`
- `PDB:3R1R`
- `PDB:4R1R`
- `PDB:5R1R`
- `PDB:6R1R`
- `PDB:7R1R`
- `PDB:2X0X`
- `QSPROTEOME:QS00174137`

## Notes

1*complex.ecocyc.B1-CPLX|1*complex.ecocyc.B2-CPLX
