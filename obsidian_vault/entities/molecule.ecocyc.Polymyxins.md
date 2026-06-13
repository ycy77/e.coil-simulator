---
entity_id: "molecule.ecocyc.Polymyxins"
entity_type: "small_molecule"
name: "a polymyxin"
source_database: "EcoCyc"
source_id: "Polymyxins"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/small_molecule
  - source/EcoCyc
aliases:
---

# a polymyxin

`molecule.ecocyc.Polymyxins`

## Static

- Type: `small_molecule`
- Source: `EcoCyc:Polymyxins`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

Polymyxins are antibiotics with a general structure consisting of a cyclic peptide with a long hydrophobic tail. They disrupt the structure of the bacterial cell membrane by interacting with its phospholipids. Polymyxins are produced by the Gram-positive bacterium TAX-1406 and are selectively toxic for Gram-negative bacteria due to their specificity for the lipopolysaccharide molecules that exist within many Gram-negative outer membranes. Polymyxins are antibiotics with a general structure consisting of a cyclic peptide with a long hydrophobic tail. They disrupt the structure of the bacterial cell membrane by interacting with its phospholipids. Polymyxins are produced by the Gram-positive bacterium TAX-1406 and are selectively toxic for Gram-negative bacteria due to their specificity for the lipopolysaccharide molecules that exist within many Gram-negative outer membranes.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Annotation

Polymyxins are antibiotics with a general structure consisting of a cyclic peptide with a long hydrophobic tail. They disrupt the structure of the bacterial cell membrane by interacting with its phospholipids. Polymyxins are produced by the Gram-positive bacterium TAX-1406 and are selectively toxic for Gram-negative bacteria due to their specificity for the lipopolysaccharide molecules that exist within many Gram-negative outer membranes.

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-378|reaction.ecocyc.TRANS-RXN-378]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-378|reaction.ecocyc.TRANS-RXN-378]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.TRANS-200-CPLX|complex.ecocyc.TRANS-200-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `EcoCyc:Polymyxins`
- `CHEBI:59062`
