---
entity_id: "protein.P38038"
entity_type: "protein"
name: "cysJ"
source_database: "UniProt"
source_id: "P38038"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysJ b2764 JW2734"
---

# cysJ

`protein.P38038`

## Static

- Type: `protein`
- Source: `UniProt:P38038`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Component of the sulfite reductase complex that catalyzes the 6-electron reduction of sulfite to sulfide. This is one of several activities required for the biosynthesis of L-cysteine from sulfate. The flavoprotein component catalyzes the electron flow from NADPH -> FAD -> FMN to the hemoprotein component. {ECO:0000255|HAMAP-Rule:MF_01541}.; FUNCTION: In addition to its role in the sulfite reductase complex, it functions as a specific partner of the YcbX molybdoenzyme in the detoxification of N-hydroxylated base analogs (PubMed:20118259). CysJ mediates the N-reductive reaction through its NADPH:flavin oxidoreductase activity (PubMed:20118259). It may provide reducing equivalents to its partner YcbX, which ultimately performs the reduction of 6-N-hydroxylaminopurine (HAP) to non-toxic adenine (PubMed:20118259). The role of CysJ in base analog detoxification is independent of CysI and sulfite reductase (PubMed:20118259). {ECO:0000269|PubMed:20118259}.

## Biological Role

Component of sulfite reductase, flavoprotein subunit complex (complex.ecocyc.CPLX0-7841), assimilatory sulfite reductase (NADPH) (complex.ecocyc.SULFITE-REDUCT-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Annotation

FUNCTION: Component of the sulfite reductase complex that catalyzes the 6-electron reduction of sulfite to sulfide. This is one of several activities required for the biosynthesis of L-cysteine from sulfate. The flavoprotein component catalyzes the electron flow from NADPH -> FAD -> FMN to the hemoprotein component. {ECO:0000255|HAMAP-Rule:MF_01541}.; FUNCTION: In addition to its role in the sulfite reductase complex, it functions as a specific partner of the YcbX molybdoenzyme in the detoxification of N-hydroxylated base analogs (PubMed:20118259). CysJ mediates the N-reductive reaction through its NADPH:flavin oxidoreductase activity (PubMed:20118259). It may provide reducing equivalents to its partner YcbX, which ultimately performs the reduction of 6-N-hydroxylaminopurine (HAP) to non-toxic adenine (PubMed:20118259). The role of CysJ in base analog detoxification is independent of CysI and sulfite reductase (PubMed:20118259). {ECO:0000269|PubMed:20118259}.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7841|complex.ecocyc.CPLX0-7841]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8
- `is_component_of` --> [[complex.ecocyc.SULFITE-REDUCT-CPLX|complex.ecocyc.SULFITE-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b2764|gene.b2764]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P38038`
- `KEGG:ecj:JW2734;eco:b2764;ecoc:C3026_15190;`
- `GeneID:947239;`
- `GO:GO:0000103; GO:0004783; GO:0005829; GO:0009337; GO:0010181; GO:0016491; GO:0019344; GO:0042602; GO:0050660; GO:0070401; GO:0070814`
- `EC:1.8.1.2`

## Notes

Sulfite reductase [NADPH] flavoprotein alpha-component (SiR-FP) (EC 1.8.1.2)
