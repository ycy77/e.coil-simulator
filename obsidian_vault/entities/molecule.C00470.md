---
entity_id: "molecule.C00470"
entity_type: "small_molecule"
name: "Pectate"
source_database: "KEGG"
source_id: "C00470"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Pectate"
  - "Pectic acid"
  - "alpha-D-Polygalacturonic acid"
  - "Poly(1,4-alpha-D-galacturonate)"
  - "Poly(1,4-alpha-D-galacturonate)(n)"
  - "(1,4-alpha-D-Galacturonide)n"
  - "[(1->4)-alpha-D-Galacturonosyl]n"
  - "De-esterified pectin"
  - "(1,4-alpha-D-Galacturonosyl)n"
---

# Pectate

`molecule.C00470`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00470`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Pectate; Pectic acid; alpha-D-Polygalacturonic acid; Poly(1,4-alpha-D-galacturonate); Poly(1,4-alpha-D-galacturonate)(n); (1,4-alpha-D-Galacturonide)n; [(1->4)-alpha-D-Galacturonosyl]n; De-esterified pectin; (1,4-alpha-D-Galacturonosyl)n EcoCyc common name: α-D-galacturonate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Pectate; Pectic acid; alpha-D-Polygalacturonic acid; Poly(1,4-alpha-D-galacturonate); Poly(1,4-alpha-D-galacturonate)(n); (1,4-alpha-D-Galacturonide)n; [(1->4)-alpha-D-Galacturonosyl]n; De-esterified pectin; (1,4-alpha-D-Galacturonosyl)n

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8209|complex.ecocyc.CPLX0-8209]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-8210|complex.ecocyc.CPLX0-8210]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R02362|reaction.R02362]] `KEGG` `database` - C00714 + n C00001 <=> n C00132 + C00470
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7171|reaction.ecocyc.RXN0-7171]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7172|reaction.ecocyc.RXN0-7172]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00470`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
