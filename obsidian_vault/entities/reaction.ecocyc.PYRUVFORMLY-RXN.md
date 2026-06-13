---
entity_id: "reaction.ecocyc.PYRUVFORMLY-RXN"
entity_type: "reaction"
name: "PYRUVFORMLY-RXN"
source_database: "EcoCyc"
source_id: "PYRUVFORMLY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PYRUVFORMLY-RXN

`reaction.ecocyc.PYRUVFORMLY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYRUVFORMLY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A key reaction of anaerobic glucose fermentation pathway. EcoCyc reaction equation: FORMATE + ACETYL-COA -> PYRUVATE + CO-A; direction=REVERSIBLE. A key reaction of anaerobic glucose fermentation pathway.

## Biological Role

Catalyzed by PFL-GrcA complex (complex.ecocyc.CPLX0-9871), activated pyruvate-formate lyase (complex.ecocyc.PYRUVFORMLY-CPLX), tdcE (protein.P42632). Substrates: Acetyl-CoA (molecule.C00024), Formate (molecule.C00058). Products: CoA (molecule.C00010), Pyruvate (molecule.C00022).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-5480` pyruvate fermentation to ethanol I (EcoCyc)
- `ecocyc.PWY-5485` pyruvate fermentation to acetate IV (EcoCyc)

## Annotation

A key reaction of anaerobic glucose fermentation pathway.

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-5480` pyruvate fermentation to ethanol I (EcoCyc)
- `ecocyc.PWY-5485` pyruvate fermentation to acetate IV (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-9871|complex.ecocyc.CPLX0-9871]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.PYRUVFORMLY-CPLX|complex.ecocyc.PYRUVFORMLY-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P42632|protein.P42632]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-13859|molecule.ecocyc.CPD-13859]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-27|molecule.ecocyc.CPD-27]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PYRUVFORMLY-RXN`

## Notes

FORMATE + ACETYL-COA -> PYRUVATE + CO-A; direction=REVERSIBLE
