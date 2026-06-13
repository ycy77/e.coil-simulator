---
entity_id: "protein.P37388"
entity_type: "protein"
name: "xylG"
source_database: "UniProt"
source_id: "P37388"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01722}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01722}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xylG b3567 JW3539"
---

# xylG

`protein.P37388`

## Static

- Type: `protein`
- Source: `UniProt:P37388`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01722}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01722}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex XylFGH involved in xylose import. Responsible for energy coupling to the transport system (Probable). The XylFGH system can also transport ribose in absence of xylose. {ECO:0000255|HAMAP-Rule:MF_01722, ECO:0000269|PubMed:9673030, ECO:0000305}. xylG encodes the predicted ATP-binding subunit of a high-affinity xylose uptake system; XylG contains sequence motifs conserved in ATP-binding cassette proteins; XylG contains an ABC-ABC domain .

## Biological Role

Component of xylose ABC transporter (complex.ecocyc.ABC-33-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex XylFGH involved in xylose import. Responsible for energy coupling to the transport system (Probable). The XylFGH system can also transport ribose in absence of xylose. {ECO:0000255|HAMAP-Rule:MF_01722, ECO:0000269|PubMed:9673030, ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-33-CPLX|complex.ecocyc.ABC-33-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3567|gene.b3567]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37388`
- `KEGG:ecj:JW3539;eco:b3567;ecoc:C3026_19340;`
- `GeneID:948127;`
- `GO:GO:0005524; GO:0005886; GO:0015148; GO:0015614; GO:0015752; GO:0015753; GO:0016020; GO:0016887; GO:0042732; GO:0055052`
- `EC:7.5.2.10`

## Notes

Xylose import ATP-binding protein XylG (EC 7.5.2.10)
