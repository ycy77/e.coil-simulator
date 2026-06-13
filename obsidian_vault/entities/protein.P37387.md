---
entity_id: "protein.P37387"
entity_type: "protein"
name: "xylF"
source_database: "UniProt"
source_id: "P37387"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xylF xylT b3566 JW3538"
---

# xylF

`protein.P37387`

## Static

- Type: `protein`
- Source: `UniProt:P37387`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Involved in the high-affinity D-xylose membrane transport system. Binds with high affinity to xylose. XylF is the periplasmic binding protein of an ATP-dependent, high-affinity xylose uptake system. Purified XylF binds a sngle molecule of D-xylose with high affinity (Kd = 0.6 µM); XylF binds D-xylose specifically - in a wide range of sugars tested only methyl-α-D-xylofuranoside showed some inhibition of D-xylose binding . XylF consists of two similar globular domains connected by a three-stranded hinge; xylose (as the chair form β-pyranose) binds in the cleft between the two domains . Based on the comparison of XylF-open-apo, XylF-open-xyl and XylF-closed-xyl crystal structures, a description of the conformational change that accompanies ligand binding to XylF is available .

## Biological Role

Component of xylose ABC transporter (complex.ecocyc.ABC-33-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Involved in the high-affinity D-xylose membrane transport system. Binds with high affinity to xylose.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-33-CPLX|complex.ecocyc.ABC-33-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3566|gene.b3566]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37387`
- `KEGG:ecj:JW3538;eco:b3566;ecoc:C3026_19335;`
- `GeneID:86862023;948090;`
- `GO:GO:0015752; GO:0015753; GO:0016020; GO:0030246; GO:0030288; GO:0042732; GO:0048029; GO:0055052`

## Notes

D-xylose-binding periplasmic protein
