---
entity_id: "complex.ecocyc.CPLX0-8613"
entity_type: "complex"
name: "dethiobiotin synthetase BidA"
source_database: "EcoCyc"
source_id: "CPLX0-8613"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dethiobiotin synthetase BidA

`complex.ecocyc.CPLX0-8613`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8613`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A6E9|protein.P0A6E9]]

## Enriched Summary

BidA was shown to have dethiobiotin synthetase activity in vitro. In vivo, the activity of BidA appears to be limited by the availability of its substrate, DIAMINONONANOATE DAPA . BidA shows sequence similarity to DETHIOBIOTIN-SYN-MONOMER BioD; replacement of active site residues with the corresponding residues of the more-active BioD enzyme increase the dethiobiotin synthetase activity of BidA. EGS crosslinking assays suggest that BidA has a weaker homodimerization activity than BioD; DAPA improves dimer formation . bidA is only weakly expressed. Transcription is activated by FNR . Under anaerobic conditions on minimal media, a ΔbioD mutant shows weak growth; growth of a double ΔbioD ΔbidA deletion mutant requires supplementation with biotin . BidA: "BioD anaerobic" BidA was shown to have dethiobiotin synthetase activity in vitro. In vivo, the activity of BidA appears to be limited by the availability of its substrate, DIAMINONONANOATE DAPA . BidA shows sequence similarity to DETHIOBIOTIN-SYN-MONOMER BioD; replacement of active site residues with the corresponding residues of the more-active BioD enzyme increase the dethiobiotin synthetase activity of BidA. EGS crosslinking assays suggest that BidA has a weaker homodimerization activity than BioD; DAPA improves dimer formation . bidA is only weakly expressed. Transcription is activated by FNR...

## Biological Role

Catalyzes DETHIOBIOTIN-SYN-RXN (reaction.ecocyc.DETHIOBIOTIN-SYN-RXN).

## Annotation

BidA was shown to have dethiobiotin synthetase activity in vitro. In vivo, the activity of BidA appears to be limited by the availability of its substrate, DIAMINONONANOATE DAPA . BidA shows sequence similarity to DETHIOBIOTIN-SYN-MONOMER BioD; replacement of active site residues with the corresponding residues of the more-active BioD enzyme increase the dethiobiotin synthetase activity of BidA. EGS crosslinking assays suggest that BidA has a weaker homodimerization activity than BioD; DAPA improves dimer formation . bidA is only weakly expressed. Transcription is activated by FNR . Under anaerobic conditions on minimal media, a ΔbioD mutant shows weak growth; growth of a double ΔbioD ΔbidA deletion mutant requires supplementation with biotin . BidA: "BioD anaerobic"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DETHIOBIOTIN-SYN-RXN|reaction.ecocyc.DETHIOBIOTIN-SYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A6E9|protein.P0A6E9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8613`
- `QSPROTEOME:QS00203713`

## Notes

2*protein.P0A6E9
