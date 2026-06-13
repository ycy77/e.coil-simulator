---
entity_id: "reaction.R02889"
entity_type: "reaction"
name: "UDPglucose:1,4-beta-D-glucan 4-beta-D-glucosyltransferase"
source_database: "KEGG"
source_id: "R02889"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02889"
---

# UDPglucose:1,4-beta-D-glucan 4-beta-D-glucosyltransferase

`reaction.R02889`

## Static

- Type: `reaction`
- Source: `KEGG:R02889`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-glucose + Cellulose UDP + Cellulose

## Biological Role

Catalyzed by bcsA (protein.P37653). Substrates: UDP-glucose (molecule.C00029), Cellulose (molecule.C00760). Products: UDP (molecule.C00015), Cellulose (molecule.C00760).

## Annotation

UDP-glucose + Cellulose <=> UDP + Cellulose

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P37653|protein.P37653]] `KEGG` `database` - via EC:2.4.1.12
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `KEGG` `database` - C00029 + C00760 <=> C00015 + C00760
- `is_product_of` <-- [[molecule.C00760|molecule.C00760]] `KEGG` `database` - C00029 + C00760 <=> C00015 + C00760
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `KEGG` `database` - C00029 + C00760 <=> C00015 + C00760
- `is_substrate_of` <-- [[molecule.C00760|molecule.C00760]] `KEGG` `database` - C00029 + C00760 <=> C00015 + C00760

## External IDs

- `KEGG:R02889`

## Notes

EQUATION: C00029 + C00760 <=> C00015 + C00760
