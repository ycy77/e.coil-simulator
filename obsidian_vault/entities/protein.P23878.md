---
entity_id: "protein.P23878"
entity_type: "protein"
name: "fepC"
source_database: "UniProt"
source_id: "P23878"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:3011753}; Peripheral membrane protein {ECO:0000269|PubMed:3011753}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fepC b0588 JW0580"
---

# fepC

`protein.P23878`

## Static

- Type: `protein`
- Source: `UniProt:P23878`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:3011753}; Peripheral membrane protein {ECO:0000269|PubMed:3011753}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex FepBDGC involved in ferric enterobactin uptake (PubMed:1838574, PubMed:3011753). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:1838574, ECO:0000269|PubMed:3011753, ECO:0000305}. fepC encodes the predicted ATP-binding subunit of a ferrric enterobactin ABC transporter complex . Insertional inactivation of fepC results in the loss of ferric enterobactin uptake

## Biological Role

Component of ferric enterobactin ABC transporter (complex.ecocyc.ABC-10-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex FepBDGC involved in ferric enterobactin uptake (PubMed:1838574, PubMed:3011753). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:1838574, ECO:0000269|PubMed:3011753, ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-10-CPLX|complex.ecocyc.ABC-10-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0588|gene.b0588]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23878`
- `KEGG:ecj:JW0580;eco:b0588;ecoc:C3026_02935;`
- `GeneID:75170592;945201;`
- `GO:GO:0005524; GO:0005886; GO:0015620; GO:0015624; GO:0015685; GO:0016020; GO:0016887; GO:0033212; GO:0055052; GO:0071281`
- `EC:7.2.2.17`

## Notes

Ferric enterobactin transport ATP-binding protein FepC (EC 7.2.2.17)
