---
entity_id: "molecule.C04225"
entity_type: "small_molecule"
name: "(Z)-But-2-ene-1,2,3-tricarboxylate"
source_database: "KEGG"
source_id: "C04225"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(Z)-But-2-ene-1,2,3-tricarboxylate"
  - "cis-2-Methylaconitate"
---

# (Z)-But-2-ene-1,2,3-tricarboxylate

`molecule.C04225`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04225`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (Z)-But-2-ene-1,2,3-tricarboxylate; cis-2-Methylaconitate EcoCyc common name: (Z)-2-methylaconitate.

## Biological Role

Produced in 4 reaction(s).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)

## Annotation

KEGG compound: (Z)-But-2-ene-1,2,3-tricarboxylate; cis-2-Methylaconitate

## Pathways

- `eco00640` Propanoate metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R04424|reaction.R04424]] `KEGG` `database` - C02225 <=> C04225 + C00001
- `is_product_of` --> [[reaction.R04425|reaction.R04425]] `KEGG` `database` - C04593 <=> C04225 + C00001
- `is_product_of` --> [[reaction.ecocyc.2-METHYLCITRATE-DEHYDRATASE-RXN|reaction.ecocyc.2-METHYLCITRATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.4.2.1.99-RXN|reaction.ecocyc.4.2.1.99-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04225`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
