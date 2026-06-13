---
entity_id: "protein.P0ABC3"
entity_type: "protein"
name: "hflC"
source_database: "UniProt"
source_id: "P0ABC3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:8947034}; Single-pass type II membrane protein {ECO:0000269|PubMed:8947034}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hflC hflA b4175 JW4133"
---

# hflC

`protein.P0ABC3`

## Static

- Type: `protein`
- Source: `UniProt:P0ABC3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:8947034}; Single-pass type II membrane protein {ECO:0000269|PubMed:8947034}.

## Enriched Summary

FUNCTION: HflC and HflK help govern the stability of phage lambda cII protein, and thereby control the lysogenization frequency of phage lambda. HflKC inhibits the SecY-degrading activity of FtsH, possibly helping quality control of integral membrane proteins. {ECO:0000269|PubMed:8947034}. HflC is an inner membrane protein which forms part of the HflCK complex that interacts with and regulates, the ATP-dependent protease FtsH . HflC expressed as a single subunit is unstable in vivo . HflC has been purified as a single subunit after overexpression of both hflK and hflC in an E. coli strain lacking the chromosomal hflCK genes. The purified subunit can inhibit FtsH mediated proteolysis of the bacteriophage lambda cII protein in vitro . A study aiming to isolate detergent-resistant membranes (DRMs) has found that HflC, tagged by fusion with mCherry (a red monomeric fluorescent protein), was found to be localized on discrete foci on the poles of the normal cells .

## Biological Role

Component of HflK-HflC complex; regulator of FtsH protease (complex.ecocyc.CPLX0-1321), FtsH/HflKC protease complex (complex.ecocyc.CPLX0-2982).

## Annotation

FUNCTION: HflC and HflK help govern the stability of phage lambda cII protein, and thereby control the lysogenization frequency of phage lambda. HflKC inhibits the SecY-degrading activity of FtsH, possibly helping quality control of integral membrane proteins. {ECO:0000269|PubMed:8947034}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1321|complex.ecocyc.CPLX0-1321]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-2982|complex.ecocyc.CPLX0-2982]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b4175|gene.b4175]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABC3`
- `KEGG:ecj:JW4133;eco:b4175;ecoc:C3026_22560;`
- `GeneID:86861431;93777646;948697;`
- `GO:GO:0009408; GO:0098796; GO:0098797`

## Notes

Modulator of FtsH protease HflC
