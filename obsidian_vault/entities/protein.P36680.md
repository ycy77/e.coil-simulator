---
entity_id: "protein.P36680"
entity_type: "protein"
name: "zapD"
source_database: "UniProt"
source_id: "P36680"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01092, ECO:0000269|PubMed:22505682}. Note=Localizes to mid-cell in an FtsZ-dependent manner. Localization does not require FtsA, ZipA, ZapA or ZapC."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "zapD yacF b0102 JW0099"
---

# zapD

`protein.P36680`

## Static

- Type: `protein`
- Source: `UniProt:P36680`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01092, ECO:0000269|PubMed:22505682}. Note=Localizes to mid-cell in an FtsZ-dependent manner. Localization does not require FtsA, ZipA, ZapA or ZapC.

## Enriched Summary

FUNCTION: Cell division factor that enhances FtsZ-ring assembly. Directly interacts with FtsZ and promotes bundling of FtsZ protofilaments, with a reduction in FtsZ GTPase activity. {ECO:0000255|HAMAP-Rule:MF_01092, ECO:0000269|PubMed:22505682}.

## Biological Role

Component of cell division factor ZapD (complex.ecocyc.CPLX0-7973).

## Annotation

FUNCTION: Cell division factor that enhances FtsZ-ring assembly. Directly interacts with FtsZ and promotes bundling of FtsZ protofilaments, with a reduction in FtsZ GTPase activity. {ECO:0000255|HAMAP-Rule:MF_01092, ECO:0000269|PubMed:22505682}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7973|complex.ecocyc.CPLX0-7973]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0102|gene.b0102]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36680`
- `KEGG:ecj:JW0099;eco:b0102;ecoc:C3026_00415;`
- `GeneID:93777333;944873;`
- `GO:GO:0000917; GO:0005829; GO:0032153; GO:0042802; GO:0042803; GO:0043093`

## Notes

Cell division protein ZapD (Z ring-associated protein D)
