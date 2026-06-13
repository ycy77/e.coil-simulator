---
entity_id: "reaction.R00084"
entity_type: "reaction"
name: "porphobilinogen:(4-[2-carboxyethyl]-3-[carboxymethyl]pyrrol-2-yl)methyltransferase (hydrolysing);"
source_database: "KEGG"
source_id: "R00084"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00084"
---

# porphobilinogen:(4-[2-carboxyethyl]-3-[carboxymethyl]pyrrol-2-yl)methyltransferase (hydrolysing);

`reaction.R00084`

## Static

- Type: `reaction`
- Source: `KEGG:R00084`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

4 Porphobilinogen + H2O Hydroxymethylbilane + 4 Ammonia

## Biological Role

Catalyzed by hemC (protein.P06983). Substrates: H2O (molecule.C00001), Porphobilinogen (molecule.C00931). Products: Ammonia (molecule.C00014), Hydroxymethylbilane (molecule.C01024).

## Annotation

4 Porphobilinogen + H2O <=> Hydroxymethylbilane + 4 Ammonia

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P06983|protein.P06983]] `KEGG` `database` - via EC:2.5.1.61
- `is_product_of` <-- [[molecule.C00014|molecule.C00014]] `KEGG` `database` - 4 C00931 + C00001 <=> C01024 + 4 C00014
- `is_product_of` <-- [[molecule.C01024|molecule.C01024]] `KEGG` `database` - 4 C00931 + C00001 <=> C01024 + 4 C00014
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - 4 C00931 + C00001 <=> C01024 + 4 C00014
- `is_substrate_of` <-- [[molecule.C00931|molecule.C00931]] `KEGG` `database` - 4 C00931 + C00001 <=> C01024 + 4 C00014

## External IDs

- `KEGG:R00084`

## Notes

EQUATION: 4 C00931 + C00001 <=> C01024 + 4 C00014
