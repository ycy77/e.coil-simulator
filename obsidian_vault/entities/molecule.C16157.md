---
entity_id: "molecule.C16157"
entity_type: "small_molecule"
name: "Undecaprenyl phosphate alpha-L-Ara4N"
source_database: "KEGG"
source_id: "C16157"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Undecaprenyl phosphate alpha-L-Ara4N"
  - "4-Amino-4-deoxy-alpha-L-arabinopyranosyl ditrans,octacis-undecaprenyl phosphate"
---

# Undecaprenyl phosphate alpha-L-Ara4N

`molecule.C16157`

## Static

- Type: `small_molecule`
- Source: `KEGG:C16157`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Undecaprenyl phosphate alpha-L-Ara4N; 4-Amino-4-deoxy-alpha-L-arabinopyranosyl ditrans,octacis-undecaprenyl phosphate EcoCyc common name: 4-amino-4-deoxy-α-L-arabinopyranosyl ditrans,octacis-undecaprenyl phosphate.

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Annotation

KEGG compound: Undecaprenyl phosphate alpha-L-Ara4N; 4-Amino-4-deoxy-alpha-L-arabinopyranosyl ditrans,octacis-undecaprenyl phosphate

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.RXN0-5409|reaction.ecocyc.RXN0-5409]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-276|reaction.ecocyc.TRANS-RXN0-276]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R09773|reaction.R09773]] `KEGG` `database` - C16157 + C04919 <=> C19884 + C17556
- `is_substrate_of` --> [[reaction.R09774|reaction.R09774]] `KEGG` `database` - C16157 + C06025 <=> C19883 + C17556
- `is_substrate_of` --> [[reaction.R09781|reaction.R09781]] `KEGG` `database` - C06026 + C16157 <=> C19890 + C17556
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2001|reaction.ecocyc.RXN0-2001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-276|reaction.ecocyc.TRANS-RXN0-276]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C16157`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
