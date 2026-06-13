---
entity_id: "complex.ecocyc.CPLX0-7904"
entity_type: "complex"
name: "pyrimidine-specific ribonucleoside hydrolase RihB"
source_database: "EcoCyc"
source_id: "CPLX0-7904"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# pyrimidine-specific ribonucleoside hydrolase RihB

`complex.ecocyc.CPLX0-7904`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7904`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P33022|protein.P33022]]

## Enriched Summary

rihB encodes a ribonucleoside hydrolase that utilizes both cytidine and uridine . E. coli contains two other nucleoside hydrolases with differing specificities, encoded by rihA and rihC . A crystal structure of RihB has been solved at 1.7 Å resolution. Kinetic analysis of site-specific mutants supports involvement of His82 and His239 in substrate binding . A crystal structure of the RihB-inosine complex was solved, enabling investigation of the structural basis for the substrate specificity of RihB. The presence of a specific double mutation, T223Y/Q227Y, increases the catalytic efficiency of RihB towards purine nucleosides . Molecular dynamics simulations of protein-ligand interactions have been performed . A triple mutant lacking rihA, rihB and rihC grows normally . The rihB gene is hardly expressed unless an activating mutation is present . rihB encodes a ribonucleoside hydrolase that utilizes both cytidine and uridine . E. coli contains two other nucleoside hydrolases with differing specificities, encoded by rihA and rihC . A crystal structure of RihB has been solved at 1.7 Å resolution. Kinetic analysis of site-specific mutants supports involvement of His82 and His239 in substrate binding . A crystal structure of the RihB-inosine complex was solved, enabling investigation of the structural basis for the substrate specificity of RihB...

## Biological Role

Catalyzes RIBOSYLPYRIMIDINE-NUCLEOSIDASE-RXN (reaction.ecocyc.RIBOSYLPYRIMIDINE-NUCLEOSIDASE-RXN), RXN0-361 (reaction.ecocyc.RXN0-361), URIDINE-NUCLEOSIDASE-RXN (reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN). Bound by Ca2+ (molecule.ecocyc.CA_2).

## Annotation

rihB encodes a ribonucleoside hydrolase that utilizes both cytidine and uridine . E. coli contains two other nucleoside hydrolases with differing specificities, encoded by rihA and rihC . A crystal structure of RihB has been solved at 1.7 Å resolution. Kinetic analysis of site-specific mutants supports involvement of His82 and His239 in substrate binding . A crystal structure of the RihB-inosine complex was solved, enabling investigation of the structural basis for the substrate specificity of RihB. The presence of a specific double mutation, T223Y/Q227Y, increases the catalytic efficiency of RihB towards purine nucleosides . Molecular dynamics simulations of protein-ligand interactions have been performed . A triple mutant lacking rihA, rihB and rihC grows normally . The rihB gene is hardly expressed unless an activating mutation is present .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RIBOSYLPYRIMIDINE-NUCLEOSIDASE-RXN|reaction.ecocyc.RIBOSYLPYRIMIDINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-361|reaction.ecocyc.RXN0-361]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN|reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P33022|protein.P33022]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7904`
- `QSPROTEOME:QS00181839`

## Notes

4*protein.P33022
