---
entity_id: "molecule.C03619"
entity_type: "small_molecule"
name: "Methyl beta-D-galactoside"
source_database: "KEGG"
source_id: "C03619"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Methyl beta-D-galactoside"
  - "Methyl beta-D-galactopyranoside"
---

# Methyl beta-D-galactoside

`molecule.C03619`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03619`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Methyl beta-D-galactoside; Methyl beta-D-galactopyranoside EcoCyc common name: methyl-β-D-galactoside.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Methyl beta-D-galactoside; Methyl beta-D-galactopyranoside

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-520|reaction.ecocyc.TRANS-RXN0-520]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-541|reaction.ecocyc.TRANS-RXN0-541]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-520|reaction.ecocyc.TRANS-RXN0-520]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-541|reaction.ecocyc.TRANS-RXN0-541]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-18-CPLX|complex.ecocyc.ABC-18-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P02921|protein.P02921]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C03619`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
