---
entity_id: "molecule.C00645"
entity_type: "small_molecule"
name: "N-Acetyl-D-mannosamine"
source_database: "KEGG"
source_id: "C00645"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-Acetyl-D-mannosamine"
  - "2-Acetamido-2-deoxy-D-mannose"
---

# N-Acetyl-D-mannosamine

`molecule.C00645`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00645`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-Acetyl-D-mannosamine; 2-Acetamido-2-deoxy-D-mannose

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: N-Acetyl-D-mannosamine; 2-Acetamido-2-deoxy-D-mannose

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R00414|reaction.R00414]] `KEGG` `database` - C00043 + C00001 <=> C00645 + C00015
- `is_product_of` --> [[reaction.ecocyc.ACNEULY-RXN|reaction.ecocyc.ACNEULY-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7390|reaction.ecocyc.RXN0-7390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.NANK-RXN|reaction.ecocyc.NANK-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-446|reaction.ecocyc.TRANS-RXN0-446]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (1)

- `transports` <-- [[complex.ecocyc.CPLX-165|complex.ecocyc.CPLX-165]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00645`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
