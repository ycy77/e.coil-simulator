---
entity_id: "reaction.ecocyc.TRANS-RXN-1594"
entity_type: "reaction"
name: "TRANS-RXN-1594"
source_database: "EcoCyc"
source_id: "TRANS-RXN-1594"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-1594

`reaction.ecocyc.TRANS-RXN-1594`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-1594`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Antimicrobial-Peptides + ATP + WATER -> Antimicrobial-Peptides + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Antimicrobial-Peptides + ATP + WATER -> Antimicrobial-Peptides + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by putative antimicrobial peptide ABC transporter (complex.ecocyc.ABC-29-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), an antimicrobial peptide (molecule.ecocyc.Antimicrobial-Peptides). Products: ADP (molecule.C00008), H+ (molecule.C00080), an antimicrobial peptide (molecule.ecocyc.Antimicrobial-Peptides), phosphate (molecule.ecocyc.Pi).

## Annotation

Antimicrobial-Peptides + ATP + WATER -> Antimicrobial-Peptides + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.ABC-29-CPLX|complex.ecocyc.ABC-29-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Antimicrobial-Peptides|molecule.ecocyc.Antimicrobial-Peptides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Antimicrobial-Peptides|molecule.ecocyc.Antimicrobial-Peptides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-1594`

## Notes

Antimicrobial-Peptides + ATP + WATER -> Antimicrobial-Peptides + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
