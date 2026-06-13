---
entity_id: "molecule.C03794"
entity_type: "small_molecule"
name: "N6-(1,2-Dicarboxyethyl)-AMP"
source_database: "KEGG"
source_id: "C03794"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N6-(1,2-Dicarboxyethyl)-AMP"
  - "N6-(1,2-Dicarboxyethyl)AMP"
  - "Adenylosuccinate"
  - "Adenylosuccinic acid"
---

# N6-(1,2-Dicarboxyethyl)-AMP

`molecule.C03794`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03794`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N6-(1,2-Dicarboxyethyl)-AMP; N6-(1,2-Dicarboxyethyl)AMP; Adenylosuccinate; Adenylosuccinic acid EcoCyc common name: adenylosuccinate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)

## Annotation

KEGG compound: N6-(1,2-Dicarboxyethyl)-AMP; N6-(1,2-Dicarboxyethyl)AMP; Adenylosuccinate; Adenylosuccinic acid

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R01135|reaction.R01135]] `KEGG` `database` - C00044 + C00130 + C00049 <=> C00035 + C00009 + C03794
- `is_product_of` --> [[reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN|reaction.ecocyc.ADENYLOSUCCINATE-SYNTHASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.AMPSYN-RXN|reaction.ecocyc.AMPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03794`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
