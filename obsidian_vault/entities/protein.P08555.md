---
entity_id: "protein.P08555"
entity_type: "protein"
name: "dsdX"
source_database: "UniProt"
source_id: "P08555"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dsdX orf445 yfdA yfdD b2365 JW2362"
---

# dsdX

`protein.P08555`

## Static

- Type: `protein`
- Source: `UniProt:P08555`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: A D-serine-specific transporter, may function as a H(+) symporter. {ECO:0000250|UniProtKB:A0A0H2VAP9}. DsdX from E. coli clinical isolate CFT073 has been characterised as a D-serine permease . E. coli CFT073 dsdX has 98% identity with dsdX from E. coli K-12. dsdX is located in a serine-inducible operon with EG10249 "dsdA" encoding D-serine deaminase .

## Biological Role

Catalyzes TRANS-RXN0-495 (reaction.ecocyc.TRANS-RXN0-495).

## Annotation

FUNCTION: A D-serine-specific transporter, may function as a H(+) symporter. {ECO:0000250|UniProtKB:A0A0H2VAP9}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-495|reaction.ecocyc.TRANS-RXN0-495]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2365|gene.b2365]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08555`
- `KEGG:ecj:JW2362;eco:b2365;ecoc:C3026_13155;`
- `GeneID:949103;`
- `GO:GO:0005886; GO:0006974; GO:0015128; GO:0035429; GO:0042942; GO:0042945`

## Notes

D-serine transporter DsdX
