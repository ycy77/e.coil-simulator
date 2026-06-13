---
entity_id: "protein.P32716"
entity_type: "protein"
name: "mdtN"
source_database: "UniProt"
source_id: "P32716"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass type II membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtN yjcR b4082 JW4043"
---

# mdtN

`protein.P32716`

## Static

- Type: `protein`
- Source: `UniProt:P32716`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Single-pass type II membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Could be involved in resistance to puromycin, acriflavine and tetraphenylarsonium chloride. MdtN is predicted to be the membrane fusion protein component of a putative multidrug efflux pump . An mdtN null mutant is more sensitive to sulfonamide antibiotics than wild type . sdsR: sulfa drug sensitivity mdtN: multi drug transporter

## Biological Role

Component of putative multidrug efflux pump MdtNOP (complex.ecocyc.CPLX0-7807).

## Annotation

FUNCTION: Could be involved in resistance to puromycin, acriflavine and tetraphenylarsonium chloride.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7807|complex.ecocyc.CPLX0-7807]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4082|gene.b4082]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32716`
- `KEGG:ecj:JW4043;eco:b4082;ecoc:C3026_22065;`
- `GeneID:948598;`
- `GO:GO:0005886; GO:0015546; GO:0016020; GO:0022857; GO:0042910; GO:0046677; GO:0055085; GO:1902599; GO:1990351; GO:1990961`

## Notes

Multidrug resistance protein MdtN
