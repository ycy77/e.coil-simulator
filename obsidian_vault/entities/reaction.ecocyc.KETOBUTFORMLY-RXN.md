---
entity_id: "reaction.ecocyc.KETOBUTFORMLY-RXN"
entity_type: "reaction"
name: "KETOBUTFORMLY-RXN"
source_database: "EcoCyc"
source_id: "KETOBUTFORMLY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "acetyl-CoA:formate C-acetyltransferase"
  - "formate acetyltransferase"
  - "pyruvate formate-lyase"
---

# KETOBUTFORMLY-RXN

`reaction.ecocyc.KETOBUTFORMLY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:KETOBUTFORMLY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the anaerobic L-threonine degradation pathway. EcoCyc reaction equation: PROPIONYL-COA + FORMATE -> 2-OXOBUTANOATE + CO-A; direction=REVERSIBLE. This is the second reaction in the anaerobic L-threonine degradation pathway.

## Biological Role

Catalyzed by PFL-GrcA complex (complex.ecocyc.CPLX0-9871), activated pyruvate-formate lyase (complex.ecocyc.PYRUVFORMLY-CPLX), tdcE (protein.P42632). Substrates: Formate (molecule.C00058), Propanoyl-CoA (molecule.C00100). Products: CoA (molecule.C00010), 2-Oxobutanoate (molecule.C00109).

## Enriched Pathways

- `ecocyc.PWY-5437` L-threonine degradation I (EcoCyc)

## Annotation

This is the second reaction in the anaerobic L-threonine degradation pathway.

## Pathways

- `ecocyc.PWY-5437` L-threonine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-9871|complex.ecocyc.CPLX0-9871]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.PYRUVFORMLY-CPLX|complex.ecocyc.PYRUVFORMLY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P42632|protein.P42632]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00109|molecule.C00109]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00100|molecule.C00100]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:KETOBUTFORMLY-RXN`

## Notes

PROPIONYL-COA + FORMATE -> 2-OXOBUTANOATE + CO-A; direction=REVERSIBLE
