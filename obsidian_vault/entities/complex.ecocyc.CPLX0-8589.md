---
entity_id: "complex.ecocyc.CPLX0-8589"
entity_type: "complex"
name: "3-aminoacrylate deaminase"
source_database: "EcoCyc"
source_id: "CPLX0-8589"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 3-aminoacrylate deaminase

`complex.ecocyc.CPLX0-8589`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8589`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AFQ5|protein.P0AFQ5]]

## Enriched Summary

E. coli K-12 contains a previously undescribed pathway for pyrimidine degradation. RutC catalyzes the 3-aminoacrylate deaminase reaction, which can also occur spontaneously at a lower rate . A crystal structure of RutC from E. coli strain CFT073 has been solved at 1.95 Å resolution. The protein is homotrimeric in the crystal structure . (Note: The RutC sequence from CFT073 is 100% identical to RutC from K-12 MG1655.) An R104A mutant in the predicted active site reduces the rate of 3-aminoacrylate deamination to that of the spontaneously occurring reaction . Expression of the rutABCDEFG operon is under the control of nitrogen regulatory protein C (NtrC) . A rutC insertion mutant loses the ability to utilize pyrimidine nucleosides and bases as the sole source of nitrogen at room temperature . RutC is not required for the release of ammonium from uracil in vitro , likely because the reaction it catalyzes can also occur spontaneously . Overexpression of rutC from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid . RutC: "pyrimidine utilization C" Reviews: E. coli K-12 contains a previously undescribed pathway for pyrimidine degradation. RutC catalyzes the 3-aminoacrylate deaminase reaction, which can also occur spontaneously at a lower rate . A crystal structure of RutC from E. coli strain CFT073 has been solved at 1.95 Å resolution...

## Biological Role

Catalyzes RXN0-6452 (reaction.ecocyc.RXN0-6452).

## Annotation

E. coli K-12 contains a previously undescribed pathway for pyrimidine degradation. RutC catalyzes the 3-aminoacrylate deaminase reaction, which can also occur spontaneously at a lower rate . A crystal structure of RutC from E. coli strain CFT073 has been solved at 1.95 Å resolution. The protein is homotrimeric in the crystal structure . (Note: The RutC sequence from CFT073 is 100% identical to RutC from K-12 MG1655.) An R104A mutant in the predicted active site reduces the rate of 3-aminoacrylate deamination to that of the spontaneously occurring reaction . Expression of the rutABCDEFG operon is under the control of nitrogen regulatory protein C (NtrC) . A rutC insertion mutant loses the ability to utilize pyrimidine nucleosides and bases as the sole source of nitrogen at room temperature . RutC is not required for the release of ammonium from uracil in vitro , likely because the reaction it catalyzes can also occur spontaneously . Overexpression of rutC from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid . RutC: "pyrimidine utilization C" Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6452|reaction.ecocyc.RXN0-6452]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AFQ5|protein.P0AFQ5]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-8589`
- `QSPROTEOME:QS00182011`

## Notes

3*protein.P0AFQ5
