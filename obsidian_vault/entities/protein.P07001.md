---
entity_id: "protein.P07001"
entity_type: "protein"
name: "pntA"
source_database: "UniProt"
source_id: "P07001"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pntA b1603 JW1595"
---

# pntA

`protein.P07001`

## Static

- Type: `protein`
- Source: `UniProt:P07001`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: The transhydrogenation between NADH and NADP is coupled to respiration and ATP hydrolysis and functions as a proton pump across the membrane. {ECO:0000269|PubMed:16083909}. pntA encodes the α subunit of membrane-bound proton-translocating pyridine nucleotide transhydrogenase. The α subunit is predicted to consist of a large N-terminal cytosolic region (domain I) which binds NAD(H) , followed by 4 transmembrane regions and a short C-terminal tail .

## Biological Role

Component of pyridine nucleotide transhydrogenase (complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: The transhydrogenation between NADH and NADP is coupled to respiration and ATP hydrolysis and functions as a proton pump across the membrane. {ECO:0000269|PubMed:16083909}.

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX|complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1603|gene.b1603]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07001`
- `KEGG:ecj:JW1595;eco:b1603;ecoc:C3026_09230;`
- `GeneID:946628;`
- `GO:GO:0005886; GO:0006740; GO:0008750; GO:0016491; GO:0046983; GO:0050661; GO:0120029`
- `EC:7.1.1.1`

## Notes

NAD(P) transhydrogenase subunit alpha (EC 7.1.1.1) (Nicotinamide nucleotide transhydrogenase subunit alpha) (Pyridine nucleotide transhydrogenase subunit alpha)
