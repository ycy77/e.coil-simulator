---
entity_id: "reaction.R04125"
entity_type: "reaction"
name: "[protein]-S8-aminomethyldihydrolipoyllysine:tetrahydrofolate aminomethyltransferase (ammonia-forming)"
source_database: "KEGG"
source_id: "R04125"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04125"
---

# [protein]-S8-aminomethyldihydrolipoyllysine:tetrahydrofolate aminomethyltransferase (ammonia-forming)

`reaction.R04125`

## Static

- Type: `reaction`
- Source: `KEGG:R04125`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

[Protein]-S8-aminomethyldihydrolipoyllysine + Tetrahydrofolate Dihydrolipoylprotein + 5,10-Methylenetetrahydrofolate + Ammonia

## Biological Role

Catalyzed by gcvT (protein.P27248). Substrates: Tetrahydrofolate (molecule.C00101), [Protein]-S8-aminomethyldihydrolipoyllysine (molecule.C01242). Products: Ammonia (molecule.C00014), 5,10-Methylenetetrahydrofolate (molecule.C00143), Dihydrolipoylprotein (molecule.C02972).

## Annotation

[Protein]-S8-aminomethyldihydrolipoyllysine + Tetrahydrofolate <=> Dihydrolipoylprotein + 5,10-Methylenetetrahydrofolate + Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P27248|protein.P27248]] `KEGG` `database` - via EC:2.1.2.10
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - C01242 + C00101 <=> C02972 + C00143 + C00014
- `is_product_of` <-- [[molecule.C00143|molecule.C00143]] `KEGG` `database` - C01242 + C00101 <=> C02972 + C00143 + C00014
- `is_product_of` <-- [[molecule.C02972|molecule.C02972]] `KEGG` `database` - C01242 + C00101 <=> C02972 + C00143 + C00014
- `is_substrate_of` <-- [[molecule.C00101|molecule.C00101]] `KEGG` `database` - C01242 + C00101 <=> C02972 + C00143 + C00014
- `is_substrate_of` <-- [[molecule.C01242|molecule.C01242]] `KEGG` `database` - C01242 + C00101 <=> C02972 + C00143 + C00014

## External IDs

- `KEGG:R04125`

## Notes

EQUATION: C01242 + C00101 <=> C02972 + C00143 + C00014
