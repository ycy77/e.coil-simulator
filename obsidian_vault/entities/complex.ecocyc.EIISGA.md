---
entity_id: "complex.ecocyc.EIISGA"
entity_type: "complex"
name: "L-ascorbate specific PTS enzyme II"
source_database: "EcoCyc"
source_id: "EIISGA"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EII<sup>Sga</sup>"
  - "EII<sup>Ula</sup>"
  - "Enzyme II<sup>Sga</sup>"
  - "Enzyme II<sup>Ula</sup>"
---

# L-ascorbate specific PTS enzyme II

`complex.ecocyc.EIISGA`

## Static

- Type: `complex`
- Source: `EcoCyc:EIISGA`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P69820|protein.P69820]], [[protein.P69822|protein.P69822]], [[protein.P39301|protein.P39301]]

## Enriched Summary

UlaABC, the L-ascorbate PTS permease belongs to the functional superfamily of the phosphoenolpyruvate (PEP) -dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in . The ascorbate PTS transporter takes up exogenous L-ascorbate, releasing the phosphate ester, L-ascorbate-6-phosphate, into the cell cytoplasm in preparation for metabolism . E. coli K-12 can ferment L-ascorbate only when it is supplied at low concentrations (ulaB encodes a predicted hydrophilic protein containing an Enzyme IIB PTS domain and ulaC contains an Enzyme IIA PTS domain . UlaABC is the only member of the distinct PTS L-ascorbate family of transporters . All three components of the L-ascorbate PTS transporter are necessary for the anaerobic uptake of L-ascorbate in vivo and the phosphorylation of L-ascorbate in vitro. The L-ascorbate PTS transporter requires the general PTS enzymes CPLX0-7938 "Enzyme I" (PtsI) and PTSH-MONOMER "HPr" (PtsH) for transport and phosphorylation of its substrate...

## Biological Role

Catalyzes RXN0-2461 (reaction.ecocyc.RXN0-2461).

## Annotation

UlaABC, the L-ascorbate PTS permease belongs to the functional superfamily of the phosphoenolpyruvate (PEP) -dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in . The ascorbate PTS transporter takes up exogenous L-ascorbate, releasing the phosphate ester, L-ascorbate-6-phosphate, into the cell cytoplasm in preparation for metabolism . E. coli K-12 can ferment L-ascorbate only when it is supplied at low concentrations (ulaB encodes a predicted hydrophilic protein containing an Enzyme IIB PTS domain and ulaC contains an Enzyme IIA PTS domain . UlaABC is the only member of the distinct PTS L-ascorbate family of transporters . All three components of the L-ascorbate PTS transporter are necessary for the anaerobic uptake of L-ascorbate in vivo and the phosphorylation of L-ascorbate in vitro. The L-ascorbate PTS transporter requires the general PTS enzymes CPLX0-7938 "Enzyme I" (PtsI) and PTSH-MONOMER "HPr" (PtsH) for transport and phosphorylation of its substrate . The overall PTS-mediated phosphoryl transfer reaction can be represented as: PEP → Enzyme I-Phis189 → HPR-Phis15 → Enzyme IIA-Phis68 → Enzyme IIB-Pcys9 - (Enzyme IIC) → L-ascorbate-6-phosphate ulaABC forms an operon with three other genes (ulaDEF) required for the utilisation of L-ascorbate . G7854 "ulaR" acts as the repressor of the ula regulon . The ula regulon is subject to glucose repression . A mutation of UlaA conferred lactoperoxidase tolerance by an unkown mechanism . ula: utilization of l-ascorbate

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2461|reaction.ecocyc.RXN0-2461]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P39301|protein.P39301]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P69820|protein.P69820]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P69822|protein.P69822]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:EIISGA`
- `QSPROTEOME:QS00049489`

## Notes

1*protein.P69820|1*protein.P69822|2*protein.P39301
