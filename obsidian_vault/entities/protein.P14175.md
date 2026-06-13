---
entity_id: "protein.P14175"
entity_type: "protein"
name: "proV"
source_database: "UniProt"
source_id: "P14175"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "proV b2677 JW2652"
---

# proV

`protein.P14175`

## Static

- Type: `protein`
- Source: `UniProt:P14175`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Part of the ProU ABC transporter complex involved in glycine betaine and proline betaine uptake (PubMed:23249124, PubMed:3305496, PubMed:7898450). Probably responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:23249124, ECO:0000269|PubMed:3305496, ECO:0000269|PubMed:7898450, ECO:0000305}. ProV is the predicted ATP binding subunit of an osmoresponsive ABC transport system that imports compounds such as glycine betaine and proline betaine in response to osmotic upshift. ProV contains signature motifs conserved in ATP-binding cassette (ABC) domains . ProV contains a cystathionine β-synthase (CBS) domain which has been implicated in osmosensing (see ) . proV is an experimentally validated antibiotic resistance gene (ARG) .

## Biological Role

Component of glycine betaine ABC transporter (complex.ecocyc.ABC-26-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ProU ABC transporter complex involved in glycine betaine and proline betaine uptake (PubMed:23249124, PubMed:3305496, PubMed:7898450). Probably responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:23249124, ECO:0000269|PubMed:3305496, ECO:0000269|PubMed:7898450, ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-26-CPLX|complex.ecocyc.ABC-26-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2677|gene.b2677]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P14175`
- `KEGG:ecj:JW2652;eco:b2677;ecoc:C3026_14750;`
- `GeneID:75205920;947148;`
- `GO:GO:0005034; GO:0005275; GO:0005524; GO:0006972; GO:0016020; GO:0016887; GO:0031460; GO:0043190; GO:0071470; GO:0089718; GO:1903804; GO:1990222`

## Notes

Glycine betaine/proline betaine transport system ATP-binding protein ProV
