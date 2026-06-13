---
entity_id: "molecule.C03273"
entity_type: "small_molecule"
name: "5-Oxopentanoate"
source_database: "KEGG"
source_id: "C03273"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-Oxopentanoate"
  - "Glutarate semialdehyde"
  - "5-Oxopentanoic acid"
---

# 5-Oxopentanoate

`molecule.C03273`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03273`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-Oxopentanoate; Glutarate semialdehyde; 5-Oxopentanoic acid EcoCyc common name: glutarate semialdehyde.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)

## Annotation

KEGG compound: 5-Oxopentanoate; Glutarate semialdehyde; 5-Oxopentanoic acid

## Pathways

- `eco00310` Lysine degradation (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.VAGL-RXN|reaction.ecocyc.VAGL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R02401|reaction.R02401]] `KEGG` `database` - C03273 + C00003 + C00001 <=> C00489 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.RXN-8182|reaction.ecocyc.RXN-8182]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN|reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03273`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
