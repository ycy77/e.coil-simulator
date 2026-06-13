---
entity_id: "molecule.C00415"
entity_type: "small_molecule"
name: "Dihydrofolate"
source_database: "KEGG"
source_id: "C00415"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Dihydrofolate"
  - "Dihydrofolic acid"
  - "7,8-Dihydrofolate"
  - "7,8-Dihydrofolic acid"
  - "7,8-Dihydropteroylglutamate"
---

# Dihydrofolate

`molecule.C00415`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00415`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Dihydrofolate; Dihydrofolic acid; 7,8-Dihydrofolate; 7,8-Dihydrofolic acid; 7,8-Dihydropteroylglutamate EcoCyc common name: 7,8-dihydrofolate monoglutamate.

## Biological Role

Produced in 2 reaction(s).

## Enriched Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

KEGG compound: Dihydrofolate; Dihydrofolic acid; 7,8-Dihydrofolate; 7,8-Dihydrofolic acid; 7,8-Dihydropteroylglutamate

## Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.DIHYDROFOLATESYNTH-RXN|reaction.ecocyc.DIHYDROFOLATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19329|reaction.ecocyc.RXN-19329]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `represses` --> [[reaction.ecocyc.DIHYDROFOLATESYNTH-RXN|reaction.ecocyc.DIHYDROFOLATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN|reaction.ecocyc.FOLYLPOLYGLUTAMATESYNTH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00415`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
