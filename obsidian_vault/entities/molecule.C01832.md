---
entity_id: "molecule.C01832"
entity_type: "small_molecule"
name: "Lauroyl-CoA"
source_database: "KEGG"
source_id: "C01832"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Lauroyl-CoA"
  - "Lauroyl coenzyme A"
  - "Dodecanoyl-CoA"
---

# Lauroyl-CoA

`molecule.C01832`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01832`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Lauroyl-CoA; Lauroyl coenzyme A; Dodecanoyl-CoA EcoCyc common name: dodecanoyl-CoA.

## Biological Role

Produced in 1 reaction(s).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)

## Annotation

KEGG compound: Lauroyl-CoA; Lauroyl coenzyme A; Dodecanoyl-CoA

## Pathways

- `eco00071` Fatty acid degradation (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.RXN-16393|reaction.ecocyc.RXN-16393]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `represses` --> [[reaction.ecocyc.LAUROYLACYLTRAN-RXN|reaction.ecocyc.LAUROYLACYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01832`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
