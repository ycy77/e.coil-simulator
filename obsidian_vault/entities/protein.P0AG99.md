---
entity_id: "protein.P0AG99"
entity_type: "protein"
name: "secG"
source_database: "UniProt"
source_id: "P0AG99"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "secG b3175 JW3142"
---

# secG

`protein.P0AG99`

## Static

- Type: `protein`
- Source: `UniProt:P0AG99`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Subunit of the protein translocation channel SecYEG. Overexpression of some hybrid proteins has been thought to jam the protein secretion apparatus resulting in cell death; while this may be true it also results in FtsH-mediated degradation of SecY. Treatment with antibiotics that block translation elongation such as chloramphenicol also leads to degradation of SecY and SecE but not SecG. The SecG inner membrane protein is a component of the heterotrimeric SecYEG preprotein translocase. SecY, SecE and an unidentified polypeptide termed 'band1' (later shown to be SecG ) form a stable complex which supports precursor protein translocation in vitro . SecG stimulates translocation of a model secretory protein in SecYE containing proteoliposomes . SecG is not required for SecA binding to SecYE containing proteoliposomes; the translocation ATPase activity of SecA in SecYE containing proteoliposomes is enhanced by the presence of SecG . SecG participates in preprotein signal sequence recognition . SecG contributes to the stability of the translocase and to the interaction with signal sequence . SecG stimulates SecA insertion at SecYE after the initiation of translocation has begun . Two SecG molecules may be present in a single translocon . SecG and SecA may act cooperatively to facilitate preprotein translocation...

## Biological Role

Component of SecYEG-SecA complex (complex.ecocyc.CPLX0-12269), Sec Holo-Translocon (complex.ecocyc.SEC-SECRETION-CPLX), SecYEG translocon (complex.ecocyc.SECE-G-Y-CPLX).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: Subunit of the protein translocation channel SecYEG. Overexpression of some hybrid proteins has been thought to jam the protein secretion apparatus resulting in cell death; while this may be true it also results in FtsH-mediated degradation of SecY. Treatment with antibiotics that block translation elongation such as chloramphenicol also leads to degradation of SecY and SecE but not SecG.

## Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12269|complex.ecocyc.CPLX0-12269]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` --> [[complex.ecocyc.SEC-SECRETION-CPLX|complex.ecocyc.SEC-SECRETION-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.SECE-G-Y-CPLX|complex.ecocyc.SECE-G-Y-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3175|gene.b3175]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG99`
- `KEGG:ecj:JW3142;eco:b3175;ecoc:C3026_17290;`
- `GeneID:89518018;93778806;947720;`
- `GO:GO:0005886; GO:0006616; GO:0006886; GO:0008320; GO:0009306; GO:0015450; GO:0016020; GO:0031522; GO:0043952; GO:0065002`

## Notes

Protein-export membrane protein SecG (P12) (Preprotein translocase band 1 subunit)
