---
entity_id: "molecule.C03981"
entity_type: "small_molecule"
name: "2-Hydroxyethylenedicarboxylate"
source_database: "KEGG"
source_id: "C03981"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "2-Hydroxyethylenedicarboxylate"
  - "enol-Oxaloacetate"
  - "enol-Oxaloacetic acid"
  - "2-Hydroxybut-2-enedioic acid"
---

# 2-Hydroxyethylenedicarboxylate

`molecule.C03981`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03981`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 2-Hydroxyethylenedicarboxylate; enol-Oxaloacetate; enol-Oxaloacetic acid; 2-Hydroxybut-2-enedioic acid EcoCyc common name: enol-oxaloacetate. This is the enol form tautomer of OXALACETIC_ACID.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)

## Annotation

KEGG compound: 2-Hydroxyethylenedicarboxylate; enol-Oxaloacetate; enol-Oxaloacetic acid; 2-Hydroxybut-2-enedioic acid

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R00363|reaction.R00363]] `KEGG` `database` - C00036 <=> C03981
- `is_product_of` --> [[reaction.ecocyc.OXALOACETATE-TAUTOMERASE-RXN|reaction.ecocyc.OXALOACETATE-TAUTOMERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21383|reaction.ecocyc.RXN-21383]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03981`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
