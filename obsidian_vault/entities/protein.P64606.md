---
entity_id: "protein.P64606"
entity_type: "protein"
name: "mlaE"
source_database: "UniProt"
source_id: "P64606"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:19383799}; Multi-pass membrane protein {ECO:0000255, ECO:0000305|PubMed:19383799}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mlaE yrbE b3194 JW3161"
---

# mlaE

`protein.P64606`

## Static

- Type: `protein`
- Source: `UniProt:P64606`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000305|PubMed:19383799}; Multi-pass membrane protein {ECO:0000255, ECO:0000305|PubMed:19383799}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex MlaFEDB, which is involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:19383799, ECO:0000269|PubMed:27529189}. mlaE encodes an inner membrane subunit of the MlaFEDB transporter complex which functions as part of a retrograde and/or anterograde intermembrane phospholipid trafficking system. MlaE is the predicted permease component of a retrograde phospholipid trafficking pathway; a ΔmlaE mutant displays increased SDS-EDTA sensitivity . MlaE forms a stable complex with MlaF, MlaD, and MlaB . In the MlaFEDB cryo-EM structures determined by , dimeric MlaE forms the transmembrane core of the complex interacting with both the periplasmic MlaD hexamer and the cytoplasmic MlaF dimer; each MlaE subunit consists of five transmembrane domains plus an N-terminal 'elbow helix' which runs parallel to the plane of the membrane; in the phospholipid-bound MlaFEDB structure, dimeric MlaE binds phospholipid within a V-shaped cavity that extends into the periplasm and forms a continuous pathway with the central channel of the MlaD hexamer (see also )...

## Biological Role

Component of intermembrane phospholipid transport system (complex.ecocyc.ABC-45-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex MlaFEDB, which is involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:19383799, ECO:0000269|PubMed:27529189}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-45-CPLX|complex.ecocyc.ABC-45-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3194|gene.b3194]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64606`
- `KEGG:ecj:JW3161;eco:b3194;`
- `GeneID:93778787;947732;`
- `GO:GO:0005548; GO:0005886; GO:0015914; GO:0016020; GO:0043190; GO:0120010; GO:0120014; GO:1990531`

## Notes

Intermembrane phospholipid transport system permease protein MlaE
