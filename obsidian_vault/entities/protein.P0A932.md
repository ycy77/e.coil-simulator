---
entity_id: "protein.P0A932"
entity_type: "protein"
name: "gfcE"
source_database: "UniProt"
source_id: "P0A932"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000250}; Multi-pass membrane protein {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gfcE yccZ b0983 JW0966"
---

# gfcE

`protein.P0A932`

## Static

- Type: `protein`
- Source: `UniProt:P0A932`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000250}; Multi-pass membrane protein {ECO:0000250}.

## Enriched Summary

FUNCTION: May be involved in polysaccharide transport. GfcE is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). The operon encoding YmcD, YmcC, YmcB, YmcA, YccZ, Etp, and Etk was characterized in the enteropathogenic E. coli strain O127:H6. There, all seven gene products are required for the production of the G4C capsule polysaccharide . This operon may not be expressed in E. coli K-12, because the promoter region that was mapped in E. coli O127:H6 is inactivated in E. coli K-12 by the insertion of an IS1 element 15 bp upstream of the YmcD translation start site .

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: May be involved in polysaccharide transport.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0983|gene.b0983]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A932`
- `KEGG:ecj:JW0966;eco:b0983;ecoc:C3026_05995;`
- `GeneID:93776429;945586;`
- `GO:GO:0006811; GO:0009279; GO:0015159; GO:0015288; GO:0046930`

## Notes

Putative polysaccharide export protein GfcE (Group 4 capsule protein E homolog)
