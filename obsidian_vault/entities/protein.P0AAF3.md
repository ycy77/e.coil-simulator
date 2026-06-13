---
entity_id: "protein.P0AAF3"
entity_type: "protein"
name: "araG"
source_database: "UniProt"
source_id: "P0AAF3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01721, ECO:0000269|PubMed:7028715}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01721, ECO:0000269|PubMed:7028715}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "araG b1900 JW1888"
---

# araG

`protein.P0AAF3`

## Static

- Type: `protein`
- Source: `UniProt:P0AAF3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01721, ECO:0000269|PubMed:7028715}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01721, ECO:0000269|PubMed:7028715}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex AraFGH involved in arabinose import. Responsible for energy coupling to the transport system (Probable). {ECO:0000305|PubMed:2656640, ECO:0000305|PubMed:7028715}. araG is predicted to encode a soluble protein. Sequence analysis indicates the presence of putative ATP binding sites .

## Biological Role

Component of arabinose ABC transporter (complex.ecocyc.ABC-2-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex AraFGH involved in arabinose import. Responsible for energy coupling to the transport system (Probable). {ECO:0000305|PubMed:2656640, ECO:0000305|PubMed:7028715}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-2-CPLX|complex.ecocyc.ABC-2-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1900|gene.b1900]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAF3`
- `KEGG:ecj:JW1888;eco:b1900;ecoc:C3026_10785;`
- `GeneID:75171970;946408;`
- `GO:GO:0005524; GO:0005829; GO:0005886; GO:0015147; GO:0015612; GO:0016020; GO:0016887; GO:0042882; GO:0055052`
- `EC:7.5.2.12`

## Notes

Arabinose import ATP-binding protein AraG (EC 7.5.2.12)
