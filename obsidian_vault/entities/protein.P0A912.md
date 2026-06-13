---
entity_id: "protein.P0A912"
entity_type: "protein"
name: "pal"
source_database: "UniProt"
source_id: "P0A912"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_02204, ECO:0000269|PubMed:1574003}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_02204, ECO:0000269|PubMed:1574003}. Note=Accumulates at cell constriction sites. Recruitment to the division site is dependent on FtsN activity. {ECO:0000269|PubMed:17233825}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pal excC b0741 JW0731"
---

# pal

`protein.P0A912`

## Static

- Type: `protein`
- Source: `UniProt:P0A912`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000255|HAMAP-Rule:MF_02204, ECO:0000269|PubMed:1574003}; Lipid-anchor {ECO:0000255|HAMAP-Rule:MF_02204, ECO:0000269|PubMed:1574003}. Note=Accumulates at cell constriction sites. Recruitment to the division site is dependent on FtsN activity. {ECO:0000269|PubMed:17233825}.

## Enriched Summary

FUNCTION: Part of the Tol-Pal system, which plays a role in outer membrane invagination during cell division and is important for maintaining outer membrane integrity (PubMed:11115123, PubMed:17233825). The Tol-Pal system is also required for polar localization of chemoreceptors clusters (PubMed:24720726). The system also appears to be required for the activity of several outer membrane-localized enzymes with cell wall remodeling activity (PubMed:32152098). {ECO:0000269|PubMed:11115123, ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:24720726, ECO:0000269|PubMed:32152098}. Pal is an outer membrane component of the Tol-Pal system - a group of interacting proteins which span the cell envelope in E. coli K-12. The Tol-Pal system plays a role in outer membrane invagination and septal peptidoglycan processing during cell division and is important for maintaining outer membrane integrity via lipid homeostasis. It also has a role in facilitating phage infection and colicin uptake. Pal is a peptidoglycan-associated outer membrane lipoprotein . Pal interacts with TolA in vivo; this interaction requires the proton motive force . Pal interacts with TolB in vivo . Pal interacts with OmpA in vivo . Purified Pal binds peptidoglycan in vitro; the interaction of Pal with peptidoglycan and TolB may be exclusive - a TolB-Pal complex does not appear to be associated with the peptidoglycan...

## Biological Role

Component of Tol-Pal Cell Envelope Complex (complex.ecocyc.CPLX0-2201).

## Annotation

FUNCTION: Part of the Tol-Pal system, which plays a role in outer membrane invagination during cell division and is important for maintaining outer membrane integrity (PubMed:11115123, PubMed:17233825). The Tol-Pal system is also required for polar localization of chemoreceptors clusters (PubMed:24720726). The system also appears to be required for the activity of several outer membrane-localized enzymes with cell wall remodeling activity (PubMed:32152098). {ECO:0000269|PubMed:11115123, ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:24720726, ECO:0000269|PubMed:32152098}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2201|complex.ecocyc.CPLX0-2201]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0741|gene.b0741]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A912`
- `KEGG:ecj:JW0731;eco:b0741;ecoc:C3026_03720;`
- `GeneID:86863250;93776743;945004;`
- `GO:GO:0009279; GO:0016020; GO:0032153; GO:0051301; GO:0090529; GO:1905153`

## Notes

Peptidoglycan-associated lipoprotein (PAL) (Tol-Pal system lipoprotein Pal)
