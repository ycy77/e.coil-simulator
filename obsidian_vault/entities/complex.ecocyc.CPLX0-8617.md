---
entity_id: "complex.ecocyc.CPLX0-8617"
entity_type: "complex"
name: "divalent metal ion transporter ZupT"
source_database: "EcoCyc"
source_id: "CPLX0-8617"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# divalent metal ion transporter ZupT

`complex.ecocyc.CPLX0-8617`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8617`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A8H3|protein.P0A8H3]]

## Enriched Summary

zupT encodes a broad specificity divalent metal ion transporter that mediates the uptake of zinc, iron, cadmium, cobalt, and manganese across the inner membrane . The energetics of transport are not clear; metal uptake is inhibited by the ionophores FCCP (carbonyl cyanide-p-trifluoromethoxyphenyl hydrazone) and CCCP (carbonyl cyanide m-chlorophenyl hydrazone) which is suggestive of a role for proton motive force (PMF) . ZupT contains two asymmetric metal-binding sites (M1 and M2) in its transmembrane region; M1 binds Zn2+ and Cd2+ with high affinity and Fe2+ with lower affinity while M2 binds Fe2+ with high affinity . Zn2+, the optimal substrate for ZupT, and Cd2+, a non-physiological substrate, are transported from the M1 site while Fe2+ is directly transported from the M2 site; Fe2+ slightly stimulates Zn2+ transport and ZupT may transport the two ions in parallel in order to maintain an optimal Zn2+ to Fe2+ ratio in the cytoplasm . In the Transporter Classification Database , ZupT is a member of the Zinc (Zn2+) - Iron (Fe2+) Permease (ZIP) family. ZupT is expressed constitutively at a low level as a monocistronic transcript . zupT encodes a broad specificity divalent metal ion transporter that mediates the uptake of zinc, iron, cadmium, cobalt, and manganese across the inner membrane...

## Biological Role

Catalyzes RXN0-10 (reaction.ecocyc.RXN0-10), RXN0-12 (reaction.ecocyc.RXN0-12), RXN0-16 (reaction.ecocyc.RXN0-16), TRANS-RXN-141A (reaction.ecocyc.TRANS-RXN-141A), TRANS-RXN-499 (reaction.ecocyc.TRANS-RXN-499), TRANS-RXN-8 (reaction.ecocyc.TRANS-RXN-8). Transports CO2 (molecule.C00011), Zinc cation (molecule.C00038), Fe2+ (molecule.C14818), Cd2+ (molecule.ecocyc.CD_2), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

zupT encodes a broad specificity divalent metal ion transporter that mediates the uptake of zinc, iron, cadmium, cobalt, and manganese across the inner membrane . The energetics of transport are not clear; metal uptake is inhibited by the ionophores FCCP (carbonyl cyanide-p-trifluoromethoxyphenyl hydrazone) and CCCP (carbonyl cyanide m-chlorophenyl hydrazone) which is suggestive of a role for proton motive force (PMF) . ZupT contains two asymmetric metal-binding sites (M1 and M2) in its transmembrane region; M1 binds Zn2+ and Cd2+ with high affinity and Fe2+ with lower affinity while M2 binds Fe2+ with high affinity . Zn2+, the optimal substrate for ZupT, and Cd2+, a non-physiological substrate, are transported from the M1 site while Fe2+ is directly transported from the M2 site; Fe2+ slightly stimulates Zn2+ transport and ZupT may transport the two ions in parallel in order to maintain an optimal Zn2+ to Fe2+ ratio in the cytoplasm . In the Transporter Classification Database , ZupT is a member of the Zinc (Zn2+) - Iron (Fe2+) Permease (ZIP) family. ZupT is expressed constitutively at a low level as a monocistronic transcript .

## Outgoing Edges (11)

- `catalyzes` --> [[reaction.ecocyc.RXN0-10|reaction.ecocyc.RXN0-10]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-12|reaction.ecocyc.RXN0-12]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-16|reaction.ecocyc.RXN0-16]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-141A|reaction.ecocyc.TRANS-RXN-141A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-499|reaction.ecocyc.TRANS-RXN-499]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-8|reaction.ecocyc.TRANS-RXN-8]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A8H3|protein.P0A8H3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-8617`
- `QSPROTEOME:QS00158159`

## Notes

2*protein.P0A8H3
