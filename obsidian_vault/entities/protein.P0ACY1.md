---
entity_id: "protein.P0ACY1"
entity_type: "protein"
name: "ydjA"
source_database: "UniProt"
source_id: "P0ACY1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydjA b1765 JW1754"
---

# ydjA

`protein.P0ACY1`

## Static

- Type: `protein`
- Source: `UniProt:P0ACY1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Putative NAD(P)H nitroreductase YdjA (EC 1.-.-.-) Crystal structures of YdjA alone and with the FMN cofactor have been solved. The enzyme forms a homodimer in the crystal, and two molecules of FMN are bound at the dimer interface . Overexpressed YdjA does not appear to reduce the prodrugs CB1954 and PR-104A and was used by as a negative control for nitroreductase activity. A ydjA null mutant was reported to produce less hydrogen than wild type under fermentation conditions . No attempt to complement the mutant phenotype with wild-type ydjA was reported.

## Biological Role

Component of putative oxidoreductase YdjA (complex.ecocyc.CPLX0-7668).

## Annotation

Putative NAD(P)H nitroreductase YdjA (EC 1.-.-.-)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7668|complex.ecocyc.CPLX0-7668]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1765|gene.b1765]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACY1`
- `KEGG:ecj:JW1754;eco:b1765;ecoc:C3026_10075;`
- `GeneID:93775982;945964;`
- `GO:GO:0005829; GO:0010181; GO:0016491; GO:0042803`
- `EC:1.-.-.-`

## Notes

Putative NAD(P)H nitroreductase YdjA (EC 1.-.-.-)
