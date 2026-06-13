---
entity_id: "molecule.C00383"
entity_type: "small_molecule"
name: "Malonate"
source_database: "KEGG"
source_id: "C00383"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Malonate"
  - "Malonic acid"
  - "Propanedioic acid"
---

# Malonate

`molecule.C00383`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00383`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Malonate; Malonic acid; Propanedioic acid MALONATE Malonate is found in small amounts in plants and is produced by some bacteria . However, most of the malonate in the environment comes from industrial production. The dimethyl and diethyl forms, in particularly, are produced at more than 12,000 tons per year (1995) .

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)

## Annotation

KEGG compound: Malonate; Malonic acid; Propanedioic acid

## Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)

## Outgoing Edges (4)

- `represses` --> [[reaction.ecocyc.GLUTDECARBOX-RXN|reaction.ecocyc.GLUTDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ISOCIT-CLEAV-RXN|reaction.ecocyc.ISOCIT-CLEAV-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.R601-RXN|reaction.ecocyc.R601-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN|reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00383`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
