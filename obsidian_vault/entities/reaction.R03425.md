---
entity_id: "reaction.R03425"
entity_type: "reaction"
name: "glycine:lipoylprotein oxidoreductase (decarboxylating and acceptor-aminomethylating)"
source_database: "KEGG"
source_id: "R03425"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03425"
---

# glycine:lipoylprotein oxidoreductase (decarboxylating and acceptor-aminomethylating)

`reaction.R03425`

## Static

- Type: `reaction`
- Source: `KEGG:R03425`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Glycine + Lipoylprotein [Protein]-S8-aminomethyldihydrolipoyllysine + CO2

## Biological Role

Catalyzed by gcvP (protein.P33195). Substrates: Glycine (molecule.C00037), Lipoylprotein (molecule.C02051). Products: CO2 (molecule.C00011), [Protein]-S8-aminomethyldihydrolipoyllysine (molecule.C01242).

## Annotation

Glycine + Lipoylprotein <=> [Protein]-S8-aminomethyldihydrolipoyllysine + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P33195|protein.P33195]] `KEGG` `database` - via EC:1.4.4.2
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00037 + C02051 <=> C01242 + C00011
- `is_product_of` <-- [[molecule.C01242|molecule.C01242]] `KEGG` `database` - C00037 + C02051 <=> C01242 + C00011
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `KEGG` `database` - C00037 + C02051 <=> C01242 + C00011
- `is_substrate_of` <-- [[molecule.C02051|molecule.C02051]] `KEGG` `database` - C00037 + C02051 <=> C01242 + C00011

## External IDs

- `KEGG:R03425`

## Notes

EQUATION: C00037 + C02051 <=> C01242 + C00011
