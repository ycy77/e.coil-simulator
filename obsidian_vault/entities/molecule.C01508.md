---
entity_id: "molecule.C01508"
entity_type: "small_molecule"
name: "L-Lyxose"
source_database: "KEGG"
source_id: "C01508"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Lyxose"
---

# L-Lyxose

`molecule.C01508`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01508`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Lyxose EcoCyc common name: L-lyxopyranose. This compound stands for a mixture of CPD-11897 and L-LYXOSE. In most cases, each of these compounds mutarotates quickly to form a mixture of the two, and thus it is the general rule to use this non-specific form in reactions unless it is specifically known that an enzyme can accept only one of the forms.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Annotation

KEGG compound: L-Lyxose

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-236|reaction.ecocyc.TRANS-RXN0-236]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14968|reaction.ecocyc.RXN-14968]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-236|reaction.ecocyc.TRANS-RXN0-236]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[protein.P27125|protein.P27125]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C01508`
- `EcoCyc:L-Lyxose`
- `CHEBI:62320`
- `canonicalized_from:molecule.ecocyc.L-Lyxose`

## Notes

Included because it appears in at least one E. coli KEGG pathway. | molecule.ecocyc.L-Lyxose: EcoCyc:L-Lyxose
