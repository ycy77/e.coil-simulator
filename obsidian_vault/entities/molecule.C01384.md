---
entity_id: "molecule.C01384"
entity_type: "small_molecule"
name: "Maleic acid"
source_database: "KEGG"
source_id: "C01384"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Maleic acid"
  - "Maleate"
  - "cis-Butenedioic acid"
---

# Maleic acid

`molecule.C01384`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01384`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Maleic acid; Maleate; cis-Butenedioic acid EcoCyc common name: maleate.

## Enriched Pathways

- `eco00350` Tyrosine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Annotation

KEGG compound: Maleic acid; Maleate; cis-Butenedioic acid

## Pathways

- `eco00350` Tyrosine metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Outgoing Edges (5)

- `represses` --> [[reaction.ecocyc.ASPAMINOTRANS-RXN|reaction.ecocyc.ASPAMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLUTDECARBOX-RXN|reaction.ecocyc.GLUTDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-10814|reaction.ecocyc.RXN-10814]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-21858|reaction.ecocyc.RXN-21858]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.SAICARSYN-RXN|reaction.ecocyc.SAICARSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01384`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
