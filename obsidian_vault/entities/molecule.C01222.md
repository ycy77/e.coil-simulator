---
entity_id: "molecule.C01222"
entity_type: "small_molecule"
name: "GDP-4-dehydro-6-deoxy-D-mannose"
source_database: "KEGG"
source_id: "C01222"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "GDP-4-dehydro-6-deoxy-D-mannose"
  - "GDP-4-dehydro-6-deoxy-D-talose"
  - "GDP-4-oxo-6-deoxy-D-mannose"
  - "GDP-4-dehydro-D-rhamnose"
  - "GDP-4-keto-6-deoxy-D-mannose"
  - "GDP-4-dehydro-alpha-D-rhamnose"
  - "GDP-4-dehydro-6-deoxy-alpha-D-mannose"
---

# GDP-4-dehydro-6-deoxy-D-mannose

`molecule.C01222`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01222`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: GDP-4-dehydro-6-deoxy-D-mannose; GDP-4-dehydro-6-deoxy-D-talose; GDP-4-oxo-6-deoxy-D-mannose; GDP-4-dehydro-D-rhamnose; GDP-4-keto-6-deoxy-D-mannose; GDP-4-dehydro-alpha-D-rhamnose; GDP-4-dehydro-6-deoxy-alpha-D-mannose EcoCyc common name: GDP-4-dehydro-α-D-rhamnose. GDP-4-DEHYDRO-6-DEOXY-D-MANNOSE is a precursor for 6-deoxyhexose GDP-sugar nucleotides such as CPD-13118, CPD-9387, CPD-353, and the 3,6 dideoxyhexose nucleotide sugar CPD-9391.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: GDP-4-dehydro-6-deoxy-D-mannose; GDP-4-dehydro-6-deoxy-D-talose; GDP-4-oxo-6-deoxy-D-mannose; GDP-4-dehydro-D-rhamnose; GDP-4-keto-6-deoxy-D-mannose; GDP-4-dehydro-alpha-D-rhamnose; GDP-4-dehydro-6-deoxy-alpha-D-mannose

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.1.1.1.271-RXN|reaction.ecocyc.1.1.1.271-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GDPMANDEHYDRA-RXN|reaction.ecocyc.GDPMANDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.FCLEPIM-RXN|reaction.ecocyc.FCLEPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01222`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
