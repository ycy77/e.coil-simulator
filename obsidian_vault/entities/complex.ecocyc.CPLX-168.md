---
entity_id: "complex.ecocyc.CPLX-168"
entity_type: "complex"
name: "trehalose-specific PTS enzyme II"
source_database: "EcoCyc"
source_id: "CPLX-168"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EII<sup>Tre</sup>"
  - "Enzyme II <sup>Tre</sup>"
---

# trehalose-specific PTS enzyme II

`complex.ecocyc.CPLX-168`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-168`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P36672|protein.P36672]], [[protein.P69783|protein.P69783]]

## Enriched Summary

TreB, the trehalose PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in ). TreB together with CRR-MONOMER "Crr" (Enzyme IIAGlc or Enzyme IIACrr) takes up exogenous trehalose, releasing the phosphate ester into the cell cytoplasm for hydrolysis by catabolic TRE6PHYDRO-MONOMER "trehalose-6-phosphate hydrolase" and subsequent metabolism via glycolysis (see TREDEGLOW-PWY. TreB, the Enzyme IITre complex, possesses two domains in a single polypeptide chain with the domain order IIB-IIC . The IIC domain is predicted to contain 8 membrane spanning regions and to function as the permease proper. The IIB domain is localized to the cytoplasmic side of the membrane and contains characteristic amino acid sequence motifs that are believed to be involved in phosphoryl transfer . TreB does not contain an Enzyme IIA domain but relies on the soluble protein Enzyme IIACrr for this function. TreB/Crr is a member of the PTS Glucose-Glucoside family of transporters...

## Biological Role

Catalyzes TRANS-RXN-168 (reaction.ecocyc.TRANS-RXN-168).

## Annotation

TreB, the trehalose PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in ). TreB together with CRR-MONOMER "Crr" (Enzyme IIAGlc or Enzyme IIACrr) takes up exogenous trehalose, releasing the phosphate ester into the cell cytoplasm for hydrolysis by catabolic TRE6PHYDRO-MONOMER "trehalose-6-phosphate hydrolase" and subsequent metabolism via glycolysis (see TREDEGLOW-PWY. TreB, the Enzyme IITre complex, possesses two domains in a single polypeptide chain with the domain order IIB-IIC . The IIC domain is predicted to contain 8 membrane spanning regions and to function as the permease proper. The IIB domain is localized to the cytoplasmic side of the membrane and contains characteristic amino acid sequence motifs that are believed to be involved in phosphoryl transfer . TreB does not contain an Enzyme IIA domain but relies on the soluble protein Enzyme IIACrr for this function. TreB/Crr is a member of the PTS Glucose-Glucoside family of transporters . The overall PTS-mediated phosphoryl transfer reaction, requiring the two general energy coupling proteins of the PTS, CPLX0-7938 "Enzyme I" (PtsI) and PTSH-MONOMER "HPr" (PtsH), as well as the soluble Enzyme IIACrr protein and the two domains of the Enzyme IItre complex can be represented as: PEP --> Enzyme I-Phis189 --> HPr-Phis15 --> Enzyme IIAGlc-Phis91 --> Enzyme IIB-Pcys29-(Enzyme IIC) -> trehalose-6-P TreB transports trehalose with micromolar affinity . The tre operon is inducible in wild type E. coli K-12 by external trehelose and repressed at high osmolarity (250mM NaCl) . The treBC operon co

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-168|reaction.ecocyc.TRANS-RXN-168]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P36672|protein.P36672]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P69783|protein.P69783]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX-168`
- `QSPROTEOME:QS00049476`

## Notes

2*protein.P36672|1*protein.P69783
