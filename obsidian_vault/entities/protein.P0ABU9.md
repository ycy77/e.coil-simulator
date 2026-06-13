---
entity_id: "protein.P0ABU9"
entity_type: "protein"
name: "tolQ"
source_database: "UniProt"
source_id: "P0ABU9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02202, ECO:0000269|PubMed:8300535, ECO:0000269|PubMed:8331075}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02202, ECO:0000269|PubMed:8300535, ECO:0000305|PubMed:8331075}. Note=Accumulates at cell constriction sites. Recruitment to the division site is dependent on FtsN activity. {ECO:0000269|PubMed:17233825}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tolQ fii b0737 JW0727"
---

# tolQ

`protein.P0ABU9`

## Static

- Type: `protein`
- Source: `UniProt:P0ABU9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02202, ECO:0000269|PubMed:8300535, ECO:0000269|PubMed:8331075}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02202, ECO:0000269|PubMed:8300535, ECO:0000305|PubMed:8331075}. Note=Accumulates at cell constriction sites. Recruitment to the division site is dependent on FtsN activity. {ECO:0000269|PubMed:17233825}.

## Enriched Summary

FUNCTION: Part of the Tol-Pal system, which plays a role in outer membrane invagination during cell division and is important for maintaining outer membrane integrity (PubMed:1683466, PubMed:17233825). Required, with TolR, for the proton motive force-dependent activation of TolA and for TolA-Pal interaction (PubMed:11722743). The Tol-Pal system is also required for polar localization of chemoreceptors clusters (PubMed:24720726). The system also appears to be required for the activity of several outer membrane-localized enzymes with cell wall remodeling activity (PubMed:32152098). Is involved in the uptake of group A colicins (colicins A, E1, E2, E3, and K) and in the uptake of filamentous phage DNA (PubMed:1683466, PubMed:3294803). {ECO:0000269|PubMed:11722743, ECO:0000269|PubMed:1683466, ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:24720726, ECO:0000269|PubMed:32152098, ECO:0000269|PubMed:3294803, ECO:0000305|PubMed:1683466}. TolQ is an inner membrane component of the Tol-Pal system - a group of interacting proteins which span the cell envelope of E. coli K-12. The Tol-Pal system plays a role in outer membrane invagination and septal peptidoglycan processing during cell division and is important for maintaining outer membrane integrity via lipid homeostasis...

## Biological Role

Component of energy transducing Tol complex (complex.ecocyc.CPLX0-13341), Tol-Pal Cell Envelope Complex (complex.ecocyc.CPLX0-2201).

## Annotation

FUNCTION: Part of the Tol-Pal system, which plays a role in outer membrane invagination during cell division and is important for maintaining outer membrane integrity (PubMed:1683466, PubMed:17233825). Required, with TolR, for the proton motive force-dependent activation of TolA and for TolA-Pal interaction (PubMed:11722743). The Tol-Pal system is also required for polar localization of chemoreceptors clusters (PubMed:24720726). The system also appears to be required for the activity of several outer membrane-localized enzymes with cell wall remodeling activity (PubMed:32152098). Is involved in the uptake of group A colicins (colicins A, E1, E2, E3, and K) and in the uptake of filamentous phage DNA (PubMed:1683466, PubMed:3294803). {ECO:0000269|PubMed:11722743, ECO:0000269|PubMed:1683466, ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:24720726, ECO:0000269|PubMed:32152098, ECO:0000269|PubMed:3294803, ECO:0000305|PubMed:1683466}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13341|complex.ecocyc.CPLX0-13341]] `EcoCyc` `database` - EcoCyc component coefficient=5 | EcoCyc protcplxs.col coefficient=5
- `is_component_of` --> [[complex.ecocyc.CPLX0-2201|complex.ecocyc.CPLX0-2201]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=5

## Incoming Edges (1)

- `encodes` <-- [[gene.b0737|gene.b0737]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABU9`
- `KEGG:ecj:JW0727;eco:b0737;`
- `GeneID:86863246;93776747;948900;`
- `GO:GO:0005886; GO:0016020; GO:0017038; GO:0030313; GO:0032153; GO:0043213; GO:0051301; GO:0090529; GO:1905153`

## Notes

Tol-Pal system protein TolQ
