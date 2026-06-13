---
entity_id: "complex.ecocyc.CPLX0-3541"
entity_type: "complex"
name: "ATP-dependent RNA helicase RhlB"
source_database: "EcoCyc"
source_id: "CPLX0-3541"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "RhlB"
  - "MmrA"
---

# ATP-dependent RNA helicase RhlB

`complex.ecocyc.CPLX0-3541`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3541`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A8J8|protein.P0A8J8]]

## Enriched Summary

RNA helicase B (RhlB) is an ATP-dependent helicase that mediates the unwinding of dsRNA structures. It is a component of the CPLX0-2381 where it aids 3' to 5' exonucleolytic ssRNA degradation by CPLX0-3521 "PNPase", and is required for full degradosome activity . RhlB is a member of the DEAD-box family of ATP-dependent RNA helicases, five of which are found in E. coli (RhlB, RhlE, DeaD (CsdA), DbpA and SrmB) . RhlB binds to the C-terminal scaffold region of CPLX0-3461 "RNase E" in the degradosome, an interaction that both makes it part of the complex and stimulates its ATPase activity . In at least one case, rpsT mRNA, substrate polyadenylation is required following cleavage by RNase E to allow RhlB and PNPase to complete degradation . RhlB also has several ATP-independent activities including RNA strand annealing, RNA strand displacement, and RNA chaperone activity . In E. coli K-12 rhlB is only necessary for viability in some genetic backgrounds and its conditional lethality is not complemented by SrmB . A nonpolar deletion mutant of rhlB showed no growth defect in rich medium . Overexpression of RhlB, SrmB, or DeaD (CsdA) enhanced fitness and buffered the accumulation of deleterious mutations in E. coli mutator strains . In addition to its association with RNase E in the degradosome, RhlB can independently form homodimers (or multimers) which associate with PNPase in vivo...

## Biological Role

Catalyzes RXN-24178 (reaction.ecocyc.RXN-24178). Component of degradosome (complex.ecocyc.CPLX0-2381). Bound by Magnesium cation (molecule.C00305).

## Annotation

RNA helicase B (RhlB) is an ATP-dependent helicase that mediates the unwinding of dsRNA structures. It is a component of the CPLX0-2381 where it aids 3' to 5' exonucleolytic ssRNA degradation by CPLX0-3521 "PNPase", and is required for full degradosome activity . RhlB is a member of the DEAD-box family of ATP-dependent RNA helicases, five of which are found in E. coli (RhlB, RhlE, DeaD (CsdA), DbpA and SrmB) . RhlB binds to the C-terminal scaffold region of CPLX0-3461 "RNase E" in the degradosome, an interaction that both makes it part of the complex and stimulates its ATPase activity . In at least one case, rpsT mRNA, substrate polyadenylation is required following cleavage by RNase E to allow RhlB and PNPase to complete degradation . RhlB also has several ATP-independent activities including RNA strand annealing, RNA strand displacement, and RNA chaperone activity . In E. coli K-12 rhlB is only necessary for viability in some genetic backgrounds and its conditional lethality is not complemented by SrmB . A nonpolar deletion mutant of rhlB showed no growth defect in rich medium . Overexpression of RhlB, SrmB, or DeaD (CsdA) enhanced fitness and buffered the accumulation of deleterious mutations in E. coli mutator strains . In addition to its association with RNase E in the degradosome, RhlB can independently form homodimers (or multimers) which associate with PNPase in vivo. In vitro assays showed specific binding of RhlB to itself and to PNPase, but neither protein interacted with ENOLASE-CPLX. In addition to its physical interactions, helicase assays demonstrated that the ATP-dependent unwinding activity of RhlB is necessary for PNPase to degrade dsRNA . In the absence of the RNase E C-terminal scaffold domain, PNPase and RhlB were shown to form an active α3β2 exorib

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-24178|reaction.ecocyc.RXN-24178]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-2381|complex.ecocyc.CPLX0-2381]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A8J8|protein.P0A8J8]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-3541`
- `QSPROTEOME:QS00049387`

## Notes

2*protein.P0A8J8
