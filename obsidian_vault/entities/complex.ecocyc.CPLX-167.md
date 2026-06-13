---
entity_id: "complex.ecocyc.CPLX-167"
entity_type: "complex"
name: "N-acetylglucosamine-specific PTS enzyme II"
source_database: "EcoCyc"
source_id: "CPLX-167"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EII<sup>Nag</sup>"
  - "Enzyme II <sup>N-acetyl glucosamine</sup>"
  - "EIICBA<sup>Nag</sup>"
---

# N-acetylglucosamine-specific PTS enzyme II

`complex.ecocyc.CPLX-167`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-167`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P09323|protein.P09323]]

## Enriched Summary

NagE, the N-acetylglucosamine PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in . NagE takes up exogenous N-acetylglucosamine, releasing the phosphate ester into the cell cytoplasm in preparation for metabolism, primarily via glycolysis (see GLUAMCAT-PWY). NagE, the Enzyme IINag complex, possesses three domains in a single polypeptide chain with the domain order IIC-IIB-IIA . It is homologous to PtsG/Crr (the glucose-specific PTS Enzyme II) . Hydropathy and sequence analysis suggests that the N-terminal region of NagE resides in the membrane. Histidine at position 569 and cysteine at position 412 are believed to be the sites of phosphorylation . NagE is a member of the PTS Glucose-Glucoside family of transporters . The overall PTS-mediated phosphoryl transfer reaction, requiring the two general energy coupling proteins of the PTS, CPLX0-7938 "Enzyme I" (PtsI) and PTSH-MONOMER "HPr" (PtsH), as well as the three domains of the Enzyme IINag complex can be represented as: PEP → Enzyme I-Phis189 → HPr-Phis15 → Enzyme IIA-Phis569 → Enzyme IIB-Pcys412-(Enzyme IIC) → N-acetylglucosamine-6-P...

## Biological Role

Catalyzes TRANS-RXN-167 (reaction.ecocyc.TRANS-RXN-167), TRANS-RXN-167A (reaction.ecocyc.TRANS-RXN-167A).

## Annotation

NagE, the N-acetylglucosamine PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in . NagE takes up exogenous N-acetylglucosamine, releasing the phosphate ester into the cell cytoplasm in preparation for metabolism, primarily via glycolysis (see GLUAMCAT-PWY). NagE, the Enzyme IINag complex, possesses three domains in a single polypeptide chain with the domain order IIC-IIB-IIA . It is homologous to PtsG/Crr (the glucose-specific PTS Enzyme II) . Hydropathy and sequence analysis suggests that the N-terminal region of NagE resides in the membrane. Histidine at position 569 and cysteine at position 412 are believed to be the sites of phosphorylation . NagE is a member of the PTS Glucose-Glucoside family of transporters . The overall PTS-mediated phosphoryl transfer reaction, requiring the two general energy coupling proteins of the PTS, CPLX0-7938 "Enzyme I" (PtsI) and PTSH-MONOMER "HPr" (PtsH), as well as the three domains of the Enzyme IINag complex can be represented as: PEP → Enzyme I-Phis189 → HPr-Phis15 → Enzyme IIA-Phis569 → Enzyme IIB-Pcys412-(Enzyme IIC) → N-acetylglucosamine-6-P. NagE transports N-acetylglucosamine with low micromolar affinity. It can also transport the antibiotic streptozotocin . Genetic studies suggest that the NagE PTS transporter plays a significant role in the recycling of peptidoglycan . Expression of the nagE monocistronic operon is regulated by PD00266 "NagC" together with the cyclic AMP-cyclic AMP receptor protein (CRP) complex .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-167|reaction.ecocyc.TRANS-RXN-167]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-167A|reaction.ecocyc.TRANS-RXN-167A]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P09323|protein.P09323]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX-167`
- `QSPROTEOME:QS00049692`

## Notes

2*protein.P09323
