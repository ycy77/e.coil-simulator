---
entity_id: "reaction.ecocyc.RXN0-3201"
entity_type: "reaction"
name: "RXN0-3201"
source_database: "EcoCyc"
source_id: "RXN0-3201"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3201

`reaction.ecocyc.RXN0-3201`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3201`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the hydrolysis of a peptide bond, typically within a hydrophobic portion of a cleaved signal sequence peptide. In that case, hydrophobic residues must be at the primary and adjacent sites, with a minimum of three residues on either side of the cut site. EcoCyc reaction equation: Lipoprotein-signal-peptide + WATER -> Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the hydrolysis of a peptide bond, typically within a hydrophobic portion of a cleaved signal sequence peptide. In that case, hydrophobic residues must be at the primary and adjacent sites, with a minimum of three residues on either side of the cut site.

## Biological Role

Catalyzed by protease IV, a signal peptide peptidase (complex.ecocyc.CPLX0-2941), rseP (protein.P0AEH1). Substrates: H2O (molecule.C00001), a lipoprotein signal peptide (molecule.ecocyc.Lipoprotein-signal-peptide).

## Enriched Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Annotation

This reaction is the hydrolysis of a peptide bond, typically within a hydrophobic portion of a cleaved signal sequence peptide. In that case, hydrophobic residues must be at the primary and adjacent sites, with a minimum of three residues on either side of the cut site.

## Pathways

- `ecocyc.PWY-7884` lipoprotein posttranslational modification (Gram-negative bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-2941|complex.ecocyc.CPLX0-2941]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AEH1|protein.P0AEH1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Lipoprotein-signal-peptide|molecule.ecocyc.Lipoprotein-signal-peptide]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3201`

## Notes

Lipoprotein-signal-peptide + WATER -> Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT
