---
entity_id: "complex.ecocyc.CPLX-169"
entity_type: "complex"
name: "sorbitol-specific PTS enzyme II"
source_database: "EcoCyc"
source_id: "CPLX-169"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EII<sup>Gut</sup>"
  - "Enzyme II<sup>Gut</sup>"
  - "glucitol PTS permease"
---

# sorbitol-specific PTS enzyme II

`complex.ecocyc.CPLX-169`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-169`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P56579|protein.P56579]], [[protein.P05706|protein.P05706]], [[protein.P56580|protein.P56580]]

## Enriched Summary

SrlABE, also known as GutABE, is the sorbitol PTS permease which belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation. SrlAB takes up exogenous sorbitol, releasing the phosphate ester into the cell cytoplasm in preparation for oxidation to fructose-6-P and subsequent metabolism, primarily via glycolysis (reviewed in ). SrlABE comprises the Enzyme IISrl complex. The enzyme possesses a split IIC domain unlike all other characterized Enzyme II complexes of the PTS . SrlA is predicted to be an inner membrane protein containing 4 transmembrane (TM) regions. SrlE is a larger protein of 319 residues that includes the hydrophilic IIB domain fused to a hydrophobic domain containing 4 (putative) TM regions . SrlB is the hydrophilic IIA domain. Thus, the integral membrane IIC constituent of the sorbitol permease is split in half and encoded by two distinct genes, srlA and srlE. srlB and srlE, respectively, encode the IIA and IIB constituents. The IIB domain of SrlE and the IIA (SrlB) protein are localized to the cytoplasmic side of the membrane. SrlABE is a member of the PTS Glucitol (Gut) family of transporters...

## Biological Role

Catalyzes D-mannitol PTS permease (reaction.ecocyc.TRANS-RXN-156), TRANS-RXN-169 (reaction.ecocyc.TRANS-RXN-169).

## Annotation

SrlABE, also known as GutABE, is the sorbitol PTS permease which belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation. SrlAB takes up exogenous sorbitol, releasing the phosphate ester into the cell cytoplasm in preparation for oxidation to fructose-6-P and subsequent metabolism, primarily via glycolysis (reviewed in ). SrlABE comprises the Enzyme IISrl complex. The enzyme possesses a split IIC domain unlike all other characterized Enzyme II complexes of the PTS . SrlA is predicted to be an inner membrane protein containing 4 transmembrane (TM) regions. SrlE is a larger protein of 319 residues that includes the hydrophilic IIB domain fused to a hydrophobic domain containing 4 (putative) TM regions . SrlB is the hydrophilic IIA domain. Thus, the integral membrane IIC constituent of the sorbitol permease is split in half and encoded by two distinct genes, srlA and srlE. srlB and srlE, respectively, encode the IIA and IIB constituents. The IIB domain of SrlE and the IIA (SrlB) protein are localized to the cytoplasmic side of the membrane. SrlABE is a member of the PTS Glucitol (Gut) family of transporters . The overall PTS-mediated phosphoryl transfer reaction, requiring the two general energy coupling proteins of the PTS, CPLX0-7938 "Enzyme I" (PtsI) and PTSH-MONOMER "HPr" (PtsH), as well as the three domains of the Enzyme IIsorbitol complex can be represented by: PEP → Enzyme I-Phis189 → HPr-Phis15 → EnzymeIIA-Phis43 → Enzyme IIB-Pcys71-(Enyzme IIC) → sorbitol-6-P. The srl operon is induced by sorbitol and SrlABE transports sorbitol with low micromolar affinities. SrlABE

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-156|reaction.ecocyc.TRANS-RXN-156]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-169|reaction.ecocyc.TRANS-RXN-169]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P05706|protein.P05706]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P56579|protein.P56579]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P56580|protein.P56580]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX-169`
- `QSPROTEOME:QS00197863`

## Notes

1*protein.P56579|1*protein.P05706|1*protein.P56580
