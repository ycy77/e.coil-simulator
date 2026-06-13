---
entity_id: "molecule.C00379"
entity_type: "small_molecule"
name: "Xylitol"
source_database: "KEGG"
source_id: "C00379"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Xylitol"
---

# Xylitol

`molecule.C00379`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00379`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Xylitol XYLITOL Xylitol is a naturally occurring pentitol sugar alcohol. It is found in low concentrations in the fibers of many fruits and vegetables, and can be extracted from various berries, oats, and mushrooms, as well as fibrous material such as corn husks, sugar cane bagasse and birch . Xylitol is roughly as sweet as sucrose, and is used as a diabetic sweetener. Since it is symmetrical, there are no D or L forms of xylitol.

## Biological Role

Consumed as substrate in 3 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Xylitol

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (3)

- `is_substrate_of` --> [[reaction.R01896|reaction.R01896]] `KEGG` `database` - C00379 + C00003 <=> C00310 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.D-XYLULOSE-REDUCTASE-RXN|reaction.ecocyc.D-XYLULOSE-REDUCTASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8773|reaction.ecocyc.RXN-8773]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00379`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
