---
entity_id: "molecule.ecocyc.Peptide-Antibiotics"
entity_type: "small_molecule"
name: "a peptide antibiotic"
source_database: "EcoCyc"
source_id: "Peptide-Antibiotics"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
  - "Peptide Antibiotic"
---

# a peptide antibiotic

`molecule.ecocyc.Peptide-Antibiotics`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Peptide-Antibiotics`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

This compound class stands for generic and unspecified peptide antibiotics. This compound class stands for generic and unspecified peptide antibiotics.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Annotation

This compound class stands for generic and unspecified peptide antibiotics.

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-205A|reaction.ecocyc.TRANS-RXN-205A]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-205A|reaction.ecocyc.TRANS-RXN-205A]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.CPLX0-8097|complex.ecocyc.CPLX0-8097]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:Peptide-Antibiotics`
