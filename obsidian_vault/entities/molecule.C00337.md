---
entity_id: "molecule.C00337"
entity_type: "small_molecule"
name: "(S)-Dihydroorotate"
source_database: "KEGG"
source_id: "C00337"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(S)-Dihydroorotate"
  - "(S)-4,5-Dihydroorotate"
  - "L-Dihydroorotate"
  - "L-Dihydroorotic acid"
  - "Dihydro-L-orotic acid"
---

# (S)-Dihydroorotate

`molecule.C00337`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00337`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (S)-Dihydroorotate; (S)-4,5-Dihydroorotate; L-Dihydroorotate; L-Dihydroorotic acid; Dihydro-L-orotic acid

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: (S)-Dihydroorotate; (S)-4,5-Dihydroorotate; L-Dihydroorotate; L-Dihydroorotic acid; Dihydro-L-orotic acid

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.RXN0-6490|reaction.ecocyc.RXN0-6490]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.DIHYDROOROT-RXN|reaction.ecocyc.DIHYDROOROT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.DIHYDROOROTATE-DEHYDROGENASE-RXN|reaction.ecocyc.DIHYDROOROTATE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6491|reaction.ecocyc.RXN0-6491]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6554|reaction.ecocyc.RXN0-6554]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00337`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
