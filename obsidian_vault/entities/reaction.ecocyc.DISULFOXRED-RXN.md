---
entity_id: "reaction.ecocyc.DISULFOXRED-RXN"
entity_type: "reaction"
name: "DISULFOXRED-RXN"
source_database: "EcoCyc"
source_id: "DISULFOXRED-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DISULFOXRED-RXN

`reaction.ecocyc.DISULFOXRED-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DISULFOXRED-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

This reaction forms disulfide bonds in proteins. EcoCyc reaction equation: Oxidized-Disulfide-Carrier-Proteins + Protein-Red-Disulfides -> Reduced-Disulfide-Carrier-Proteins + Protein-Ox-Disulfides; direction=REVERSIBLE. This reaction forms disulfide bonds in proteins.

## Biological Role

Catalyzed by chaperone protein DnaJ (complex.ecocyc.CPLX0-8191).

## Annotation

This reaction forms disulfide bonds in proteins.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8191|complex.ecocyc.CPLX0-8191]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## External IDs

- `EcoCyc:DISULFOXRED-RXN`

## Notes

Oxidized-Disulfide-Carrier-Proteins + Protein-Red-Disulfides -> Reduced-Disulfide-Carrier-Proteins + Protein-Ox-Disulfides; direction=REVERSIBLE
