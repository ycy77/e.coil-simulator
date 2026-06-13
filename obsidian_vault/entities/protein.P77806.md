---
entity_id: "protein.P77806"
entity_type: "protein"
name: "ybdL"
source_database: "UniProt"
source_id: "P77806"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybdL b0600 JW0593"
---

# ybdL

`protein.P77806`

## Static

- Type: `protein`
- Source: `UniProt:P77806`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Shows aminotransferase activity with methionine and histidine as substrates, and to a lesser extent also with phenylalanine. {ECO:0000269|PubMed:15280032}.

## Biological Role

Component of methionine transaminase (complex.ecocyc.CPLX0-8561).

## Annotation

FUNCTION: Shows aminotransferase activity with methionine and histidine as substrates, and to a lesser extent also with phenylalanine. {ECO:0000269|PubMed:15280032}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8561|complex.ecocyc.CPLX0-8561]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0600|gene.b0600]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77806`
- `KEGG:ecj:JW0593;eco:b0600;ecoc:C3026_03000;`
- `GeneID:945211;`
- `GO:GO:0005737; GO:0010326; GO:0016212; GO:0030170; GO:0042803`
- `EC:2.6.1.88`

## Notes

Methionine aminotransferase (EC 2.6.1.88) (Methionine-oxo-acid transaminase)
