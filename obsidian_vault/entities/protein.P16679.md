---
entity_id: "protein.P16679"
entity_type: "protein"
name: "phnL"
source_database: "UniProt"
source_id: "P16679"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phnL b4096 JW4057"
---

# phnL

`protein.P16679`

## Static

- Type: `protein`
- Source: `UniProt:P16679`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Together with PhnG, PhnH and PhnI is required for the transfer of the ribose triphosphate moiety from ATP to methyl phosphonate. {ECO:0000269|PubMed:22089136}.

## Biological Role

Component of carbon-phosphorus lyase ATP-binding protein PhnL (complex.ecocyc.CPLX0-10308), carbon-phosphorus lyase system (complex.ecocyc.CPLX0-7958).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Together with PhnG, PhnH and PhnI is required for the transfer of the ribose triphosphate moiety from ATP to methyl phosphonate. {ECO:0000269|PubMed:22089136}.

## Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10308|complex.ecocyc.CPLX0-10308]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7958|complex.ecocyc.CPLX0-7958]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4096|gene.b4096]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16679`
- `KEGG:ecj:JW4057;eco:b4096;ecoc:C3026_22140;`
- `GeneID:948612;`
- `GO:GO:0005524; GO:0015716; GO:0016887; GO:0019634; GO:0019700; GO:0061693; GO:0061694; GO:1904176`
- `EC:2.7.8.37`

## Notes

Alpha-D-ribose 1-methylphosphonate 5-triphosphate synthase subunit PhnL (RPnTP synthase subunit PhnL) (EC 2.7.8.37)
