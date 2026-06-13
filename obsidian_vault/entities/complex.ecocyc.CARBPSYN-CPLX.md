---
entity_id: "complex.ecocyc.CARBPSYN-CPLX"
entity_type: "complex"
name: "carbamoyl-phosphate synthetase, glutamine-hydrolyzing"
source_database: "EcoCyc"
source_id: "CARBPSYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# carbamoyl-phosphate synthetase, glutamine-hydrolyzing

`complex.ecocyc.CARBPSYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CARBPSYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P00968|protein.P00968]], [[protein.P0A6F1|protein.P0A6F1]]

## Enriched Summary

Carbamoyl phosphate synthetase catalyzes the biosynthesis of the precursor for the production of pyrimidine nucleotides and L-arginine. The enzymatic activity is regulated at multiple levels to obtain the needed supply of carbamoyl phosphate for the separate biosynthesis pathways . The functional enzyme entity is an α,β-heterodimer consisting of a small amidotransferase subunit complexed to a larger synthetase subunit. The small subunit, encoded by carA, hydrolyzes glutamine to glutamate and ammonia. The large subunit, encoded by carB, binds the two required molecules of MgATP and catalyzes the two required phosphorylation events . The reaction mechanism (ordered Ter-Uni-Uni-Ter ping-pong), kinetic parameters, and activation/inhibition of the enzyme were initially investigated with the enzyme isolated from E. coli B; later, the overexpressed E. coli K-12 enzyme was used, e.g. . In the presence of the allosteric activator ornithine, the α,β-heterodimer forms an (αβ)8 heterooctamer. The assembly of carbamoyl phosphate requires at least four separate chemical reactions: phosphorylation of bicarbonate to carboxyphosphate; hydrolysis of glutamine to glutamate and ammonia; a nucleophilic attack of ammonia on carboxyphosphate yielding carbamate; and finally the phosphorylation of carbamate forming carbamoyl phosphate...

## Biological Role

Catalyzes CARBPSYN-RXN (reaction.ecocyc.CARBPSYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Carbamoyl phosphate synthetase catalyzes the biosynthesis of the precursor for the production of pyrimidine nucleotides and L-arginine. The enzymatic activity is regulated at multiple levels to obtain the needed supply of carbamoyl phosphate for the separate biosynthesis pathways . The functional enzyme entity is an α,β-heterodimer consisting of a small amidotransferase subunit complexed to a larger synthetase subunit. The small subunit, encoded by carA, hydrolyzes glutamine to glutamate and ammonia. The large subunit, encoded by carB, binds the two required molecules of MgATP and catalyzes the two required phosphorylation events . The reaction mechanism (ordered Ter-Uni-Uni-Ter ping-pong), kinetic parameters, and activation/inhibition of the enzyme were initially investigated with the enzyme isolated from E. coli B; later, the overexpressed E. coli K-12 enzyme was used, e.g. . In the presence of the allosteric activator ornithine, the α,β-heterodimer forms an (αβ)8 heterooctamer. The assembly of carbamoyl phosphate requires at least four separate chemical reactions: phosphorylation of bicarbonate to carboxyphosphate; hydrolysis of glutamine to glutamate and ammonia; a nucleophilic attack of ammonia on carboxyphosphate yielding carbamate; and finally the phosphorylation of carbamate forming carbamoyl phosphate . The enzyme contains a total of three separate active sites that are connected by an intramolecular tunnel. The small subunit harbors one of these active sites. Two molecular tunnels connect the three active sites contained within the small and large subunits. The ammonia tunnel extends from the active site of the small subunit to the active site of the carboxy phosphate domain of the large subunit. The carbamate tunnel connects the two active sites within the la

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CARBPSYN-RXN|reaction.ecocyc.CARBPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00968|protein.P00968]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A6F1|protein.P0A6F1]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CARBPSYN-CPLX`
- `PDB:1A9X`
- `PDB:1BXR`
- `PDB:1JDB`
- `PDB:1KEE`
- `PDB:1M6V`
- `PDB:1T36`
- `PDB:1CS0`
- `PDB:1CE8`
- `QSPROTEOME:QS00196517`

## Notes

1*protein.P00968|1*protein.P0A6F1
