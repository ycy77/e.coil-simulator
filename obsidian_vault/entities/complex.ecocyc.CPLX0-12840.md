---
entity_id: "complex.ecocyc.CPLX0-12840"
entity_type: "complex"
name: "cytochrome c552 nitrite reductase"
source_database: "EcoCyc"
source_id: "CPLX0-12840"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cytochrome c552 nitrite reductase

`complex.ecocyc.CPLX0-12840`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-12840`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ABK9|protein.P0ABK9]]

## Enriched Summary

nrfA is the structural gene for cytochrome c-552, a soluble periplasmic enzyme which catalyses the 6 electron reduction of nitrite to ammonia. nrfA encodes a cytochrome c nitrite reductase (cyt c552) . NrfA is a pentahaem enzyme that forms a redox complex with NrfB - also a pentahaem protein - to catalyse the reduction of nitrite to ammonia . NrfA is linked to the menaquinol pool in the cytoplasmic membrane through the electron carrier NrfB and the membrane integral proteins NrfC and NrfD; NrfC and NrfD are predicted to couple electron transport from the menaquinol pool in the membrane to the NrfAB complex in the periplasm . Cytochrome c-552 covalently binds five heme-c groups per molecule - 4 heme groups are bound to the conventional CXXCH- motif and one heme group is bound to the novel CWSCK motif . NrfA crystallises as a homodimer . NrfA receives electrons from the pentaheme c-type cytochrome, NrfB and under physiological conditions a tightly associated NrfAB decaheme heterodimer is predicted to exist . NrfA can also reduce and thereby detoxify nitric oxide (NO) ; mutant strains lacking NrfA activity have increased sensitivity to NO . Nitrite reduction and synthesis of the NrfA protein are repressed by oxygen. During anaerobic growth nitrite reduction by the Nrf pathway is induced by nitrite and repressed by nitrate...

## Biological Role

Catalyzes RXN-18605 (reaction.ecocyc.RXN-18605), RXN0-7493 (reaction.ecocyc.RXN0-7493).

## Annotation

nrfA is the structural gene for cytochrome c-552, a soluble periplasmic enzyme which catalyses the 6 electron reduction of nitrite to ammonia. nrfA encodes a cytochrome c nitrite reductase (cyt c552) . NrfA is a pentahaem enzyme that forms a redox complex with NrfB - also a pentahaem protein - to catalyse the reduction of nitrite to ammonia . NrfA is linked to the menaquinol pool in the cytoplasmic membrane through the electron carrier NrfB and the membrane integral proteins NrfC and NrfD; NrfC and NrfD are predicted to couple electron transport from the menaquinol pool in the membrane to the NrfAB complex in the periplasm . Cytochrome c-552 covalently binds five heme-c groups per molecule - 4 heme groups are bound to the conventional CXXCH- motif and one heme group is bound to the novel CWSCK motif . NrfA crystallises as a homodimer . NrfA receives electrons from the pentaheme c-type cytochrome, NrfB and under physiological conditions a tightly associated NrfAB decaheme heterodimer is predicted to exist . NrfA can also reduce and thereby detoxify nitric oxide (NO) ; mutant strains lacking NrfA activity have increased sensitivity to NO . Nitrite reduction and synthesis of the NrfA protein are repressed by oxygen. During anaerobic growth nitrite reduction by the Nrf pathway is induced by nitrite and repressed by nitrate . The PD00197 "Fnr transciptional regulator" is essential for NrfA synthesis and nitrite reduction by formate . The nrf operon is further regulated by the PWY0-1515 "NarQP" and PWY0-1515 "NarXL" two-component systems in response to levels of nitrite and nitrate in the environment. Related reviews:

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-18605|reaction.ecocyc.RXN-18605]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7493|reaction.ecocyc.RXN0-7493]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ABK9|protein.P0ABK9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-12840`

## Notes

2*protein.P0ABK9
