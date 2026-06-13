---
entity_id: "molecule.C02679"
entity_type: "small_molecule"
name: "Dodecanoic acid"
source_database: "KEGG"
source_id: "C02679"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dodecanoic acid"
  - "Dodecanoate"
  - "Dodecylcarboxylate"
  - "Lauric acid"
---

# Dodecanoic acid

`molecule.C02679`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02679`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dodecanoic acid; Dodecanoate; Dodecylcarboxylate; Lauric acid EcoCyc common name: dodecanoate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Annotation

KEGG compound: Dodecanoic acid; Dodecanoate; Dodecylcarboxylate; Lauric acid

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Outgoing Edges (3)

- `activates` --> [[reaction.ecocyc.PEPCARBOX-RXN|reaction.ecocyc.PEPCARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.3.1.2.21-RXN|reaction.ecocyc.3.1.2.21-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16393|reaction.ecocyc.RXN-16393]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02679`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
