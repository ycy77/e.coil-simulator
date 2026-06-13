---
entity_id: "protein.P08395"
entity_type: "protein"
name: "sppA"
source_database: "UniProt"
source_id: "P08395"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:18476724, ECO:0000269|PubMed:3522590}; Single-pass membrane protein {ECO:0000269|PubMed:18476724, ECO:0000269|PubMed:3522590}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sppA b1766 JW1755"
---

# sppA

`protein.P08395`

## Static

- Type: `protein`
- Source: `UniProt:P08395`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:18476724, ECO:0000269|PubMed:3522590}; Single-pass membrane protein {ECO:0000269|PubMed:18476724, ECO:0000269|PubMed:3522590}.

## Enriched Summary

FUNCTION: Digests cleaved signal peptides in vitro, its in vivo function is unknown. This activity is necessary to maintain proper secretion of mature proteins across the membrane. {ECO:0000269|PubMed:18164727, ECO:0000269|PubMed:18476724, ECO:0000269|PubMed:21810987, ECO:0000269|PubMed:3522590}.

## Biological Role

Component of protease IV, a signal peptide peptidase (complex.ecocyc.CPLX0-2941).

## Annotation

FUNCTION: Digests cleaved signal peptides in vitro, its in vivo function is unknown. This activity is necessary to maintain proper secretion of mature proteins across the membrane. {ECO:0000269|PubMed:18164727, ECO:0000269|PubMed:18476724, ECO:0000269|PubMed:21810987, ECO:0000269|PubMed:3522590}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2941|complex.ecocyc.CPLX0-2941]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1766|gene.b1766]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08395`
- `KEGG:ecj:JW1755;eco:b1766;ecoc:C3026_10085;`
- `GeneID:946281;`
- `GO:GO:0004175; GO:0004252; GO:0005886; GO:0006465; GO:0016020`
- `EC:3.4.21.-`

## Notes

Protease 4 (EC 3.4.21.-) (Endopeptidase IV) (Protease IV) (Signal peptide peptidase)
