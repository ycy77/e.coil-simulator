---
entity_id: "protein.P0AAT4"
entity_type: "protein"
name: "ybdG"
source_database: "UniProt"
source_id: "P0AAT4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:20616037, ECO:0000269|PubMed:31256002}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybdG mscM b0577 JW0566"
---

# ybdG

`protein.P0AAT4`

## Static

- Type: `protein`
- Source: `UniProt:P0AAT4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:20616037, ECO:0000269|PubMed:31256002}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Functions as a component of a mechanosensing system that transmits signals triggered by external osmotic changes to intracellular factors (PubMed:31256002). Probably plays a crucial role in cellular protection against high osmotic pressure (PubMed:31256002). Also confers protection against mild hypoosmotic shock (PubMed:20616037). Overexpression confers protection against severe shocks (PubMed:20616037). Lacks measurable transport activity (PubMed:20616037, PubMed:31256002). {ECO:0000269|PubMed:20616037, ECO:0000269|PubMed:31256002}.

## Biological Role

Component of miniconductance mechanosensitive channel YbdG (complex.ecocyc.CPLX0-7981).

## Annotation

FUNCTION: Functions as a component of a mechanosensing system that transmits signals triggered by external osmotic changes to intracellular factors (PubMed:31256002). Probably plays a crucial role in cellular protection against high osmotic pressure (PubMed:31256002). Also confers protection against mild hypoosmotic shock (PubMed:20616037). Overexpression confers protection against severe shocks (PubMed:20616037). Lacks measurable transport activity (PubMed:20616037, PubMed:31256002). {ECO:0000269|PubMed:20616037, ECO:0000269|PubMed:31256002}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7981|complex.ecocyc.CPLX0-7981]] `EcoCyc` `database` - EcoCyc component coefficient=7 | EcoCyc protcplxs.col coefficient=7

## Incoming Edges (1)

- `encodes` <-- [[gene.b0577|gene.b0577]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAT4`
- `KEGG:ecj:JW0566;eco:b0577;ecoc:C3026_02865;`
- `GeneID:93776911;946243;`
- `GO:GO:0005886; GO:0006970; GO:0008381; GO:0042802; GO:0071470`

## Notes

Mechanosensing system component YbdG (Mechanosensitive channel homolog YbdG)
