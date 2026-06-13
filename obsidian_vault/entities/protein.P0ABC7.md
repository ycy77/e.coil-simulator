---
entity_id: "protein.P0ABC7"
entity_type: "protein"
name: "hflK"
source_database: "UniProt"
source_id: "P0ABC7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:8947034}; Single-pass type II membrane protein {ECO:0000269|PubMed:8947034}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hflK hflA b4174 JW4132"
---

# hflK

`protein.P0ABC7`

## Static

- Type: `protein`
- Source: `UniProt:P0ABC7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:8947034}; Single-pass type II membrane protein {ECO:0000269|PubMed:8947034}.

## Enriched Summary

FUNCTION: HflC and HflK help govern the stability of phage lambda cII protein, and thereby control the lysogenization frequency of phage lambda. HflKC inhibits the SecY-degrading activity of FtsH, possibly helping quality control of integral membrane proteins. {ECO:0000269|PubMed:8947034}. HflK is an inner membrane protein which forms part of the HflCK complex that interacts with and regulates, the ATP-dependent protease FtsH . HflK expressed as a single subunit is unstable in vivo . HflK has been purified as a single subunit after overexpression of both hflK and hflC in an E. coli strain lacking the chromosomal hflCK genes. The purified subunit can inhibit FtsH mediated proteolysis of the bacteriophage lambda cII protein in vitro . Fluorescence microscopy of live cells indicated that expression of hflK is growth stage dependent - it is very low in exponential growing cells and significantly higher in stationary phase cells. In addition, the study found that HflK, tagged by fusion to mCherry (a red fluorescent protein) localizes in discrete foci on cell poles or on the septum region of the cells .

## Biological Role

Component of HflK-HflC complex; regulator of FtsH protease (complex.ecocyc.CPLX0-1321), FtsH/HflKC protease complex (complex.ecocyc.CPLX0-2982).

## Annotation

FUNCTION: HflC and HflK help govern the stability of phage lambda cII protein, and thereby control the lysogenization frequency of phage lambda. HflKC inhibits the SecY-degrading activity of FtsH, possibly helping quality control of integral membrane proteins. {ECO:0000269|PubMed:8947034}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1321|complex.ecocyc.CPLX0-1321]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-2982|complex.ecocyc.CPLX0-2982]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b4174|gene.b4174]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABC7`
- `KEGG:ecj:JW4132;eco:b4174;ecoc:C3026_22555;`
- `GeneID:86861432;93777647;948698;`
- `GO:GO:0005829; GO:0009408; GO:0098796; GO:0098797`

## Notes

Modulator of FtsH protease HflK
