---
entity_id: "protein.P23839"
entity_type: "protein"
name: "yicC"
source_database: "UniProt"
source_id: "P23839"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yicC orfX b3644 JW3619"
---

# yicC

`protein.P23839`

## Static

- Type: `protein`
- Source: `UniProt:P23839`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Contributes to degradation of small RNA (sRNA) RhyB. Upon overexpression suppresses sRNA-mediated RhyB-silencing of multiple RNA targets but not other sRNA's targets; overexpression leads to loss of RhyB sRNA. Enables degradation of RhyB by 3' to 5' exoribonuclease PNPase (pnp) (PubMed:34210798). Endonucleolytically cleaves ssRNA, probably generating a 3'-OH and a 5'-phosphate group (PubMed:34815358). {ECO:0000269|PubMed:34210798, ECO:0000269|PubMed:34815358}.

## Biological Role

Component of putative RNase adaptor protein YicC (complex.ecocyc.CPLX0-11240).

## Annotation

FUNCTION: Contributes to degradation of small RNA (sRNA) RhyB. Upon overexpression suppresses sRNA-mediated RhyB-silencing of multiple RNA targets but not other sRNA's targets; overexpression leads to loss of RhyB sRNA. Enables degradation of RhyB by 3' to 5' exoribonuclease PNPase (pnp) (PubMed:34210798). Endonucleolytically cleaves ssRNA, probably generating a 3'-OH and a 5'-phosphate group (PubMed:34815358). {ECO:0000269|PubMed:34210798, ECO:0000269|PubMed:34815358}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-11240|complex.ecocyc.CPLX0-11240]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b3644|gene.b3644]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23839`
- `KEGG:ecj:JW3619;eco:b3644;ecoc:C3026_19745;`
- `GeneID:948154;`
- `GO:GO:0005829; GO:0006401; GO:0016891`
- `EC:3.1.26.-`

## Notes

Endoribonuclease YicC (EC 3.1.26.-)
