---
entity_id: "protein.P0ABW0"
entity_type: "protein"
name: "hcaC"
source_database: "UniProt"
source_id: "P0ABW0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hcaC hcaA3 phdB yfhW b2540 JW2524"
---

# hcaC

`protein.P0ABW0`

## Static

- Type: `protein`
- Source: `UniProt:P0ABW0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of the multicomponent 3-phenylpropionate dioxygenase, that converts 3-phenylpropionic acid (PP) and cinnamic acid (CI) into 3-phenylpropionate-dihydrodiol (PP-dihydrodiol) and cinnamic acid-dihydrodiol (CI-dihydrodiol), respectively. This protein seems to be a 2Fe-2S ferredoxin. Based on sequence similarity, HcaC is thought to encode the ferredoxin component of the 3-phenylpropionate dioxygenase system . Partially purified HcaC protein was shown to contain a [2Fe-2S] iron-sulfur cluster that can be reduced by dithionite, but not ascorbate, identifying it as a low-potential Rieske iron-sulfur cluster protein . 3-phenylpropionate dioxygenase has not been biochemically characterized. E. coli is able to utilize certain aromatic acids as carbon and energy sources. A meta-cleavage pathway involving HcaC is used for the catabolism of 3-phenylpropionate . HcaC: "hydroxycinnamic acid"

## Biological Role

Component of putative 3-phenylpropionate/cinnamate dioxygenase (complex.ecocyc.HCAMULTI-CPLX).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

FUNCTION: Part of the multicomponent 3-phenylpropionate dioxygenase, that converts 3-phenylpropionic acid (PP) and cinnamic acid (CI) into 3-phenylpropionate-dihydrodiol (PP-dihydrodiol) and cinnamic acid-dihydrodiol (CI-dihydrodiol), respectively. This protein seems to be a 2Fe-2S ferredoxin.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.HCAMULTI-CPLX|complex.ecocyc.HCAMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2540|gene.b2540]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABW0`
- `KEGG:ecj:JW2524;eco:b2540;ecoc:C3026_14070;`
- `GeneID:93774596;947015;`
- `GO:GO:0008695; GO:0009334; GO:0019380; GO:0046872; GO:0051536; GO:0051537`

## Notes

3-phenylpropionate/cinnamic acid dioxygenase ferredoxin subunit
