---
entity_id: "protein.P0AFR7"
entity_type: "protein"
name: "ycjO"
source_database: "UniProt"
source_id: "P0AFR7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycjO b1311 JW1304"
---

# ycjO

`protein.P0AFR7`

## Static

- Type: `protein`
- Source: `UniProt:P0AFR7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex YcjNOPV primarily involved in maltose uptake (PubMed:40721696). The transporter may also be involved in the uptake of glucosides (PubMed:40721696). In vitro, it actively transports ethidium bromide (EB) (PubMed:40721696). This subunit is responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:40721696, ECO:0000305}. YcjO is one of two predicted inner membrane components of a putative ATP-binding cassette transporter (YcjNOPV) .

## Biological Role

Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-55-CPLX).

## Annotation

FUNCTION: Part of the ABC transporter complex YcjNOPV primarily involved in maltose uptake (PubMed:40721696). The transporter may also be involved in the uptake of glucosides (PubMed:40721696). In vitro, it actively transports ethidium bromide (EB) (PubMed:40721696). This subunit is responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:40721696, ECO:0000305}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-55-CPLX|complex.ecocyc.ABC-55-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1311|gene.b1311]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFR7`
- `KEGG:ecj:JW1304;eco:b1311;ecoc:C3026_07685;`
- `GeneID:93775437;945888;`
- `GO:GO:0005886; GO:0016020; GO:0055052; GO:0055085`

## Notes

Maltose transport system permease protein YcjO
