---
entity_id: "reaction.R10906"
entity_type: "reaction"
name: "(9Z)-hexadec-9-enoyl-[acyl-carrier protein]:KDO2-lipid IVA O-palmitoleoyltransferase"
source_database: "KEGG"
source_id: "R10906"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10906"
---

# (9Z)-hexadec-9-enoyl-[acyl-carrier protein]:KDO2-lipid IVA O-palmitoleoyltransferase

`reaction.R10906`

## Static

- Type: `reaction`
- Source: `KEGG:R10906`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Hexadecenoyl-[acyl-carrier protein] + KDO2-lipid IVA (9Z)-Hexadec-9-enoyl-KDO2-lipid IV(A) + Acyl-carrier protein

## Biological Role

Catalyzed by lpxP (protein.P0ACV2). Substrates: KDO2-lipid IVA (molecule.C06025), Hexadecenoyl-[acyl-carrier protein] (molecule.C16520). Products: Acyl-carrier protein (molecule.C00229), (9Z)-Hexadec-9-enoyl-KDO2-lipid IV(A) (molecule.C20933).

## Annotation

Hexadecenoyl-[acyl-carrier protein] + KDO2-lipid IVA <=> (9Z)-Hexadec-9-enoyl-KDO2-lipid IV(A) + Acyl-carrier protein

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0ACV2|protein.P0ACV2]] `KEGG` `database` - via EC:2.3.1.242
- `is_product_of` <-- [[molecule.C00229|molecule.C00229]] `KEGG` `database` - C16520 + C06025 <=> C20933 + C00229
- `is_product_of` <-- [[molecule.C20933|molecule.C20933]] `KEGG` `database` - C16520 + C06025 <=> C20933 + C00229
- `is_substrate_of` <-- [[molecule.C06025|molecule.C06025]] `KEGG` `database` - C16520 + C06025 <=> C20933 + C00229
- `is_substrate_of` <-- [[molecule.C16520|molecule.C16520]] `KEGG` `database` - C16520 + C06025 <=> C20933 + C00229

## External IDs

- `KEGG:R10906`

## Notes

EQUATION: C16520 + C06025 <=> C20933 + C00229
