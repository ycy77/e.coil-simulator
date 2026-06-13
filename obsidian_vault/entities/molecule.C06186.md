---
entity_id: "molecule.C06186"
entity_type: "small_molecule"
name: "Arbutin"
source_database: "KEGG"
source_id: "C06186"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Arbutin"
  - "Ursin"
  - "Uvasol"
  - "Hydroquinone-O-beta-D-glucopyranoside"
---

# Arbutin

`molecule.C06186`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06186`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Arbutin; Ursin; Uvasol; Hydroquinone-O-beta-D-glucopyranoside

## Biological Role

Consumed as substrate in 1 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: Arbutin; Ursin; Uvasol; Hydroquinone-O-beta-D-glucopyranoside

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-153|reaction.ecocyc.TRANS-RXN-153]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.CPLX-154|complex.ecocyc.CPLX-154]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C06186`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
