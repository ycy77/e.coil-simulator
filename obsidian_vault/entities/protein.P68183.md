---
entity_id: "protein.P68183"
entity_type: "protein"
name: "malG"
source_database: "UniProt"
source_id: "P68183"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:18456666, ECO:0000269|PubMed:2233678}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441, ECO:0000269|PubMed:18456666, ECO:0000269|PubMed:2233678}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "malG b4032 JW3992"
---

# malG

`protein.P68183`

## Static

- Type: `protein`
- Source: `UniProt:P68183`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:18456666, ECO:0000269|PubMed:2233678}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00441, ECO:0000269|PubMed:18456666, ECO:0000269|PubMed:2233678}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex MalEFGK involved in maltose/maltodextrin import. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:2026607, ECO:0000269|PubMed:2155217}. MalG is an integral membrane component of the maltose ABC transporter . A MalG-MalF heterodimer forms the translocation channel of the maltose ABC transporter; the MalG-MalF channel contacts the MalK dimer at the cytoplasmic face of the membrane and the MalE binding protein at the periplasmic face of the membrane MalG contains 6 transmembrane (TM) helices; in a crystal structure of the maltose transporter in complex with MalE, maltose and ATP, an EAA loop located between TM4 and 5 is a major area of contact with the MalK dimer while a C-terminal tail region (residues 290296) packs along the Q loop of one MalK monomer .

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

- `encodes` <-- [[gene.b4032|gene.b4032]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P68183`
- `KEGG:ecj:JW3992;eco:b4032;ecoc:C3026_21785;`
- `GeneID:86861565;948530;`
- `GO:GO:0005886; GO:0015423; GO:0015768; GO:0016020; GO:0034763; GO:0042956; GO:0043190; GO:1902344; GO:1990060; GO:1990154`

## Notes

Maltose/maltodextrin transport system permease protein MalG
