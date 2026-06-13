---
entity_id: "molecule.C01825"
entity_type: "small_molecule"
name: "L-Galactose"
source_database: "KEGG"
source_id: "C01825"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Galactose"
---

# L-Galactose

`molecule.C01825`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01825`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Galactose EcoCyc common name: L-galactopyranose. This compound stands for a mixture of CPD-13428 and CPD-25003. In most cases, each of these compounds mutarotates quickly to form a mixture of the two, and thus it is the general rule to use this non-specific form in reactions unless it is specifically known that an enzyme can accept only one of the forms.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Annotation

KEGG compound: L-Galactose

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.RXN0-7222|reaction.ecocyc.RXN0-7222]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7222|reaction.ecocyc.RXN0-7222]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P11551|protein.P11551]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C01825`
- `EcoCyc:L-Galactose`
- `CHEBI:37618`
- `canonicalized_from:molecule.ecocyc.L-Galactose`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.L-Galactose: EcoCyc:L-Galactose
