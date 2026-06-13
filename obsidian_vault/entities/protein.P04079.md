---
entity_id: "protein.P04079"
entity_type: "protein"
name: "guaA"
source_database: "UniProt"
source_id: "P04079"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "guaA b2507 JW2491"
---

# guaA

`protein.P04079`

## Static

- Type: `protein`
- Source: `UniProt:P04079`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of GMP from XMP.

## Biological Role

Catalyzes L-glutamine amidohydrolase (reaction.R00256). Component of GMP synthetase (complex.ecocyc.GMP-SYN-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the synthesis of GMP from XMP.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00256|reaction.R00256]] `KEGG` `database` - via EC:6.3.5.2
- `is_component_of` --> [[complex.ecocyc.GMP-SYN-CPLX|complex.ecocyc.GMP-SYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2507|gene.b2507]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04079`
- `KEGG:ecj:JW2491;eco:b2507;ecoc:C3026_13905;`
- `GeneID:947334;`
- `GO:GO:0003921; GO:0003922; GO:0005524; GO:0005829; GO:0006177; GO:0042802`
- `EC:6.3.5.2`

## Notes

GMP synthase [glutamine-hydrolyzing] (EC 6.3.5.2) (GMP synthetase) (GMPS) (Glutamine amidotransferase)
