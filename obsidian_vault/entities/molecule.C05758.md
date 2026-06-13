---
entity_id: "molecule.C05758"
entity_type: "small_molecule"
name: "trans-Dodec-2-enoyl-[acp]"
source_database: "KEGG"
source_id: "C05758"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "trans-Dodec-2-enoyl-[acp]"
  - "trans-Dodec-2-enoyl-[acyl-carrier protein]"
  - "(2E)-Dodecenoyl-[acp]"
---

# trans-Dodec-2-enoyl-[acp]

`molecule.C05758`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05758`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: trans-Dodec-2-enoyl-[acp]; trans-Dodec-2-enoyl-[acyl-carrier protein]; (2E)-Dodecenoyl-[acp]

## Biological Role

Produced in 3 reaction(s).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Annotation

KEGG compound: trans-Dodec-2-enoyl-[acp]; trans-Dodec-2-enoyl-[acyl-carrier protein]; (2E)-Dodecenoyl-[acp]

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R04724|reaction.R04724]] `KEGG` `database` - C05223 + C00003 <=> C05758 + C00004 + C00080
- `is_product_of` --> [[reaction.R04725|reaction.R04725]] `KEGG` `database` - C05223 + C00006 <=> C05758 + C00005 + C00080
- `is_product_of` --> [[reaction.R04965|reaction.R04965]] `KEGG` `database` - C05757 <=> C05758 + C00001

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05758`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
