---
entity_id: "protein.P0ABV6"
entity_type: "protein"
name: "tolR"
source_database: "UniProt"
source_id: "P0ABV6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02203, ECO:0000269|PubMed:8331075, ECO:0000269|PubMed:8376353}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02203, ECO:0000269|PubMed:8376353, ECO:0000305|PubMed:8331075}. Note=Accumulates at cell constriction sites. Recruitment to the division site is dependent on FtsN activity. {ECO:0000269|PubMed:17233825}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tolR b0738 JW0728"
---

# tolR

`protein.P0ABV6`

## Static

- Type: `protein`
- Source: `UniProt:P0ABV6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_02203, ECO:0000269|PubMed:8331075, ECO:0000269|PubMed:8376353}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_02203, ECO:0000269|PubMed:8376353, ECO:0000305|PubMed:8331075}. Note=Accumulates at cell constriction sites. Recruitment to the division site is dependent on FtsN activity. {ECO:0000269|PubMed:17233825}.

## Enriched Summary

FUNCTION: Part of the Tol-Pal system, which plays a role in outer membrane invagination during cell division and is important for maintaining outer membrane integrity (PubMed:1683466, PubMed:17233825). Required, with TolQ, for the proton motive force-dependent activation of TolA and for TolA-Pal interaction (PubMed:11722743). The Tol-Pal system is also required for polar localization of chemoreceptors clusters (PubMed:24720726). The system also appears to be required for the activity of several outer membrane-localized enzymes with cell wall remodeling activity (PubMed:32152098). Modeling suggests that non-covalent binding of OmpA (from the outer membrane) and TolR (from the inner membrane) to peptidoglycan maintains the position of the cell wall in the periplasm, holding it approximately equidistant from both the inner and outer membranes. Trimeric Lpp controls the width of the periplasm, adjusts its tilt angle to accommodate to the available space, and can compensate in part for an absence of OmpA (Probable). {ECO:0000269|PubMed:11722743, ECO:0000269|PubMed:1683466, ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:24720726, ECO:0000269|PubMed:32152098, ECO:0000305|PubMed:30713026}.; FUNCTION: (Microbial infection) Involved in the uptake of group A colicins (colicins A, E1, E2, E3, and K) and in the uptake of filamentous phage DNA...

## Biological Role

Component of energy transducing Tol complex (complex.ecocyc.CPLX0-13341), Tol-Pal Cell Envelope Complex (complex.ecocyc.CPLX0-2201).

## Annotation

FUNCTION: Part of the Tol-Pal system, which plays a role in outer membrane invagination during cell division and is important for maintaining outer membrane integrity (PubMed:1683466, PubMed:17233825). Required, with TolQ, for the proton motive force-dependent activation of TolA and for TolA-Pal interaction (PubMed:11722743). The Tol-Pal system is also required for polar localization of chemoreceptors clusters (PubMed:24720726). The system also appears to be required for the activity of several outer membrane-localized enzymes with cell wall remodeling activity (PubMed:32152098). Modeling suggests that non-covalent binding of OmpA (from the outer membrane) and TolR (from the inner membrane) to peptidoglycan maintains the position of the cell wall in the periplasm, holding it approximately equidistant from both the inner and outer membranes. Trimeric Lpp controls the width of the periplasm, adjusts its tilt angle to accommodate to the available space, and can compensate in part for an absence of OmpA (Probable). {ECO:0000269|PubMed:11722743, ECO:0000269|PubMed:1683466, ECO:0000269|PubMed:17233825, ECO:0000269|PubMed:24720726, ECO:0000269|PubMed:32152098, ECO:0000305|PubMed:30713026}.; FUNCTION: (Microbial infection) Involved in the uptake of group A colicins (colicins A, E1, E2, E3, and K) and in the uptake of filamentous phage DNA. {ECO:0000269|PubMed:1683466, ECO:0000269|PubMed:3294803}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13341|complex.ecocyc.CPLX0-13341]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-2201|complex.ecocyc.CPLX0-2201]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0738|gene.b0738]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABV6`
- `KEGG:ecj:JW0728;eco:b0738;ecoc:C3026_03705;`
- `GeneID:93776746;945328;`
- `GO:GO:0005886; GO:0015031; GO:0016020; GO:0022857; GO:0032153; GO:0043213; GO:0051301; GO:0090529; GO:1905153`

## Notes

Tol-Pal system protein TolR
