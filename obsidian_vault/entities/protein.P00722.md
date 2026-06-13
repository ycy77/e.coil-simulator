---
entity_id: "protein.P00722"
entity_type: "protein"
name: "lacZ"
source_database: "UniProt"
source_id: "P00722"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lacZ b0344 JW0335"
---

# lacZ

`protein.P00722`

## Static

- Type: `protein`
- Source: `UniProt:P00722`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Beta-galactosidase (Beta-gal) (EC 3.2.1.23) (Lactase)

## Biological Role

Catalyzes R07807 (reaction.R07807). Component of β-galactosidase (complex.ecocyc.BETAGALACTOSID-CPLX).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00511` Other glycan degradation (KEGG)
- `eco00600` Sphingolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

Beta-galactosidase (Beta-gal) (EC 3.2.1.23) (Lactase)

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00511` Other glycan degradation (KEGG)
- `eco00600` Sphingolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R07807|reaction.R07807]] `KEGG` `database` - via EC:3.2.1.23
- `is_component_of` --> [[complex.ecocyc.BETAGALACTOSID-CPLX|complex.ecocyc.BETAGALACTOSID-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0344|gene.b0344]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00722`
- `KEGG:ecj:JW0335;eco:b0344;`
- `GeneID:945006;`
- `GO:GO:0000287; GO:0004565; GO:0005990; GO:0009341; GO:0030246; GO:0031420; GO:0042802`
- `EC:3.2.1.23`

## Notes

Beta-galactosidase (Beta-gal) (EC 3.2.1.23) (Lactase)
