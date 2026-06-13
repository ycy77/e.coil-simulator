---
entity_id: "complex.ecocyc.CPLX-157"
entity_type: "complex"
name: "glucose-specific PTS enzyme II"
source_database: "EcoCyc"
source_id: "CPLX-157"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EII<sup>glc</sup>"
  - "enzyme II <sup>glc</sup>"
---

# glucose-specific PTS enzyme II

`complex.ecocyc.CPLX-157`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-157`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P69786|protein.P69786]], [[protein.P69783|protein.P69783]]

## Enriched Summary

PtsG/Crr, the glucose-specific PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in . PtsG/Crr takes up exogenous glucose, releasing the phosphate ester into the cell cytoplasm in preparation for metabolism, primarily via glycolysis. It also transports and phosphorylates the non-metabolizable analogue methyl α-D-glucoside . PtsG/Crr is a member of the PTS Glucose-Glucoside family of transporters . The glucose PTS permease, PtsG, possesses two domains in a single polypeptide chain with the domain order IIC-IIB and it functions with an additional polypeptide chain, the Crr or Enzyme IIAglc protein. The overall PTS-mediated phosphoryl transfer reaction, requiring the two general energy coupling proteins of the PTS, CPLX0-7938 "Enzyme I" (PtsI) and PTSH-MONOMER "HPr" (PtsH), as well as the three domains of the Enzyme IIglc complex can be represented as: PEP → Enzyme I-Phis189 → HPr-Phis15 → Enzyme IIA-Phis90 → Enzyme IIB-Pcys421 - (Enzyme IIC) → glucose-6-P EIIglc activity is induced by growth in the presence of glucose...

## Biological Role

Catalyzes transport of β-D-glucose by PTS (reaction.ecocyc.TRANS-RXN-157), TRANS-RXN0-583 (reaction.ecocyc.TRANS-RXN0-583).

## Annotation

PtsG/Crr, the glucose-specific PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in . PtsG/Crr takes up exogenous glucose, releasing the phosphate ester into the cell cytoplasm in preparation for metabolism, primarily via glycolysis. It also transports and phosphorylates the non-metabolizable analogue methyl α-D-glucoside . PtsG/Crr is a member of the PTS Glucose-Glucoside family of transporters . The glucose PTS permease, PtsG, possesses two domains in a single polypeptide chain with the domain order IIC-IIB and it functions with an additional polypeptide chain, the Crr or Enzyme IIAglc protein. The overall PTS-mediated phosphoryl transfer reaction, requiring the two general energy coupling proteins of the PTS, CPLX0-7938 "Enzyme I" (PtsI) and PTSH-MONOMER "HPr" (PtsH), as well as the three domains of the Enzyme IIglc complex can be represented as: PEP → Enzyme I-Phis189 → HPr-Phis15 → Enzyme IIA-Phis90 → Enzyme IIB-Pcys421 - (Enzyme IIC) → glucose-6-P EIIglc activity is induced by growth in the presence of glucose .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-157|reaction.ecocyc.TRANS-RXN-157]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-583|reaction.ecocyc.TRANS-RXN0-583]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P69783|protein.P69783]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P69786|protein.P69786]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX-157`
- `PDB:1O2F`
- `QSPROTEOME:QS00049471`

## Notes

2*protein.P69786|1*protein.P69783
