---
entity_id: "protein.P46888"
entity_type: "protein"
name: "uspC"
source_database: "UniProt"
source_id: "P46888"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uspC yecG b1895 JW1884"
---

# uspC

`protein.P46888`

## Static

- Type: `protein`
- Source: `UniProt:P46888`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Required for resistance to DNA-damaging agents. {ECO:0000269|PubMed:11849540}.

## Biological Role

Component of universal stress protein C (complex.ecocyc.CPLX0-8586).

## Annotation

FUNCTION: Required for resistance to DNA-damaging agents. {ECO:0000269|PubMed:11849540}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8586|complex.ecocyc.CPLX0-8586]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1895|gene.b1895]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P46888`
- `KEGG:ecj:JW1884;eco:b1895;ecoc:C3026_10765;`
- `GeneID:946404;`
- `GO:GO:0005737; GO:0006950; GO:0009267; GO:0009651; GO:0034644; GO:0042803; GO:0060090`

## Notes

Universal stress protein C
