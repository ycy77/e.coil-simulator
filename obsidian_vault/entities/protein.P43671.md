---
entity_id: "protein.P43671"
entity_type: "protein"
name: "pqiB"
source_database: "UniProt"
source_id: "P43671"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:28819315}; Single-pass membrane protein {ECO:0000255}; Periplasmic side {ECO:0000269|PubMed:27795327}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pqiB pqi5B b0951 JW0934"
---

# pqiB

`protein.P43671`

## Static

- Type: `protein`
- Source: `UniProt:P43671`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:28819315}; Single-pass membrane protein {ECO:0000255}; Periplasmic side {ECO:0000269|PubMed:27795327}.

## Enriched Summary

FUNCTION: Forms a tunnel that spans the entire periplasmic space (PubMed:28388411). Could be implicated in lipid transport between the inner membrane and the outer membrane (PubMed:28388411). Binds phospholipids (PubMed:28388411). Required for outer membrane homeostasis (PubMed:28819315). Contributes to membrane integrity (PubMed:27795327). {ECO:0000269|PubMed:27795327, ECO:0000269|PubMed:28388411, ECO:0000269|PubMed:28819315}.

## Biological Role

Component of intermembrane transport protein PqiB (complex.ecocyc.CPLX0-8244).

## Annotation

FUNCTION: Forms a tunnel that spans the entire periplasmic space (PubMed:28388411). Could be implicated in lipid transport between the inner membrane and the outer membrane (PubMed:28388411). Binds phospholipids (PubMed:28388411). Required for outer membrane homeostasis (PubMed:28819315). Contributes to membrane integrity (PubMed:27795327). {ECO:0000269|PubMed:27795327, ECO:0000269|PubMed:28388411, ECO:0000269|PubMed:28819315}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8244|complex.ecocyc.CPLX0-8244]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0951|gene.b0951]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P43671`
- `KEGG:ecj:JW0934;eco:b0951;ecoc:C3026_05820;`
- `GeneID:75204042;945653;`
- `GO:GO:0005886; GO:0030288; GO:0042802; GO:0061024; GO:0120009`

## Notes

Intermembrane transport protein PqiB (Paraquat-inducible protein B)
