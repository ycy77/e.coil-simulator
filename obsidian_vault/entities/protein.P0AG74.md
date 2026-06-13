---
entity_id: "protein.P0AG74"
entity_type: "protein"
name: "rusA"
source_database: "UniProt"
source_id: "P0AG74"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rusA rus ybcP b0550 JW0538"
---

# rusA

`protein.P0AG74`

## Static

- Type: `protein`
- Source: `UniProt:P0AG74`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Endonuclease that resolves Holliday junction intermediates made during homologous genetic recombination and DNA repair. Exhibits sequence and structure-selective cleavage of four-way DNA junctions, where it introduces symmetrical nicks in two strands of the same polarity at the 5' side of CC dinucleotides. Corrects the defects in genetic recombination and DNA repair associated with inactivation of ruvAB or ruvC.

## Biological Role

Component of DLP12 prophage; crossover junction endodeoxyribonuclease RusA (complex.ecocyc.CPLX0-8237).

## Annotation

FUNCTION: Endonuclease that resolves Holliday junction intermediates made during homologous genetic recombination and DNA repair. Exhibits sequence and structure-selective cleavage of four-way DNA junctions, where it introduces symmetrical nicks in two strands of the same polarity at the 5' side of CC dinucleotides. Corrects the defects in genetic recombination and DNA repair associated with inactivation of ruvAB or ruvC.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8237|complex.ecocyc.CPLX0-8237]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0550|gene.b0550]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG74`
- `KEGG:ecj:JW0538;eco:b0550;ecoc:C3026_02710;`
- `GeneID:945174;`
- `GO:GO:0000287; GO:0000400; GO:0006281; GO:0006310; GO:0008821; GO:0042803`
- `EC:3.1.21.10`

## Notes

Crossover junction endodeoxyribonuclease RusA (EC 3.1.21.10) (Holliday junction nuclease RusA) (Holliday junction resolvase)
