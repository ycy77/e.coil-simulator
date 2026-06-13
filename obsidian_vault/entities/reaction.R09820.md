---
entity_id: "reaction.R09820"
entity_type: "reaction"
name: "3-oxo-5,6-dehydrosuberyl-CoA semialdehyde:NADP+ oxidoreductase"
source_database: "KEGG"
source_id: "R09820"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09820"
---

# 3-oxo-5,6-dehydrosuberyl-CoA semialdehyde:NADP+ oxidoreductase

`reaction.R09820`

## Static

- Type: `reaction`
- Source: `KEGG:R09820`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-Oxo-5,6-dehydrosuberyl-CoA semialdehyde + NADP+ + H2O 3-Oxo-5,6-dehydrosuberyl-CoA + NADPH + H+

## Biological Role

Catalyzed by paaZ (protein.P77455). Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), 3-Oxo-5,6-dehydrosuberyl-CoA semialdehyde (molecule.C19946). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 3-Oxo-5,6-dehydrosuberyl-CoA (molecule.C19945).

## Annotation

3-Oxo-5,6-dehydrosuberyl-CoA semialdehyde + NADP+ + H2O <=> 3-Oxo-5,6-dehydrosuberyl-CoA + NADPH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P77455|protein.P77455]] `KEGG` `database` - via EC:1.2.1.91
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `KEGG` `database` - C19946 + C00006 + C00001 <=> C19945 + C00005 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C19946 + C00006 + C00001 <=> C19945 + C00005 + C00080
- `is_product_of` <-- [[molecule.C19945|molecule.C19945]] `KEGG` `database` - C19946 + C00006 + C00001 <=> C19945 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C19946 + C00006 + C00001 <=> C19945 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `KEGG` `database` - C19946 + C00006 + C00001 <=> C19945 + C00005 + C00080
- `is_substrate_of` <-- [[molecule.C19946|molecule.C19946]] `KEGG` `database` - C19946 + C00006 + C00001 <=> C19945 + C00005 + C00080

## External IDs

- `KEGG:R09820`

## Notes

EQUATION: C19946 + C00006 + C00001 <=> C19945 + C00005 + C00080
