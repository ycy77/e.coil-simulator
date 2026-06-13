---
entity_id: "protein.P15031"
entity_type: "protein"
name: "fecE"
source_database: "UniProt"
source_id: "P15031"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2651410}; Peripheral membrane protein {ECO:0000305|PubMed:2651410}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fecE b4287 JW4247"
---

# fecE

`protein.P15031`

## Static

- Type: `protein`
- Source: `UniProt:P15031`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2651410}; Peripheral membrane protein {ECO:0000305|PubMed:2651410}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex FecBCDE involved in citrate-dependent Fe(3+) uptake (PubMed:2651410). Binds ATP (PubMed:1526456). Probably responsible for energy coupling to the transport system (PubMed:1526456). {ECO:0000269|PubMed:1526456, ECO:0000269|PubMed:2651410}. fecE encodes a hydrophilic protein that is found in the membrane fraction; it contains conserved ATP-binding sites and is predicted to be the peripheral membrane, ATP-binding protein of the ferric dicitrate ABC transport system . Cloned, overexpressed FecE binds ATP .

## Biological Role

Component of ferric citrate ABC transporter (complex.ecocyc.ABC-9-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex FecBCDE involved in citrate-dependent Fe(3+) uptake (PubMed:2651410). Binds ATP (PubMed:1526456). Probably responsible for energy coupling to the transport system (PubMed:1526456). {ECO:0000269|PubMed:1526456, ECO:0000269|PubMed:2651410}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-9-CPLX|complex.ecocyc.ABC-9-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4287|gene.b4287]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15031`
- `KEGG:ecj:JW4247;eco:b4287;ecoc:C3026_23120;`
- `GeneID:948819;`
- `GO:GO:0005524; GO:0005886; GO:0006879; GO:0015620; GO:0015685; GO:0016020; GO:0016887; GO:0033212; GO:0055052; GO:0071281`
- `EC:7.2.2.18`

## Notes

Fe(3+) dicitrate transport ATP-binding protein FecE (EC 7.2.2.18) (Iron(III) dicitrate transport ATP-binding protein FecE)
