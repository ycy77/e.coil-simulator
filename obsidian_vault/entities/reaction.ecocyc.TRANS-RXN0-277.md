---
entity_id: "reaction.ecocyc.TRANS-RXN0-277"
entity_type: "reaction"
name: "TRANS-RXN0-277"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-277"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-277

`reaction.ecocyc.TRANS-RXN0-277`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-277`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NADPH + NAD + PROTON -> NADP + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: NADPH + NAD + PROTON -> NADP + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by pyridine nucleotide transhydrogenase (complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX). Substrates: NAD+ (molecule.C00003), NADPH (molecule.C00005), H+ (molecule.C00080). Products: NADH (molecule.C00004), NADP+ (molecule.C00006), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.NADPHOS-DEPHOS-PWY` NAD phosphorylation and dephosphorylation (EcoCyc)

## Annotation

NADPH + NAD + PROTON -> NADP + NADH + PROTON; direction=REVERSIBLE

## Pathways

- `ecocyc.NADPHOS-DEPHOS-PWY` NAD phosphorylation and dephosphorylation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX|complex.ecocyc.PYRNUTRANSHYDROGEN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-10322|molecule.ecocyc.CPD-10322]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1250|molecule.ecocyc.CPD0-1250]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-277`

## Notes

NADPH + NAD + PROTON -> NADP + NADH + PROTON; direction=REVERSIBLE
