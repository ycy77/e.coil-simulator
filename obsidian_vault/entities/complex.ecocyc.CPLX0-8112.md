---
entity_id: "complex.ecocyc.CPLX0-8112"
entity_type: "complex"
name: "50S ribosomal protein L16-arginine 3-hydroxylase"
source_database: "EcoCyc"
source_id: "CPLX0-8112"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 50S ribosomal protein L16-arginine 3-hydroxylase

`complex.ecocyc.CPLX0-8112`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8112`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P27431|protein.P27431]]

## Enriched Summary

RoxA is a ribosomal oxygenase that hydroxylates the Arg81 residue of EG10877-MONOMER . RoxA is a member of the 2OG oxygenase family ; a new structural subfamily with highly conserved folds and novel dimerization modes has been defined . Crystal structures of RoxA have been determined at 2.7 Å and 2.6 Å resolution, showing a homodimeric form. RoxA binds 2-oxoglutarate, and residues S116 or R140 were found to be required for the interaction . An I211R mutation disrupts dimerization and decreases catalytic activity of RoxA . A roxA deletion strain exhibits lowered bulk translation rates than wild type and a growth defect in minimal media . roxA is not essential for viability . Overexpression of RoxA inhibits colony formation on LB agar . RoxA is a ribosomal oxygenase that hydroxylates the Arg81 residue of EG10877-MONOMER . RoxA is a member of the 2OG oxygenase family ; a new structural subfamily with highly conserved folds and novel dimerization modes has been defined . Crystal structures of RoxA have been determined at 2.7 Å and 2.6 Å resolution, showing a homodimeric form. RoxA binds 2-oxoglutarate, and residues S116 or R140 were found to be required for the interaction . An I211R mutation disrupts dimerization and decreases catalytic activity of RoxA . A roxA deletion strain exhibits lowered bulk translation rates than wild type and a growth defect in minimal media...

## Biological Role

Catalyzes RXN0-7090 (reaction.ecocyc.RXN0-7090). Bound by Fe2+ (molecule.C14818).

## Annotation

RoxA is a ribosomal oxygenase that hydroxylates the Arg81 residue of EG10877-MONOMER . RoxA is a member of the 2OG oxygenase family ; a new structural subfamily with highly conserved folds and novel dimerization modes has been defined . Crystal structures of RoxA have been determined at 2.7 Å and 2.6 Å resolution, showing a homodimeric form. RoxA binds 2-oxoglutarate, and residues S116 or R140 were found to be required for the interaction . An I211R mutation disrupts dimerization and decreases catalytic activity of RoxA . A roxA deletion strain exhibits lowered bulk translation rates than wild type and a growth defect in minimal media . roxA is not essential for viability . Overexpression of RoxA inhibits colony formation on LB agar .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7090|reaction.ecocyc.RXN0-7090]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P27431|protein.P27431]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8112`
- `QSPROTEOME:QS00188885`

## Notes

2*protein.P27431
