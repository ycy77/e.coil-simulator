---
entity_id: "molecule.C05730"
entity_type: "small_molecule"
name: "Glutathionylspermidine"
source_database: "KEGG"
source_id: "C05730"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Glutathionylspermidine"
  - "N1-(gamma-L-Glutamyl-L-cysteinyl-glycyl)-spermidine"
---

# Glutathionylspermidine

`molecule.C05730`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05730`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Glutathionylspermidine; N1-(gamma-L-Glutamyl-L-cysteinyl-glycyl)-spermidine

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)

## Annotation

KEGG compound: Glutathionylspermidine; N1-(gamma-L-Glutamyl-L-cysteinyl-glycyl)-spermidine

## Pathways

- `eco00480` Glutathione metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.GSPSYN-RXN|reaction.ecocyc.GSPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GSPAMID-RXN|reaction.ecocyc.GSPAMID-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05730`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
