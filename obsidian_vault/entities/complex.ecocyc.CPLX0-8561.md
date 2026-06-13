---
entity_id: "complex.ecocyc.CPLX0-8561"
entity_type: "complex"
name: "methionine transaminase"
source_database: "EcoCyc"
source_id: "CPLX0-8561"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# methionine transaminase

`complex.ecocyc.CPLX0-8561`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8561`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77806|protein.P77806]]

## Enriched Summary

YbdL is an aminotransferase that was reported to have a preference for methionine followed by histidine and phenylalanine . However, deletion of ybdL in a ΔEG10372 ΔEG10403-EG10404 strain (which is not able to use GLT as an amine donor) did not affect growth with methionine as an amine donor, suggesting that the physiological contribution of YbdL to the use of methionine as an amine source is negligible . A crystal structure of YbdL was solved at 2.35 Å resolution, showing a homodimer with a typical aspartate aminotransferase fold. YbdL contains a covalently bound pyridoxal-5'-phosphate at the conserved active site residue Lys236 . Expression of ybdL is increased by exposure to S-nitrosoglutathione in defined medium under aerobic conditions . YbdL is an aminotransferase that was reported to have a preference for methionine followed by histidine and phenylalanine . However, deletion of ybdL in a ΔEG10372 ΔEG10403-EG10404 strain (which is not able to use GLT as an amine donor) did not affect growth with methionine as an amine donor, suggesting that the physiological contribution of YbdL to the use of methionine as an amine source is negligible . A crystal structure of YbdL was solved at 2.35 Å resolution, showing a homodimer with a typical aspartate aminotransferase fold. YbdL contains a covalently bound pyridoxal-5'-phosphate at the conserved active site residue Lys236...

## Biological Role

Catalyzes R15-RXN (reaction.ecocyc.R15-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

YbdL is an aminotransferase that was reported to have a preference for methionine followed by histidine and phenylalanine . However, deletion of ybdL in a ΔEG10372 ΔEG10403-EG10404 strain (which is not able to use GLT as an amine donor) did not affect growth with methionine as an amine donor, suggesting that the physiological contribution of YbdL to the use of methionine as an amine source is negligible . A crystal structure of YbdL was solved at 2.35 Å resolution, showing a homodimer with a typical aspartate aminotransferase fold. YbdL contains a covalently bound pyridoxal-5'-phosphate at the conserved active site residue Lys236 . Expression of ybdL is increased by exposure to S-nitrosoglutathione in defined medium under aerobic conditions .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.R15-RXN|reaction.ecocyc.R15-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P77806|protein.P77806]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8561`
- `QSPROTEOME:QS00188665`

## Notes

2*protein.P77806
