---
entity_id: "complex.ecocyc.BETAGALACTOSID-CPLX"
entity_type: "complex"
name: "β-galactosidase"
source_database: "EcoCyc"
source_id: "BETAGALACTOSID-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "&beta"
  - "-D-galactoside galactohydrolase"
  - "-D-galactosidase"
  - "lactase"
---

# β-galactosidase

`complex.ecocyc.BETAGALACTOSID-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:BETAGALACTOSID-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P00722|protein.P00722]]

## Enriched Summary

β-galactosidase is a bifunctional enzyme that hydrolyses lactose to galactose plus glucose and converts lactose to allolactose. The enzyme requires Mg2+ or Mn2+ for full activity plus a monovalent cation, usually Na+ or K+ . Purification of β-galactosidase was achieved during the middle of the 20th century from E. coli strain ML 308 and from strain K-12 . It was subsequently used as a model system to analyse how the response to a change in environment was regulated at the cellular level, specifically addressing questions of enzyme 'adaption' or enzyme 'induction' as it was then called (reviewed by ). These studies resulted in the elucidation of a pathway of negative control of β-galactosidase synthesis and led to the description of the operon model for gene regulation . lacZ forms an operon with LACY-MONOMER "lacY" (encoding lactose permease) and EG10524 lacA (a transacetylase). Expression of the lac operon is repressed by EG10525 "LacI" which binds to the lac operator . In the presence of allolactose - the physiological inducer - LacI binding to the operator is reduced leading to expression of the lac operon and production of the proteins necessary for lactose utilisation (reviewed by ). β-galactosidase is a large tetrameric molecule made up of 4 identical subunits. The tetramer has 4 active sites but it takes two monomers to complete an active site...

## Biological Role

Catalyzes BETAGALACTOSID-RXN (reaction.ecocyc.BETAGALACTOSID-RXN), RXN-17726 (reaction.ecocyc.RXN-17726), RXN-24169 (reaction.ecocyc.RXN-24169), RXN-25312 (reaction.ecocyc.RXN-25312), RXN0-5363 (reaction.ecocyc.RXN0-5363), RXN0-7219 (reaction.ecocyc.RXN0-7219). Bound by Magnesium cation (molecule.C00305).

## Annotation

β-galactosidase is a bifunctional enzyme that hydrolyses lactose to galactose plus glucose and converts lactose to allolactose. The enzyme requires Mg2+ or Mn2+ for full activity plus a monovalent cation, usually Na+ or K+ . Purification of β-galactosidase was achieved during the middle of the 20th century from E. coli strain ML 308 and from strain K-12 . It was subsequently used as a model system to analyse how the response to a change in environment was regulated at the cellular level, specifically addressing questions of enzyme 'adaption' or enzyme 'induction' as it was then called (reviewed by ). These studies resulted in the elucidation of a pathway of negative control of β-galactosidase synthesis and led to the description of the operon model for gene regulation . lacZ forms an operon with LACY-MONOMER "lacY" (encoding lactose permease) and EG10524 lacA (a transacetylase). Expression of the lac operon is repressed by EG10525 "LacI" which binds to the lac operator . In the presence of allolactose - the physiological inducer - LacI binding to the operator is reduced leading to expression of the lac operon and production of the proteins necessary for lactose utilisation (reviewed by ). β-galactosidase is a large tetrameric molecule made up of 4 identical subunits. The tetramer has 4 active sites but it takes two monomers to complete an active site. Each monomer contains 5 domains including domain 3 which has an α/β barrel structure that interacts with the loop structure from domain 2 of a separate monomer to form much of the active site (reviewed by ). Deletion of residues from the amino terminus results in inactive dimers. Supplying peptides that include the missing residues restores the tetrameric structure and catalytic activity. This process is known as α-complem

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.BETAGALACTOSID-RXN|reaction.ecocyc.BETAGALACTOSID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17726|reaction.ecocyc.RXN-17726]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24169|reaction.ecocyc.RXN-24169]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-25312|reaction.ecocyc.RXN-25312]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5363|reaction.ecocyc.RXN0-5363]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7219|reaction.ecocyc.RXN0-7219]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00722|protein.P00722]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:BETAGALACTOSID-CPLX`
- `QSPROTEOME:QS00182033`
- `PDB:5A1A`
- `PDB:4TTG`

## Notes

4*protein.P00722
