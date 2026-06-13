---
entity_id: "protein.P02916"
entity_type: "protein"
name: "malF"
source_database: "UniProt"
source_id: "P02916"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:18456666}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441, ECO:0000269|PubMed:18456666}; Periplasmic side {ECO:0000269|PubMed:18456666}. Note=A substantial portion of it protrudes into the periplasmic space; inserts in an SRP- and Sec-dependent, YidC-independent fashion into the membrane."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "malF b4033 JW3993"
---

# malF

`protein.P02916`

## Static

- Type: `protein`
- Source: `UniProt:P02916`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:18456666}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441, ECO:0000269|PubMed:18456666}; Periplasmic side {ECO:0000269|PubMed:18456666}. Note=A substantial portion of it protrudes into the periplasmic space; inserts in an SRP- and Sec-dependent, YidC-independent fashion into the membrane.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex MalEFGK involved in maltose/maltodextrin import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:2026607, ECO:0000269|PubMed:2155217}. MalF is an integral membrane component of the maltose ABC transporter . A MalF-MalG heterodimer forms the translocation channel of the maltose ABC transporter; the MalF-MalG channel contacts the MalK dimer at the cytoplasmic face of the membrane and the MalE binding protein at the periplasmic face of the membrane MalF contains 8 transmembrane (TM) helices; in a crystal structure of the maltose transporter in complex with MalE, maltose and ATP, the MalF periplasmic loop (P2) located between TM 3 and 4 is a major area of contact with the maltose binding protein MalE, while an EAA loop located between TM 6 and 7 is a major area of contact with the MalK dimer . malF mutations that alter the substrate specificity of the maltose ABC transporter have been isolated and characterised . Insertion of MalF into the cytoplasmic membrane is SecE- and SecA-dependent ; MalF can assemble in the membrane independently of the bacterial secretion machinery .

## Biological Role

Component of maltose ABC transporter (complex.ecocyc.ABC-16-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex MalEFGK involved in maltose/maltodextrin import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:2026607, ECO:0000269|PubMed:2155217}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-16-CPLX|complex.ecocyc.ABC-16-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4033|gene.b4033]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02916`
- `KEGG:ecj:JW3993;eco:b4033;`
- `GeneID:948532;`
- `GO:GO:0005886; GO:0006974; GO:0015423; GO:0015768; GO:0016020; GO:0034763; GO:0042956; GO:0043190; GO:1902344; GO:1990060; GO:1990154`

## Notes

Maltose/maltodextrin transport system permease protein MalF
