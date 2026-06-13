---
entity_id: "protein.P0AGA2"
entity_type: "protein"
name: "secY"
source_database: "UniProt"
source_id: "P0AGA2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "secY prlA b3300 JW3262"
---

# secY

`protein.P0AGA2`

## Static

- Type: `protein`
- Source: `UniProt:P0AGA2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: The central subunit of the protein translocation channel SecYEG. Consists of two halves formed by TMs 1-5 and 6-10. These two domains form a lateral gate at the front which open onto the bilayer between TMs 2 and 7, and are clamped together by SecE at the back. The channel is closed by both a pore ring composed of hydrophobic SecY resides and a short helix (helix 2A) on the extracellular side of the membrane which forms a plug. The plug probably moves laterally to allow the channel to open. The ring and the pore may move independently. SecY is required to insert newly synthesized SecY into the inner membrane. Overexpression of some hybrid proteins has been thought to jam the protein secretion apparatus resulting in cell death; while this may be true, overexpression also results in FtsH-mediated degradation of SecY. The SecY inner membrane protein is the core component of the heterotrimeric SecYEG preprotein translocase; SecY forms the protein conducting channel with channel plug and hydrophobic seal; SecY contains a signal sequence binding pocket and cytosolic loops that interact with partner proteins (see and ). SecY is required for efficient protein translocation across the cytoplasmic membrane...

## Biological Role

Component of SecYEG-SecA complex (complex.ecocyc.CPLX0-12269), Sec Holo-Translocon (complex.ecocyc.SEC-SECRETION-CPLX), SecYEG translocon (complex.ecocyc.SECE-G-Y-CPLX).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: The central subunit of the protein translocation channel SecYEG. Consists of two halves formed by TMs 1-5 and 6-10. These two domains form a lateral gate at the front which open onto the bilayer between TMs 2 and 7, and are clamped together by SecE at the back. The channel is closed by both a pore ring composed of hydrophobic SecY resides and a short helix (helix 2A) on the extracellular side of the membrane which forms a plug. The plug probably moves laterally to allow the channel to open. The ring and the pore may move independently. SecY is required to insert newly synthesized SecY into the inner membrane. Overexpression of some hybrid proteins has been thought to jam the protein secretion apparatus resulting in cell death; while this may be true, overexpression also results in FtsH-mediated degradation of SecY.

## Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12269|complex.ecocyc.CPLX0-12269]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.SEC-SECRETION-CPLX|complex.ecocyc.SEC-SECRETION-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.SECE-G-Y-CPLX|complex.ecocyc.SECE-G-Y-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3300|gene.b3300]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGA2`
- `KEGG:ecj:JW3262;eco:b3300;ecoc:C3026_17940;`
- `GeneID:86862302;947799;`
- `GO:GO:0005048; GO:0005886; GO:0006616; GO:0006886; GO:0008320; GO:0016020; GO:0031522; GO:0043952; GO:0065002`

## Notes

Protein translocase subunit SecY
