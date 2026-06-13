---
entity_id: "complex.ecocyc.CPLX0-1163"
entity_type: "complex"
name: "HslVU protease"
source_database: "EcoCyc"
source_id: "CPLX0-1163"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ClpYQ protease"
  - "HslUV protease"
---

# HslVU protease

`complex.ecocyc.CPLX0-1163`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1163`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[complex.ecocyc.CPLX0-1161|complex.ecocyc.CPLX0-1161]], [[complex.ecocyc.CPLX0-1162|complex.ecocyc.CPLX0-1162]]

## Enriched Summary

Intracellular proteases enforce protein quality control and modify the proteome composition in response to environmental and nutritional cues. Most targeted proteolysis in bacteria is performed by a group of proteases that was named the AAA+ family (ATPases Associated with various cellular Activities) . All of these proteins contain ring-shaped hexamers that use energy from ATP hydrolysis to unfold protein substrates, followed by translocation of the unfolded chains through a central channel into a degradation chamber, where they are degraded. TAX-562 encodes five AAA+ proteases: CPLX0-2982 FtsH, CPLX0-3107 ClpXP, CPLX0-3104 ClpAP, EG10542-MONOMER Lon, and CPLX0-1163 HslUV . The HslVU protease exhibits ATP-stimulated activity similar to that of the chymotrypsin-like activity of the eukaryotic proteasome . HslU and HslV form ring shaped complexes of protein hexamers that stack into a four-ring cylinder with HslU rings on each end and HslV rings in the center . Of the six potential ATP binding sites on an HslU hexamer only three or four molecules of ATP are bound at saturation. ATP binding controls the assembly and activity of the HslVU complex. The binding of a single molecule of ATP to HslU allows it to bind HslV, and binding of additional ATP molecules support substrate recognition and activate ATP hydrolysis which drives substrate unfolding and translocation...

## Biological Role

Catalyzes RXN0-5103 (reaction.ecocyc.RXN0-5103).

## Annotation

Intracellular proteases enforce protein quality control and modify the proteome composition in response to environmental and nutritional cues. Most targeted proteolysis in bacteria is performed by a group of proteases that was named the AAA+ family (ATPases Associated with various cellular Activities) . All of these proteins contain ring-shaped hexamers that use energy from ATP hydrolysis to unfold protein substrates, followed by translocation of the unfolded chains through a central channel into a degradation chamber, where they are degraded. TAX-562 encodes five AAA+ proteases: CPLX0-2982 FtsH, CPLX0-3107 ClpXP, CPLX0-3104 ClpAP, EG10542-MONOMER Lon, and CPLX0-1163 HslUV . The HslVU protease exhibits ATP-stimulated activity similar to that of the chymotrypsin-like activity of the eukaryotic proteasome . HslU and HslV form ring shaped complexes of protein hexamers that stack into a four-ring cylinder with HslU rings on each end and HslV rings in the center . Of the six potential ATP binding sites on an HslU hexamer only three or four molecules of ATP are bound at saturation. ATP binding controls the assembly and activity of the HslVU complex. The binding of a single molecule of ATP to HslU allows it to bind HslV, and binding of additional ATP molecules support substrate recognition and activate ATP hydrolysis which drives substrate unfolding and translocation. This thermodynamic hierarchy ensures efficient function of HslVU . HslV uses its N-terminal threonine as the active site residue. Mutagenesis studies showed that in the HslV dodecamer only approximately six of the twelve active site threonines are necessary to support full catalytic activity and to stabilize the interaction between HslV and HslU . The HslU hexamer portion of the HslVU complex recognizes and unfol

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5103|reaction.ecocyc.RXN0-5103]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-1161|complex.ecocyc.CPLX0-1161]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` <-- [[complex.ecocyc.CPLX0-1162|complex.ecocyc.CPLX0-1162]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` <-- [[protein.P0A6H5|protein.P0A6H5]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` <-- [[protein.P0A7B8|protein.P0A7B8]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12

## External IDs

- `EcoCyc:CPLX0-1163`
- `PDB:1E94`
- `PDB:1G4A`
- `PDB:1G4B`
- `PDB:1HQY`
- `PDB:1HT1`
- `PDB:1HT2`
- `PDB:5JI3`
- `PDB:6PXI`

## Notes

2*complex.ecocyc.CPLX0-1161|2*complex.ecocyc.CPLX0-1162
