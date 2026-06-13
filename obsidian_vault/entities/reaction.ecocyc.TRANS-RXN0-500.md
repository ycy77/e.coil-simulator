---
entity_id: "reaction.ecocyc.TRANS-RXN0-500"
entity_type: "reaction"
name: "TRANS-RXN0-500"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-500"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-500

`reaction.ecocyc.TRANS-RXN0-500`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-500`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

4-methylphenol is a by-product of PWY-6892 "thiazole biosynthesis" in E. coli K-12. 4-methylphenol is detected in the supernatant of an E. coli strain lacking chromosomally encoded THIH-MONOMER "thiH" but expressing thiH from a plasmid . The transporter responsible for export has not been characterised. EcoCyc reaction equation: CPD-108 -> CPD-108; direction=PHYSIOL-LEFT-TO-RIGHT. 4-methylphenol is a by-product of PWY-6892 "thiazole biosynthesis" in E. coli K-12. 4-methylphenol is detected in the supernatant of an E. coli strain lacking chromosomally encoded THIH-MONOMER "thiH" but expressing thiH from a plasmid . The transporter responsible for export has not been characterised.

## Biological Role

Substrates: 4-Cresol (molecule.C01468). Products: 4-Cresol (molecule.C01468).

## Annotation

4-methylphenol is a by-product of PWY-6892 "thiazole biosynthesis" in E. coli K-12. 4-methylphenol is detected in the supernatant of an E. coli strain lacking chromosomally encoded THIH-MONOMER "thiH" but expressing thiH from a plasmid . The transporter responsible for export has not been characterised.

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C01468|molecule.C01468]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01468|molecule.C01468]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-500`

## Notes

CPD-108 -> CPD-108; direction=PHYSIOL-LEFT-TO-RIGHT
