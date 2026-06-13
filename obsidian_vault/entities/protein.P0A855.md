---
entity_id: "protein.P0A855"
entity_type: "protein"
name: "tolB"
source_database: "UniProt"
source_id: "P0A855"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_00671, ECO:0000269|PubMed:2687247, ECO:0000269|PubMed:7929011}. Note=Partially associated with the outer membrane through a specific interaction with Pal (PubMed:7744736). Accumulates at cell constriction sites. Recruitment to the division site is dependent on FtsN activity (PubMed:17233825). {ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:7744736}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tolB b0740 JW5100"
---

# tolB

`protein.P0A855`

## Static

- Type: `protein`
- Source: `UniProt:P0A855`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_00671, ECO:0000269|PubMed:2687247, ECO:0000269|PubMed:7929011}. Note=Partially associated with the outer membrane through a specific interaction with Pal (PubMed:7744736). Accumulates at cell constriction sites. Recruitment to the division site is dependent on FtsN activity (PubMed:17233825). {ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:7744736}.

## Enriched Summary

FUNCTION: Part of the Tol-Pal system, which plays a role in outer membrane invagination during cell division and is important for maintaining outer membrane integrity (PubMed:17233825). TolB occupies a key intermediary position in the Tol-Pal system because it communicates directly with both membrane-embedded components, Pal in the outer membrane and TolA in the inner membrane (PubMed:19696740). The Tol-Pal system is also required for polar localization of chemoreceptors clusters (PubMed:24720726). The system also appears to be required for the activity of several outer membrane-localized enzymes with cell wall remodeling activity (PubMed:32152098). Is involved in the uptake of some colicins A (PubMed:11994151, PubMed:2687247, PubMed:7929011). {ECO:0000269|PubMed:11994151, ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:19696740, ECO:0000269|PubMed:24720726, ECO:0000269|PubMed:32152098, ECO:0000305|PubMed:2687247, ECO:0000305|PubMed:7929011}. TolB is a periplasmic component of the Tol-Pal system - a group of interacting proteins which span the cell envelope of E. coli K-12. The Tol-Pal system plays a role in outer membrane invagination and septal peptidoglycan processing during cell division and is important for maintaining outer membrane integrity via lipid homeostasis. It also has a role in facilitating phage infection and colicin uptake...

## Biological Role

Component of Tol-Pal Cell Envelope Complex (complex.ecocyc.CPLX0-2201).

## Annotation

FUNCTION: Part of the Tol-Pal system, which plays a role in outer membrane invagination during cell division and is important for maintaining outer membrane integrity (PubMed:17233825). TolB occupies a key intermediary position in the Tol-Pal system because it communicates directly with both membrane-embedded components, Pal in the outer membrane and TolA in the inner membrane (PubMed:19696740). The Tol-Pal system is also required for polar localization of chemoreceptors clusters (PubMed:24720726). The system also appears to be required for the activity of several outer membrane-localized enzymes with cell wall remodeling activity (PubMed:32152098). Is involved in the uptake of some colicins A (PubMed:11994151, PubMed:2687247, PubMed:7929011). {ECO:0000269|PubMed:11994151, ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:19696740, ECO:0000269|PubMed:24720726, ECO:0000269|PubMed:32152098, ECO:0000305|PubMed:2687247, ECO:0000305|PubMed:7929011}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2201|complex.ecocyc.CPLX0-2201]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0740|gene.b0740]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A855`
- `KEGG:ecj:JW5100;eco:b0740;ecoc:C3026_03715;`
- `GeneID:93776744;945429;`
- `GO:GO:0015031; GO:0016020; GO:0017038; GO:0019904; GO:0030288; GO:0032153; GO:0032991; GO:0042597; GO:0043213; GO:0044877; GO:0051301; GO:0071237; GO:0090529; GO:1905153`

## Notes

Tol-Pal system protein TolB
