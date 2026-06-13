---
entity_id: "protein.P0AB67"
entity_type: "protein"
name: "pntB"
source_database: "UniProt"
source_id: "P0AB67"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pntB b1602 JW1594"
---

# pntB

`protein.P0AB67`

## Static

- Type: `protein`
- Source: `UniProt:P0AB67`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: The transhydrogenation between NADH and NADP is coupled to respiration and ATP hydrolysis and functions as a proton pump across the membrane. pntB encodes the β subunit of membrane-bound proton-translocating pyridine nucleotide transhydrogenase. The β subunit contains an N-terminal domain with 6 - 8 transmembrane regions and a cytosolic C-terminal domain that binds NADP(H) . Early studies characterized the pnt-1 mutation (PntB G314E ) which causes loss of both energy-dependent and energy-independent pyridine nucleotide transhydrogenase activity .

## Biological Role

Component of pyridine nucleotide transhydrogenase (complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: The transhydrogenation between NADH and NADP is coupled to respiration and ATP hydrolysis and functions as a proton pump across the membrane.

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX|complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1602|gene.b1602]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB67`
- `KEGG:ecj:JW1594;eco:b1602;ecoc:C3026_09225;`
- `GeneID:93775750;946144;`
- `GO:GO:0005886; GO:0006740; GO:0008750; GO:0050661; GO:0120029`
- `EC:7.1.1.1`

## Notes

NAD(P) transhydrogenase subunit beta (EC 7.1.1.1) (Nicotinamide nucleotide transhydrogenase subunit beta) (Pyridine nucleotide transhydrogenase subunit beta)
