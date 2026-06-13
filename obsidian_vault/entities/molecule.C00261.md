---
entity_id: "molecule.C00261"
entity_type: "small_molecule"
name: "Benzaldehyde"
source_database: "KEGG"
source_id: "C00261"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Benzaldehyde"
  - "Benzoic aldehyde"
---

# Benzaldehyde

`molecule.C00261`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00261`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Benzaldehyde; Benzoic aldehyde

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00623` Toluene degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)

## Annotation

KEGG compound: Benzaldehyde; Benzoic aldehyde

## Pathways

- `eco00623` Toluene degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.PHENYLSERINE-ALDOLASE-RXN|reaction.ecocyc.PHENYLSERINE-ALDOLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-24038|reaction.ecocyc.RXN-24038]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ACETALD-DEHYDROG-RXN|reaction.ecocyc.ACETALD-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.BADH-RXN|reaction.ecocyc.BADH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00261`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
