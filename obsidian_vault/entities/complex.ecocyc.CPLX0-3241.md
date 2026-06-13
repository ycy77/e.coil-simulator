---
entity_id: "complex.ecocyc.CPLX0-3241"
entity_type: "complex"
name: "ubiquinol—[NapC cytochrome c] reductase"
source_database: "EcoCyc"
source_id: "CPLX0-3241"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ubiquinol—[NapC cytochrome c] reductase

`complex.ecocyc.CPLX0-3241`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3241`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AAL3|protein.P0AAL3]], [[protein.P33934|protein.P33934]]

## Enriched Summary

The EG12064 and EG12062 genes are located in the operon of the periplasmic nitrite reductase. Both proteins are ferredoxin-type non-heme iron-sulfur proteins . A mutant lacking EG12064 and EG12062 was totally defective for growth in glycerol/nitrate medium. When grown in glucose/nitrate medium, it was found that the mutant had almost completely lost the ability to reduce nitrate. With ubiquinol as the electron donor no significant nitrate reduction could be observed . In a subsequent study, deletion of either EG12064 or EG12062 almost abolished Nap-dependent nitrate reduction by a strain incapable of producing menaquinone. Since experiments with a bacterial two-hybrid system showed that NapH interacts with NapC, it was concluded that both NapG and NapH are required for efficient electron transfer from ubiquinol, but not menaquinol, via NAPC-MONOMER NapC to the NapAB complex. Since NapC is able to transfer electrons directly from menaquinol to NapAB, NapH and NapG are not required when menaquinone is available . No direct evidence for the formation of a NapGH complex has been obtained yet, but the available experimental data is consistent with its existence . The EG12064 and EG12062 genes are located in the operon of the periplasmic nitrite reductase. Both proteins are ferredoxin-type non-heme iron-sulfur proteins...

## Biological Role

Catalyzes RXN-18584 (reaction.ecocyc.RXN-18584). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

The EG12064 and EG12062 genes are located in the operon of the periplasmic nitrite reductase. Both proteins are ferredoxin-type non-heme iron-sulfur proteins . A mutant lacking EG12064 and EG12062 was totally defective for growth in glycerol/nitrate medium. When grown in glucose/nitrate medium, it was found that the mutant had almost completely lost the ability to reduce nitrate. With ubiquinol as the electron donor no significant nitrate reduction could be observed . In a subsequent study, deletion of either EG12064 or EG12062 almost abolished Nap-dependent nitrate reduction by a strain incapable of producing menaquinone. Since experiments with a bacterial two-hybrid system showed that NapH interacts with NapC, it was concluded that both NapG and NapH are required for efficient electron transfer from ubiquinol, but not menaquinol, via NAPC-MONOMER NapC to the NapAB complex. Since NapC is able to transfer electrons directly from menaquinol to NapAB, NapH and NapG are not required when menaquinone is available . No direct evidence for the formation of a NapGH complex has been obtained yet, but the available experimental data is consistent with its existence .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-18584|reaction.ecocyc.RXN-18584]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AAL3|protein.P0AAL3]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P33934|protein.P33934]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-3241`
- `QSPROTEOME:QS00049417`

## Notes

1*protein.P0AAL3|1*protein.P33934
