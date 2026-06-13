---
entity_id: "molecule.C00096"
entity_type: "small_molecule"
name: "GDP-mannose"
source_database: "KEGG"
source_id: "C00096"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "GDP-mannose"
  - "GDP-D-mannose"
  - "GDP-alpha-D-mannose"
---

# GDP-mannose

`molecule.C00096`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00096`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: GDP-mannose; GDP-D-mannose; GDP-alpha-D-mannose EcoCyc common name: GDP-α-D-mannose.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: GDP-mannose; GDP-D-mannose; GDP-alpha-D-mannose

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.2.7.7.13-RXN|reaction.ecocyc.2.7.7.13-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.GDPMANDEHYDRA-RXN|reaction.ecocyc.GDPMANDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GDPMANMANHYDRO-RXN|reaction.ecocyc.GDPMANMANHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5108|reaction.ecocyc.RXN0-5108]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00096`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
