---
entity_id: "protein.P0A8H6"
entity_type: "protein"
name: "yihI"
source_database: "UniProt"
source_id: "P0A8H6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yihI b3866 JW3837"
---

# yihI

`protein.P0A8H6`

## Static

- Type: `protein`
- Source: `UniProt:P0A8H6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A GTPase-activating protein (GAP) that modifies Der/EngA GTPase function, negatively regulating cell growth, probably via ribosome assembly. Stimulates the GTPase activity of Der; a construct missing the first 45 residues is even more stimulatory. Does not stimulate 2 other GTPases (ObgE and Era). Overexpression inhibits cell growth; precursor 16S rRNA accumulates, the 23S rRNA is 6-7 bases longer than usual, and 50S ribosomal subunits are improperly assembled, leading to 45S subunits lacking proteins L9, L18 and L25. Overexpression of Der in the same cells suppresses the 50S subunit assembly defect, corroborating that YihI and Der interact. {ECO:0000269|PubMed:20434458}.

## Biological Role

Component of Der GTPase-activating protein YihI (complex.ecocyc.CPLX0-7853).

## Annotation

FUNCTION: A GTPase-activating protein (GAP) that modifies Der/EngA GTPase function, negatively regulating cell growth, probably via ribosome assembly. Stimulates the GTPase activity of Der; a construct missing the first 45 residues is even more stimulatory. Does not stimulate 2 other GTPases (ObgE and Era). Overexpression inhibits cell growth; precursor 16S rRNA accumulates, the 23S rRNA is 6-7 bases longer than usual, and 50S ribosomal subunits are improperly assembled, leading to 45S subunits lacking proteins L9, L18 and L25. Overexpression of Der in the same cells suppresses the 50S subunit assembly defect, corroborating that YihI and Der interact. {ECO:0000269|PubMed:20434458}.

## Outgoing Edges (2)

- `activates` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_component_of` --> [[complex.ecocyc.CPLX0-7853|complex.ecocyc.CPLX0-7853]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3866|gene.b3866]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8H6`
- `KEGG:ecj:JW3837;eco:b3866;ecoc:C3026_20895;`
- `GeneID:75174100;75204333;948363;`
- `GO:GO:0005096; GO:0005829; GO:0042254; GO:0090071`

## Notes

Der GTPase-activating protein YihI (GAP)
