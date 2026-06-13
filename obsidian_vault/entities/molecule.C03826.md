---
entity_id: "molecule.C03826"
entity_type: "small_molecule"
name: "2-Dehydro-3-deoxy-D-xylonate"
source_database: "KEGG"
source_id: "C03826"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Dehydro-3-deoxy-D-xylonate"
  - "2-Dehydro-3-deoxy-D-arabinonate"
  - "2-Dehydro-3-deoxy-D-pentonate"
  - "(4S)-4,5-Dihydroxy-2-oxopentanoate"
  - "2-Dehydro-3-deoxy-D-arabinonic acid"
---

# 2-Dehydro-3-deoxy-D-xylonate

`molecule.C03826`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03826`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Dehydro-3-deoxy-D-xylonate; 2-Dehydro-3-deoxy-D-arabinonate; 2-Dehydro-3-deoxy-D-pentonate; (4S)-4,5-Dihydroxy-2-oxopentanoate; 2-Dehydro-3-deoxy-D-arabinonic acid EcoCyc common name: 2-dehydro-3-deoxy-D-pentonate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Annotation

KEGG compound: 2-Dehydro-3-deoxy-D-xylonate; 2-Dehydro-3-deoxy-D-arabinonate; 2-Dehydro-3-deoxy-D-pentonate; (4S)-4,5-Dihydroxy-2-oxopentanoate; 2-Dehydro-3-deoxy-D-arabinonic acid

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.XYLONATE-DEHYDRATASE-RXN|reaction.ecocyc.XYLONATE-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.4.1.2.28-RXN|reaction.ecocyc.4.1.2.28-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8777|reaction.ecocyc.RXN-8777]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03826`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
