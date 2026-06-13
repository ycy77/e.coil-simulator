---
entity_id: "protein.P77650"
entity_type: "protein"
name: "hcaD"
source_database: "UniProt"
source_id: "P77650"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hcaD hcaA4 phdA yfhY b2542 JW2526"
---

# hcaD

`protein.P77650`

## Static

- Type: `protein`
- Source: `UniProt:P77650`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of the multicomponent 3-phenylpropionate dioxygenase, that converts 3-phenylpropionic acid (PP) and cinnamic acid (CI) into 3-phenylpropionate-dihydrodiol (PP-dihydrodiol) and cinnamic acid-dihydrodiol (CI-dihydrodiol), respectively. Based on sequence similarity, HcaD is thought to encode the ferredoxin reductase component of the 3-phenylpropionate dioxygenase system . 3-phenylpropionate dioxygenase has not been biochemically characterized. E. coli is able to utilize certain aromatic acids as carbon and energy sources. A meta-cleavage pathway involving HcaD is used for the catabolism of 3-phenylpropionate . HcaD: "hydroxycinnamic acid"

## Biological Role

Component of putative 3-phenylpropionate/cinnamate dioxygenase (complex.ecocyc.HCAMULTI-CPLX).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

FUNCTION: Part of the multicomponent 3-phenylpropionate dioxygenase, that converts 3-phenylpropionic acid (PP) and cinnamic acid (CI) into 3-phenylpropionate-dihydrodiol (PP-dihydrodiol) and cinnamic acid-dihydrodiol (CI-dihydrodiol), respectively.

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.HCAMULTI-CPLX|complex.ecocyc.HCAMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2542|gene.b2542]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77650`
- `KEGG:ecj:JW2526;eco:b2542;ecoc:C3026_14080;`
- `GeneID:945427;`
- `GO:GO:0008695; GO:0008860; GO:0009334; GO:0016651; GO:0019380`
- `EC:1.18.1.3`

## Notes

3-phenylpropionate/cinnamic acid dioxygenase ferredoxin--NAD(+) reductase component (EC 1.18.1.3)
