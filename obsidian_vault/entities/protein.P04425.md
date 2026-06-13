---
entity_id: "protein.P04425"
entity_type: "protein"
name: "gshB"
source_database: "UniProt"
source_id: "P04425"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gshB gsh-II b2947 JW2914"
---

# gshB

`protein.P04425`

## Static

- Type: `protein`
- Source: `UniProt:P04425`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Glutathione synthetase (EC 6.3.2.3) (GSH synthetase) (GSH-S) (GSHase) (Glutathione synthase)

## Biological Role

Catalyzes gamma-L-glutamyl-L-cysteine:glycine ligase (ADP-forming) (reaction.R00497). Component of glutathione synthetase (complex.ecocyc.GLUTATHIONE-SYN-CPLX).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

Glutathione synthetase (EC 6.3.2.3) (GSH synthetase) (GSH-S) (GSHase) (Glutathione synthase)

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00497|reaction.R00497]] `KEGG` `database` - via EC:6.3.2.3
- `is_component_of` --> [[complex.ecocyc.GLUTATHIONE-SYN-CPLX|complex.ecocyc.GLUTATHIONE-SYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b2947|gene.b2947]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P04425`
- `KEGG:ecj:JW2914;eco:b2947;ecoc:C3026_16130;`
- `GeneID:93779050;947445;`
- `GO:GO:0000287; GO:0004363; GO:0005524; GO:0005737; GO:0005829; GO:0006750; GO:0042802; GO:0051289`
- `EC:6.3.2.3`

## Notes

Glutathione synthetase (EC 6.3.2.3) (GSH synthetase) (GSH-S) (GSHase) (Glutathione synthase)
