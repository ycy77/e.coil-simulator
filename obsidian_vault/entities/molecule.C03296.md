---
entity_id: "molecule.C03296"
entity_type: "small_molecule"
name: "N2-Succinyl-L-arginine"
source_database: "KEGG"
source_id: "C03296"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N2-Succinyl-L-arginine"
  - "(2S)-2-(3-Carboxypropanoylamino)-5-(diaminomethylideneamino)pentanoic acid"
---

# N2-Succinyl-L-arginine

`molecule.C03296`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03296`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N2-Succinyl-L-arginine; (2S)-2-(3-Carboxypropanoylamino)-5-(diaminomethylideneamino)pentanoic acid

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)

## Annotation

KEGG compound: N2-Succinyl-L-arginine; (2S)-2-(3-Carboxypropanoylamino)-5-(diaminomethylideneamino)pentanoic acid

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.R00832|reaction.R00832]] `KEGG` `database` - C00091 + C00062 <=> C00010 + C03296
- `is_product_of` --> [[reaction.ecocyc.ARGININE-N-SUCCINYLTRANSFERASE-RXN|reaction.ecocyc.ARGININE-N-SUCCINYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.SUCCARGDIHYDRO-RXN|reaction.ecocyc.SUCCARGDIHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03296`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
