---
entity_id: "protein.Q47140"
entity_type: "protein"
name: "hcaF"
source_database: "UniProt"
source_id: "Q47140"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hcaF digB hcaA2 hcaB phdC2 yfhV b2539 JW2523"
---

# hcaF

`protein.Q47140`

## Static

- Type: `protein`
- Source: `UniProt:Q47140`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of the multicomponent 3-phenylpropionate dioxygenase. Converts 3-phenylpropionic acid (PP) and cinnamic acid (CI) into 3-phenylpropionate-dihydrodiol (PP-dihydrodiol) and cinnamic acid-dihydrodiol (CI-dihydrodiol), respectively. {ECO:0000269|PubMed:9603882}. Based on sequence similarity, HcaF is thought to encode the small terminal subunit of the 3-phenylpropionate dioxygenase system . 3-phenylpropionate dioxygenase has not been biochemically characterized. E. coli is able to utilize certain aromatic acids as carbon and energy sources. A meta-cleavage pathway involving HcaF is used for the catabolism of 3-phenylpropionate . HcaF: "hydroxycinnamic acid"

## Biological Role

Component of putative 3-phenylpropionate/cinnamate dioxygenase (complex.ecocyc.HCAMULTI-CPLX).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

FUNCTION: Part of the multicomponent 3-phenylpropionate dioxygenase. Converts 3-phenylpropionic acid (PP) and cinnamic acid (CI) into 3-phenylpropionate-dihydrodiol (PP-dihydrodiol) and cinnamic acid-dihydrodiol (CI-dihydrodiol), respectively. {ECO:0000269|PubMed:9603882}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.HCAMULTI-CPLX|complex.ecocyc.HCAMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2539|gene.b2539]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47140`
- `KEGG:ecj:JW2523;eco:b2539;ecoc:C3026_14065;`
- `GeneID:75172652;75206232;946997;`
- `GO:GO:0008695; GO:0009334; GO:0019380`
- `EC:1.14.12.19`

## Notes

3-phenylpropionate/cinnamic acid dioxygenase subunit beta (EC 1.14.12.19)
