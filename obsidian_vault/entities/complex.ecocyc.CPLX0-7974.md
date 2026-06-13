---
entity_id: "complex.ecocyc.CPLX0-7974"
entity_type: "complex"
name: "RNA decapping hydrolase"
source_database: "EcoCyc"
source_id: "CPLX0-7974"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# RNA decapping hydrolase

`complex.ecocyc.CPLX0-7974`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7974`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P32664|protein.P32664]]

## Enriched Summary

RNA molecules that have been capped at the 5' end with an NAD moiety have been discovered ; the caps are incorporated into certain RNAs as non-canonical initiating nucleotides (NCIN) during transcription initiation . NudC is active in decapping NAD-capped and dephospho-CoA-capped RNAs. NudC belongs to the family of "Nudix" hydrolases . In vitro, it was initially found to have NADH pyrophosphatase activity with a preference for NADH, the reduced form of the cofactor, as a substrate; its Km for NADH is 50-fold lower than its Km for NAD+ . However, NAD-capped RNA far outcompetes NAD+ as a substrate and is therefore the physiologically relevant substrate . Dephospho-CoA-capped RNA appears to be an even better substrate . NudC binds both RNA and DNA oligonucleotides and binds NAD+- and NADH-capped RNA with similar affinity, but has low affinity for m7G-capped RNA . An E178Q mutant is catalytically inactive; Y124 and F160 appear to play a role in the recognition of the AMP moiety. Mutations in several other residues have effects on the catalytic activity, in some cases specific to the substrate assayed . Crystal structures of NudC alone and in complexes with NAD, NMN or dpCoA have been solved . Predicted active site residues of the Nudix box and zinc-binding motif were mutagenized and found to be required for activity...

## Biological Role

Catalyzes RXN0-4401 (reaction.ecocyc.RXN0-4401), RXN0-7346 (reaction.ecocyc.RXN0-7346). Bound by Zinc cation (molecule.C00038), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

RNA molecules that have been capped at the 5' end with an NAD moiety have been discovered ; the caps are incorporated into certain RNAs as non-canonical initiating nucleotides (NCIN) during transcription initiation . NudC is active in decapping NAD-capped and dephospho-CoA-capped RNAs. NudC belongs to the family of "Nudix" hydrolases . In vitro, it was initially found to have NADH pyrophosphatase activity with a preference for NADH, the reduced form of the cofactor, as a substrate; its Km for NADH is 50-fold lower than its Km for NAD+ . However, NAD-capped RNA far outcompetes NAD+ as a substrate and is therefore the physiologically relevant substrate . Dephospho-CoA-capped RNA appears to be an even better substrate . NudC binds both RNA and DNA oligonucleotides and binds NAD+- and NADH-capped RNA with similar affinity, but has low affinity for m7G-capped RNA . An E178Q mutant is catalytically inactive; Y124 and F160 appear to play a role in the recognition of the AMP moiety. Mutations in several other residues have effects on the catalytic activity, in some cases specific to the substrate assayed . Crystal structures of NudC alone and in complexes with NAD, NMN or dpCoA have been solved . Predicted active site residues of the Nudix box and zinc-binding motif were mutagenized and found to be required for activity . The enzyme shows a preference for a purine and at least three unpaired nucleotides at the 5' terminus of the RNA substrate . An E178Q mutant lacks RNA decapping activity. A ΔnudC mutant shows increased levels of RNA modified with an NAD cap . Reviews:

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4401|reaction.ecocyc.RXN0-4401]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7346|reaction.ecocyc.RXN0-7346]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P32664|protein.P32664]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7974`
- `QSPROTEOME:QS00182763`

## Notes

2*protein.P32664
