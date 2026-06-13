---
entity_id: "complex.ecocyc.CPLX0-8214"
entity_type: "complex"
name: "carboxylesterase"
source_database: "EcoCyc"
source_id: "CPLX0-8214"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# carboxylesterase

`complex.ecocyc.CPLX0-8214`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8214`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P39298|protein.P39298]]

## Enriched Summary

YjfP shows carboxylesterase activity towards aryl and carboxylic acid esters; activity was assayed using model substrates including pNP acetate and pNP butyrate. Ser115 was identified as the potential catalytic residue . The authors hypothesize that YjfP hydrolyzes acetylated sugars. Thioesterase activity of YjfP was detected in a high-throughput screen of purified proteins . was unable to detect the reported thioesterase activity. yjfP is expressed during the transition from growth on glucose to growth on lactose (the diauxic lag phase), and approaching stationary phase . In a yjfP mutant, expression of BETAGALACTOSID-CPLX during the transition to growth on lactose is delayed. Overexpression of yjfP leads to an extended lag phase when cells are shifted to lactose or galactose as the sole source of carbon . YjfP shows carboxylesterase activity towards aryl and carboxylic acid esters; activity was assayed using model substrates including pNP acetate and pNP butyrate. Ser115 was identified as the potential catalytic residue . The authors hypothesize that YjfP hydrolyzes acetylated sugars. Thioesterase activity of YjfP was detected in a high-throughput screen of purified proteins . was unable to detect the reported thioesterase activity. yjfP is expressed during the transition from growth on glucose to growth on lactose (the diauxic lag phase), and approaching stationary phase...

## Biological Role

Catalyzes CARBOXYLESTERASE-RXN (reaction.ecocyc.CARBOXYLESTERASE-RXN).

## Annotation

YjfP shows carboxylesterase activity towards aryl and carboxylic acid esters; activity was assayed using model substrates including pNP acetate and pNP butyrate. Ser115 was identified as the potential catalytic residue . The authors hypothesize that YjfP hydrolyzes acetylated sugars. Thioesterase activity of YjfP was detected in a high-throughput screen of purified proteins . was unable to detect the reported thioesterase activity. yjfP is expressed during the transition from growth on glucose to growth on lactose (the diauxic lag phase), and approaching stationary phase . In a yjfP mutant, expression of BETAGALACTOSID-CPLX during the transition to growth on lactose is delayed. Overexpression of yjfP leads to an extended lag phase when cells are shifted to lactose or galactose as the sole source of carbon .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CARBOXYLESTERASE-RXN|reaction.ecocyc.CARBOXYLESTERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P39298|protein.P39298]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8214`
- `QSPROTEOME:QS00198701`

## Notes

2*protein.P39298
