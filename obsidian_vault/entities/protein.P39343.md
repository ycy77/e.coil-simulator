---
entity_id: "protein.P39343"
entity_type: "protein"
name: "idnR"
source_database: "UniProt"
source_id: "P39343"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "idnR yjgS b4264 JW4221"
---

# idnR

`protein.P39343`

## Static

- Type: `protein`
- Source: `UniProt:P39343`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Idn operon regulator. May repress gntKU and gntT genes when growing on L-idonate. {ECO:0000269|PubMed:9658018}.

## Biological Role

Component of IdnR-5-dehydro-D-gluconate DNA-binding transcriptional dual regulator (complex.ecocyc.MONOMER0-1301).

## Annotation

FUNCTION: Idn operon regulator. May repress gntKU and gntT genes when growing on L-idonate. {ECO:0000269|PubMed:9658018}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-1301|complex.ecocyc.MONOMER0-1301]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b4264|gene.b4264]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39343`
- `KEGG:ecj:JW4221;eco:b4264;ecoc:C3026_23000;`
- `GeneID:949058;`
- `GO:GO:0000976; GO:0003700; GO:0006355; GO:0019521`

## Notes

HTH-type transcriptional regulator IdnR (L-idonate regulatory protein)
