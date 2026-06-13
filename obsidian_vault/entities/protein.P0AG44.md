---
entity_id: "protein.P0AG44"
entity_type: "protein"
name: "rplQ"
source_database: "UniProt"
source_id: "P0AG44"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplQ b3294 JW3256"
---

# rplQ

`protein.P0AG44`

## Static

- Type: `protein`
- Source: `UniProt:P0AG44`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Requires L15 for assembly into the 50S subunit. {ECO:0000269|PubMed:3298242}. The L17 protein is a component of the 50S subunit of the ribosome. L17 interacts directly with tRNA and can be crosslinked to 23S rRNA . L17 can also be crosslinked to the spiramycin derivative dihydrospiramycin and may thus be located near the peptidyl transferase center .

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: Requires L15 for assembly into the 50S subunit. {ECO:0000269|PubMed:3298242}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b3294|gene.b3294]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG44`
- `KEGG:ecj:JW3256;eco:b3294;ecoc:C3026_17910;`
- `GeneID:947784;99707778;99810659;`
- `GO:GO:0000027; GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0022625`

## Notes

Large ribosomal subunit protein bL17 (50S ribosomal protein L17)
