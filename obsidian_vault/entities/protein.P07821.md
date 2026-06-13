---
entity_id: "protein.P07821"
entity_type: "protein"
name: "fhuC"
source_database: "UniProt"
source_id: "P07821"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1551849}; Peripheral membrane protein {ECO:0000269|PubMed:1551849}. Note=FhuB mediates the association of FhuC with the cytoplasmic membrane. {ECO:0000269|PubMed:1551849}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fhuC b0151 JW0147"
---

# fhuC

`protein.P07821`

## Static

- Type: `protein`
- Source: `UniProt:P07821`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1551849}; Peripheral membrane protein {ECO:0000269|PubMed:1551849}. Note=FhuB mediates the association of FhuC with the cytoplasmic membrane. {ECO:0000269|PubMed:1551849}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex FhuCDB involved in iron(3+)-hydroxamate import. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:1551849, ECO:0000269|PubMed:34887516}. FhuC is the predicted ATP-binding subunit of a high-affinity transport system for the uptake of iron (III)-hydroxamate compounds such as ferrichrome and ferric coprogen. FhuC contains signature motifs conserved in ATP-binding cassette (ABC) domains .

## Biological Role

Component of Fe(3+) hydroxamate ABC transporter (complex.ecocyc.ABC-11-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex FhuCDB involved in iron(3+)-hydroxamate import. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:1551849, ECO:0000269|PubMed:34887516}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-11-CPLX|complex.ecocyc.ABC-11-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0151|gene.b0151]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07821`
- `KEGG:ecj:JW0147;eco:b0151;ecoc:C3026_00685;`
- `GeneID:945250;`
- `GO:GO:0005524; GO:0005886; GO:0015091; GO:0015344; GO:0015625; GO:0015687; GO:0016887; GO:0043190; GO:0055052; GO:0071281; GO:0098711`
- `EC:7.2.2.16`

## Notes

Iron(3+)-hydroxamate import ATP-binding protein FhuC (EC 7.2.2.16) (Ferric hydroxamate uptake protein C) (Ferrichrome transport ATP-binding protein FhuC) (Iron(III)-hydroxamate import ATP-binding protein FhuC)
