---
entity_id: "reaction.ecocyc.RXN-14712"
entity_type: "reaction"
name: "RXN-14712"
source_database: "EcoCyc"
source_id: "RXN-14712"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14712

`reaction.ecocyc.RXN-14712`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14712`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Peptidoglycan glycosyltransferases add monomer units to the reducing end of the growing polymer . EcoCyc reaction equation: a-nascent-peptidoglycan-undecaprenol-anchored + NAcMur-Peptide-NAcGlc-Undecaprenols -> a-nascent-peptidoglycan-undecaprenol-anchored + UNDECAPRENYL-DIPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT. Peptidoglycan glycosyltransferases add monomer units to the reducing end of the growing polymer .

## Biological Role

Substrates: a lipid II (molecule.ecocyc.NAcMur-Peptide-NAcGlc-Undecaprenols), a nascent peptidoglycan (undecaprenol-anchored) (molecule.ecocyc.a-nascent-peptidoglycan-undecaprenol-anchored). Products: di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574), a nascent peptidoglycan (undecaprenol-anchored) (molecule.ecocyc.a-nascent-peptidoglycan-undecaprenol-anchored).

## Annotation

Peptidoglycan glycosyltransferases add monomer units to the reducing end of the growing polymer .

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C04574|molecule.C04574]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.a-nascent-peptidoglycan-undecaprenol-anchored|molecule.ecocyc.a-nascent-peptidoglycan-undecaprenol-anchored]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.NAcMur-Peptide-NAcGlc-Undecaprenols|molecule.ecocyc.NAcMur-Peptide-NAcGlc-Undecaprenols]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.a-nascent-peptidoglycan-undecaprenol-anchored|molecule.ecocyc.a-nascent-peptidoglycan-undecaprenol-anchored]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14712`

## Notes

a-nascent-peptidoglycan-undecaprenol-anchored + NAcMur-Peptide-NAcGlc-Undecaprenols -> a-nascent-peptidoglycan-undecaprenol-anchored + UNDECAPRENYL-DIPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT
