---
entity_id: "molecule.C00430"
entity_type: "small_molecule"
name: "5-Aminolevulinate"
source_database: "KEGG"
source_id: "C00430"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "5-Aminolevulinate"
  - "5-Amino-4-oxopentanoate"
  - "5-Amino-4-oxovaleric acid"
  - "5-Amino-4-oxopentanoic acid"
---

# 5-Aminolevulinate

`molecule.C00430`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00430`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 5-Aminolevulinate; 5-Amino-4-oxopentanoate; 5-Amino-4-oxovaleric acid; 5-Amino-4-oxopentanoic acid

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: 5-Aminolevulinate; 5-Amino-4-oxopentanoate; 5-Amino-4-oxovaleric acid; 5-Amino-4-oxopentanoic acid

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00860` Porphyrin metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.GSAAMINOTRANS-RXN|reaction.ecocyc.GSAAMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00036|reaction.R00036]] `KEGG` `database` - 2 C00430 <=> C00931 + 2 C00001
- `is_substrate_of` --> [[reaction.ecocyc.PORPHOBILSYNTH-RXN|reaction.ecocyc.PORPHOBILSYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00430`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
