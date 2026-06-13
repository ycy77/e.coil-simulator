---
entity_id: "protein.P02413"
entity_type: "protein"
name: "rplO"
source_database: "UniProt"
source_id: "P02413"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplO b3301 JW3263"
---

# rplO

`protein.P02413`

## Static

- Type: `protein`
- Source: `UniProt:P02413`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein binds the 5S rRNA. It is required for the late stages of subunit assembly, and is essential for 5S rRNA assembly onto the ribosome. {ECO:0000269|PubMed:3298242}. The L15 protein is a component of the 50S subunit of the ribosome. L15 is a late assembly protein that appears to be required for 5S rRNA incorporation . L15 interacts with domain II of 23S rRNA in a partially assembled ribosomal particle . L15 appears to be dispensible for protein synthesis and cell growth , and ribosomes lacking L15 are translationally active . L15 is a component of the binding site for erythromycin on the ribosome . L15 has RNA chaperone-like activity in an in vitro trans splicing assay .

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: This protein binds the 5S rRNA. It is required for the late stages of subunit assembly, and is essential for 5S rRNA assembly onto the ribosome. {ECO:0000269|PubMed:3298242}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b3301|gene.b3301]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02413`
- `KEGG:ecj:JW3263;eco:b3301;ecoc:C3026_17945;`
- `GeneID:947798;`
- `GO:GO:0002181; GO:0003735; GO:0005737; GO:0019843; GO:0022625`

## Notes

Large ribosomal subunit protein uL15 (50S ribosomal protein L15)
