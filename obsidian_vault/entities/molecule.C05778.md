---
entity_id: "molecule.C05778"
entity_type: "small_molecule"
name: "Sirohydrochlorin"
source_database: "KEGG"
source_id: "C05778"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Sirohydrochlorin"
---

# Sirohydrochlorin

`molecule.C05778`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05778`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Sirohydrochlorin

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Annotation

KEGG compound: Sirohydrochlorin

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R02864|reaction.R02864]] `KEGG` `database` - C00748 + 2 C00080 <=> C14818 + C05778
- `is_product_of` --> [[reaction.ecocyc.DIMETHUROPORDEHYDROG-RXN|reaction.ecocyc.DIMETHUROPORDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.SIROHEME-FERROCHELAT-RXN|reaction.ecocyc.SIROHEME-FERROCHELAT-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05778`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
