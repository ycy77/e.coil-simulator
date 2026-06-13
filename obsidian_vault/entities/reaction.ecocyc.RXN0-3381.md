---
entity_id: "reaction.ecocyc.RXN0-3381"
entity_type: "reaction"
name: "RXN0-3381"
source_database: "EcoCyc"
source_id: "RXN0-3381"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3381

`reaction.ecocyc.RXN0-3381`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3381`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cr6+, the hexavalent form of chromate is usually found associated with oxygen as chromate (CrO42-) or dichromate (Cr2O72-). CPD-4422 "Chromate" is transported by the sulfate ABC transporter in E. coli . EcoCyc reaction equation: CR+6 + NADH-P-OR-NOP + OXYGEN-MOLECULE -> CR+3 + NAD-P-OR-NOP + SUPER-OXIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. Cr6+, the hexavalent form of chromate is usually found associated with oxygen as chromate (CrO42-) or dichromate (Cr2O72-). CPD-4422 "Chromate" is transported by the sulfate ABC transporter in E. coli .

## Biological Role

Catalyzed by quinone reductase (complex.ecocyc.CPLX0-3121). Substrates: Oxygen (molecule.C00007), Cr6+ (molecule.ecocyc.CR_6), NAD(P)H (molecule.ecocyc.NADH-P-OR-NOP). Products: H+ (molecule.C00080), Cr3+ (molecule.ecocyc.CR_3), NAD(P)+ (molecule.ecocyc.NAD-P-OR-NOP), superoxide (molecule.ecocyc.SUPER-OXIDE).

## Annotation

Cr6+, the hexavalent form of chromate is usually found associated with oxygen as chromate (CrO42-) or dichromate (Cr2O72-). CPD-4422 "Chromate" is transported by the sulfate ABC transporter in E. coli .

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3121|complex.ecocyc.CPLX0-3121]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CR_3|molecule.ecocyc.CR_3]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NAD-P-OR-NOP|molecule.ecocyc.NAD-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.SUPER-OXIDE|molecule.ecocyc.SUPER-OXIDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CR_6|molecule.ecocyc.CR_6]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.NADH-P-OR-NOP|molecule.ecocyc.NADH-P-OR-NOP]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3381`

## Notes

CR+6 + NADH-P-OR-NOP + OXYGEN-MOLECULE -> CR+3 + NAD-P-OR-NOP + SUPER-OXIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
