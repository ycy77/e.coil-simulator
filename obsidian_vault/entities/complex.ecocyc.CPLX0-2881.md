---
entity_id: "complex.ecocyc.CPLX0-2881"
entity_type: "complex"
name: "Lon protease"
source_database: "EcoCyc"
source_id: "CPLX0-2881"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Lon protease

`complex.ecocyc.CPLX0-2881`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2881`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A9M0|protein.P0A9M0]]

## Enriched Summary

Intracellular proteases enforce protein quality control and modify the proteome composition in response to environmental and nutritional cues. Most targeted proteolysis in bacteria is performed by a group of proteases that was named the AAA+ family (ATPases Associated with various cellular Activities) . All of these proteins contain ring-shaped hexamers that use energy from ATP hydrolysis to unfold protein substrates, followed by translocation of the unfolded chains through a central channel into a degradation chamber, where they are degraded. TAX-562 encodes five AAA+ proteases: CPLX0-2982 FtsH, CPLX0-3107 ClpXP, CPLX0-3104 ClpAP, EG10542-MONOMER Lon, and CPLX0-1163 HslUV . Lon is an ATP-dependent protease responsible for degradation of misfolded proteins as well as a number of rapidly degraded regulatory proteins. Key regulatory proteins that are Lon substrates include the cell division regulator SulA , the capsule synthesis regulator RcsA and possibly TER components involved in blocking septation sites during the SOS response . Lon is required for degradation of misfolded proteins and the prevention of aggregate formation . In the absence of Lon function, aggregation triples . At least some of this degradation of misfolded proteins depends on the chaperone DnaK...

## Biological Role

Catalyzes 3.4.21.53-RXN (reaction.ecocyc.3.4.21.53-RXN).

## Annotation

Intracellular proteases enforce protein quality control and modify the proteome composition in response to environmental and nutritional cues. Most targeted proteolysis in bacteria is performed by a group of proteases that was named the AAA+ family (ATPases Associated with various cellular Activities) . All of these proteins contain ring-shaped hexamers that use energy from ATP hydrolysis to unfold protein substrates, followed by translocation of the unfolded chains through a central channel into a degradation chamber, where they are degraded. TAX-562 encodes five AAA+ proteases: CPLX0-2982 FtsH, CPLX0-3107 ClpXP, CPLX0-3104 ClpAP, EG10542-MONOMER Lon, and CPLX0-1163 HslUV . Lon is an ATP-dependent protease responsible for degradation of misfolded proteins as well as a number of rapidly degraded regulatory proteins. Key regulatory proteins that are Lon substrates include the cell division regulator SulA , the capsule synthesis regulator RcsA and possibly TER components involved in blocking septation sites during the SOS response . Lon is required for degradation of misfolded proteins and the prevention of aggregate formation . In the absence of Lon function, aggregation triples . At least some of this degradation of misfolded proteins depends on the chaperone DnaK . Lon also degrades the lambda phage N and Xis proteins, with degradation of the latter promoting lysogeny over lysis . Other substrates include HU1 in the absence of its partner HU2, HemA and DAM methylase . Lon degrades RNase R , Sxy , the small heat-shock proteins IbpA and IbpB , the transposase InsAB of the insertion element IS1 , SoxS , MarA , GadE , and tmRNA-tagged proteins . Lon is involved in quality control of the molybdoenzyme TorA, degrading its apo form but not its holo form . Lon appears to have

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.21.53-RXN|reaction.ecocyc.3.4.21.53-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9M0|protein.P0A9M0]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-2881`
- `QSPROTEOME:QS00181955`

## Notes

6*protein.P0A9M0
