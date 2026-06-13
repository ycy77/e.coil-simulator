---
entity_id: "complex.ecocyc.CPLX0-8280"
entity_type: "complex"
name: "pyrimidine-specific ribonucleoside hydrolase RihA"
source_database: "EcoCyc"
source_id: "CPLX0-8280"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# pyrimidine-specific ribonucleoside hydrolase RihA

`complex.ecocyc.CPLX0-8280`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8280`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P41409|protein.P41409]]

## Enriched Summary

rihA encodes a ribonucleoside hydrolase that preferentially utilizes cytidine and uridine . The kcat/KM for uridine is approximately 10 times higher than for cytidine, largely due to a lower KM value for uridine . E. coli contains two other nucleoside hydrolases with differing specificities, encoded by rihB and rihC . A crystal structure of RihA bound to the reaction product D-ribose has been solved at 1.8 Å resolution , and a structure of RihA bound to the competitive inhibitor 3,4-diaminophenyl-iminoribitol was solved at 2.1 Å resolution . A triple mutant lacking rihA, rihB and rihC grows normally. An rihA null mutant in a pyr cdd mutant background can not use cytidine as a source of pyrimidine. The rihA and rihC genes are subject to catabolite repression . rihA encodes a ribonucleoside hydrolase that preferentially utilizes cytidine and uridine . The kcat/KM for uridine is approximately 10 times higher than for cytidine, largely due to a lower KM value for uridine . E. coli contains two other nucleoside hydrolases with differing specificities, encoded by rihB and rihC . A crystal structure of RihA bound to the reaction product D-ribose has been solved at 1.8 Å resolution , and a structure of RihA bound to the competitive inhibitor 3,4-diaminophenyl-iminoribitol was solved at 2.1 Å resolution . A triple mutant lacking rihA, rihB and rihC grows normally...

## Biological Role

Catalyzes RXN0-361 (reaction.ecocyc.RXN0-361), URIDINE-NUCLEOSIDASE-RXN (reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN).

## Annotation

rihA encodes a ribonucleoside hydrolase that preferentially utilizes cytidine and uridine . The kcat/KM for uridine is approximately 10 times higher than for cytidine, largely due to a lower KM value for uridine . E. coli contains two other nucleoside hydrolases with differing specificities, encoded by rihB and rihC . A crystal structure of RihA bound to the reaction product D-ribose has been solved at 1.8 Å resolution , and a structure of RihA bound to the competitive inhibitor 3,4-diaminophenyl-iminoribitol was solved at 2.1 Å resolution . A triple mutant lacking rihA, rihB and rihC grows normally. An rihA null mutant in a pyr cdd mutant background can not use cytidine as a source of pyrimidine. The rihA and rihC genes are subject to catabolite repression .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-361|reaction.ecocyc.RXN0-361]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN|reaction.ecocyc.URIDINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P41409|protein.P41409]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8280`
- `QSPROTEOME:QS00190105`

## Notes

4*protein.P41409
