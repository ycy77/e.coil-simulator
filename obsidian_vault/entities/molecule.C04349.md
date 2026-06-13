---
entity_id: "molecule.C04349"
entity_type: "small_molecule"
name: "(4S)-4,6-Dihydroxy-2,5-dioxohexanoate"
source_database: "KEGG"
source_id: "C04349"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(4S)-4,6-Dihydroxy-2,5-dioxohexanoate"
  - "3-Deoxy-D-glycero-2,5-hexodiulosonate"
  - "2,5-Diketo-3-deoxy-D-gluconate"
  - "3-Deoxy-D-glycero-hexo-2,5-diulosonic acid"
---

# (4S)-4,6-Dihydroxy-2,5-dioxohexanoate

`molecule.C04349`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04349`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (4S)-4,6-Dihydroxy-2,5-dioxohexanoate; 3-Deoxy-D-glycero-2,5-hexodiulosonate; 2,5-Diketo-3-deoxy-D-gluconate; 3-Deoxy-D-glycero-hexo-2,5-diulosonic acid EcoCyc common name: 3-deoxy-D-glycero-2,5-hexodiulosonate.

## Biological Role

Produced in 4 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Annotation

KEGG compound: (4S)-4,6-Dihydroxy-2,5-dioxohexanoate; 3-Deoxy-D-glycero-2,5-hexodiulosonate; 2,5-Diketo-3-deoxy-D-gluconate; 3-Deoxy-D-glycero-hexo-2,5-diulosonic acid

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R01542|reaction.R01542]] `KEGG` `database` - C00204 + C00003 <=> C04349 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.1.1.1.127-RXN|reaction.ecocyc.1.1.1.127-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.5.3.1.17-RXN|reaction.ecocyc.5.3.1.17-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16964|reaction.ecocyc.RXN-16964]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04349`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
