---
entity_id: "protein.P19934"
entity_type: "protein"
name: "tolA"
source_database: "UniProt"
source_id: "P19934"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2068069, ECO:0000269|PubMed:2687247}; Single-pass membrane protein {ECO:0000269|PubMed:2687247}. Note=Accumulates at cell constriction sites. Recruitment to the division site is dependent on FtsN activity. {ECO:0000269|PubMed:17233825}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tolA cim excC lky b0739 JW0729"
---

# tolA

`protein.P19934`

## Static

- Type: `protein`
- Source: `UniProt:P19934`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2068069, ECO:0000269|PubMed:2687247}; Single-pass membrane protein {ECO:0000269|PubMed:2687247}. Note=Accumulates at cell constriction sites. Recruitment to the division site is dependent on FtsN activity. {ECO:0000269|PubMed:17233825}.

## Enriched Summary

FUNCTION: Part of the Tol-Pal system, which plays a role in outer membrane invagination during cell division and is important for maintaining outer membrane integrity (PubMed:11115123, PubMed:11994151, PubMed:1683466, PubMed:17233825, PubMed:8416897). The Tol-Pal system is also required for polar localization of chemoreceptors clusters (PubMed:24720726). The system also appears to be required for the activity of several outer membrane-localized enzymes with cell wall remodeling activity (PubMed:32152098). Is involved in the uptake of group A colicins (colicins A, E1, E2, E3, and K) and in the uptake of filamentous phage DNA (PubMed:1683466). {ECO:0000269|PubMed:11115123, ECO:0000269|PubMed:11994151, ECO:0000269|PubMed:1683466, ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:24720726, ECO:0000269|PubMed:32152098, ECO:0000269|PubMed:8416897, ECO:0000305|PubMed:1683466}. TolA is an inner membrane component of the Tol-Pal system - a group of interacting proteins which span the cell envelope of E. coli K-12. The Tol-Pal system plays a role in outer membrane invagination and septal peptidoglycan processing during cell division and is important for maintaining outer membrane integrity via lipid homeostasis. It also has a role in facilitating phage infection and colicin uptake...

## Biological Role

Component of energy transducing Tol complex (complex.ecocyc.CPLX0-13341), Tol-Pal Cell Envelope Complex (complex.ecocyc.CPLX0-2201).

## Annotation

FUNCTION: Part of the Tol-Pal system, which plays a role in outer membrane invagination during cell division and is important for maintaining outer membrane integrity (PubMed:11115123, PubMed:11994151, PubMed:1683466, PubMed:17233825, PubMed:8416897). The Tol-Pal system is also required for polar localization of chemoreceptors clusters (PubMed:24720726). The system also appears to be required for the activity of several outer membrane-localized enzymes with cell wall remodeling activity (PubMed:32152098). Is involved in the uptake of group A colicins (colicins A, E1, E2, E3, and K) and in the uptake of filamentous phage DNA (PubMed:1683466). {ECO:0000269|PubMed:11115123, ECO:0000269|PubMed:11994151, ECO:0000269|PubMed:1683466, ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:24720726, ECO:0000269|PubMed:32152098, ECO:0000269|PubMed:8416897, ECO:0000305|PubMed:1683466}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13341|complex.ecocyc.CPLX0-13341]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-2201|complex.ecocyc.CPLX0-2201]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0739|gene.b0739]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P19934`
- `KEGG:ecj:JW0729;eco:b0739;ecoc:C3026_03710;`
- `GeneID:946625;`
- `GO:GO:0005886; GO:0016020; GO:0017038; GO:0019534; GO:0019904; GO:0032153; GO:0043213; GO:0046718; GO:0046790; GO:0051301; GO:0071237; GO:0090529; GO:0097718; GO:1905153`

## Notes

Tol-Pal system protein TolA
