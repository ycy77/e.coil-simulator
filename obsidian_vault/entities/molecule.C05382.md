---
entity_id: "molecule.C05382"
entity_type: "small_molecule"
name: "Sedoheptulose 7-phosphate"
source_database: "KEGG"
source_id: "C05382"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Sedoheptulose 7-phosphate"
  - "D-Sedoheptulose 7-phosphate"
  - "D-altro-Heptulose 7-phosphate"
  - "altro-Heptulose 7-phosphate"
---

# Sedoheptulose 7-phosphate

`molecule.C05382`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05382`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Sedoheptulose 7-phosphate; D-Sedoheptulose 7-phosphate; D-altro-Heptulose 7-phosphate; altro-Heptulose 7-phosphate EcoCyc common name: D-sedoheptulose 7-phosphate. D-SEDOHEPTULOSE-7-P is an intermediate molecule of primary glucose metabolism.

## Biological Role

Consumed as substrate in 7 reaction(s).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)

## Annotation

KEGG compound: Sedoheptulose 7-phosphate; D-Sedoheptulose 7-phosphate; D-altro-Heptulose 7-phosphate; altro-Heptulose 7-phosphate

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)

## Outgoing Edges (7)

- `is_substrate_of` --> [[reaction.R06863|reaction.R06863]] `KEGG` `database` - C05382 + C00068 <=> C13378 + C00117
- `is_substrate_of` --> [[reaction.R09768|reaction.R09768]] `KEGG` `database` - C05382 <=> C19882
- `is_substrate_of` --> [[reaction.R09769|reaction.R09769]] `KEGG` `database` - C05382 <=> C19878
- `is_substrate_of` --> [[reaction.ecocyc.1TRANSKETO-RXN|reaction.ecocyc.1TRANSKETO-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4301|reaction.ecocyc.RXN0-4301]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6541|reaction.ecocyc.RXN0-6541]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANSALDOL-RXN|reaction.ecocyc.TRANSALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05382`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
