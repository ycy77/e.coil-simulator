---
entity_id: "reaction.R00839"
entity_type: "reaction"
name: "6-phospho-beta-D-glucosyl-(1->4)-D-glucose 6-phosphoglucohydrolase"
source_database: "KEGG"
source_id: "R00839"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00839"
---

# 6-phospho-beta-D-glucosyl-(1->4)-D-glucose 6-phosphoglucohydrolase

`reaction.R00839`

## Static

- Type: `reaction`
- Source: `KEGG:R00839`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

6-Phospho-beta-D-glucosyl-(1,4)-D-glucose + H2O D-Glucose + D-Glucose 6-phosphate

## Biological Role

Catalyzed by bglB (protein.P11988), chbF (protein.P17411), ascB (protein.P24240), bglA (protein.Q46829). Substrates: H2O (molecule.C00001), 6-Phospho-beta-D-glucosyl-(1,4)-D-glucose (molecule.C04534). Products: D-Glucose (molecule.C00031), D-Glucose 6-phosphate (molecule.C00092).

## Annotation

6-Phospho-beta-D-glucosyl-(1,4)-D-glucose + H2O <=> D-Glucose + D-Glucose 6-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P11988|protein.P11988]] `KEGG` `database` - via EC:3.2.1.86
- `catalyzes` <-- [[protein.P17411|protein.P17411]] `KEGG` `database` - via EC:3.2.1.86
- `catalyzes` <-- [[protein.P24240|protein.P24240]] `KEGG` `database` - via EC:3.2.1.86
- `catalyzes` <-- [[protein.Q46829|protein.Q46829]] `KEGG` `database` - via EC:3.2.1.86
- `is_product_of` <-- [[molecule.C00031|molecule.C00031]] `KEGG` `database` - C04534 + C00001 <=> C00031 + C00092
- `is_product_of` <-- [[molecule.C00092|molecule.C00092]] `KEGG` `database` - C04534 + C00001 <=> C00031 + C00092
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C04534 + C00001 <=> C00031 + C00092
- `is_substrate_of` <-- [[molecule.C04534|molecule.C04534]] `KEGG` `database` - C04534 + C00001 <=> C00031 + C00092

## External IDs

- `KEGG:R00839`

## Notes

EQUATION: C04534 + C00001 <=> C00031 + C00092
