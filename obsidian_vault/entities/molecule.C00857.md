---
entity_id: "molecule.C00857"
entity_type: "small_molecule"
name: "Deamino-NAD+"
source_database: "KEGG"
source_id: "C00857"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Deamino-NAD+"
  - "Deamido-NAD+"
  - "Deamido-NAD"
  - "Nicotinic acid adenine dinucleotide"
---

# Deamino-NAD+

`molecule.C00857`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00857`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Deamino-NAD+; Deamido-NAD+; Deamido-NAD; Nicotinic acid adenine dinucleotide EcoCyc common name: nicotinate adenine dinucleotide.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Annotation

KEGG compound: Deamino-NAD+; Deamido-NAD+; Deamido-NAD; Nicotinic acid adenine dinucleotide

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.ecocyc.NICONUCADENYLYLTRAN-RXN|reaction.ecocyc.NICONUCADENYLYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00189|reaction.R00189]] `KEGG` `database` - C00002 + C00857 + C00014 <=> C00020 + C00013 + C00003
- `is_substrate_of` --> [[reaction.ecocyc.NAD-SYNTH-GLN-RXN|reaction.ecocyc.NAD-SYNTH-GLN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.NAD-SYNTH-NH3-RXN|reaction.ecocyc.NAD-SYNTH-NH3-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00857`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
