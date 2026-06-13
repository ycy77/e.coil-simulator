---
entity_id: "reaction.ecocyc.RXN0-5190"
entity_type: "reaction"
name: "RXN0-5190"
source_database: "EcoCyc"
source_id: "RXN0-5190"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN|CCO-CYTOSOL|CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5190

`reaction.ecocyc.RXN0-5190`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5190`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN|CCO-CYTOSOL|CCO-PERI-BAC

## Enriched Summary

Nascent-peptidoglycan-dimer -> GlcNAc-1-6-anhydro-MurNAc-pentapeptide + NAcMur-5Peptide-NAcGlc-Undecaprenols; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Nascent-peptidoglycan-dimer -> GlcNAc-1-6-anhydro-MurNAc-pentapeptide + NAcMur-5Peptide-NAcGlc-Undecaprenols; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: a nascent peptidoglycan dimer (generic) (molecule.ecocyc.Nascent-peptidoglycan-dimer). Products: a GlcNAc-1,6-anhydro-MurNAc-pentapeptide (molecule.ecocyc.GlcNAc-1-6-anhydro-MurNAc-pentapeptide), a lipid II (containing a pentapeptide) (molecule.ecocyc.NAcMur-5Peptide-NAcGlc-Undecaprenols).

## Annotation

Nascent-peptidoglycan-dimer -> GlcNAc-1-6-anhydro-MurNAc-pentapeptide + NAcMur-5Peptide-NAcGlc-Undecaprenols; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.ecocyc.GlcNAc-1-6-anhydro-MurNAc-pentapeptide|molecule.ecocyc.GlcNAc-1-6-anhydro-MurNAc-pentapeptide]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.NAcMur-5Peptide-NAcGlc-Undecaprenols|molecule.ecocyc.NAcMur-5Peptide-NAcGlc-Undecaprenols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Nascent-peptidoglycan-dimer|molecule.ecocyc.Nascent-peptidoglycan-dimer]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5190`

## Notes

Nascent-peptidoglycan-dimer -> GlcNAc-1-6-anhydro-MurNAc-pentapeptide + NAcMur-5Peptide-NAcGlc-Undecaprenols; direction=PHYSIOL-LEFT-TO-RIGHT
