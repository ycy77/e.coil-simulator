---
entity_id: "complex.ecocyc.CPLX-156"
entity_type: "complex"
name: "mannitol-specific PTS enzyme II CmtBA"
source_database: "EcoCyc"
source_id: "CPLX-156"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EII<sup>Cmt</sup>"
  - "Enzyme II<sup>Cmt</sup>"
---

# mannitol-specific PTS enzyme II CmtBA

`complex.ecocyc.CPLX-156`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-156`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P69824|protein.P69824]], [[protein.P69826|protein.P69826]]

## Enriched Summary

CmtBA, the "cryptic mannitol" PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its substrates in a process called group translocation (reviewed in ). cmtA and cmtB may encode a mannitol-like PTS permease. The two genes complement a mannitol-negative E. coli mutant when expressed using a heterologous promoter . The cmt genes have a lower G+C content than the mtlA operon . The overall PTS-mediated phosphoryl transfer reaction, requiring the two general energy coupling proteins of the PTS, CPLX0-7938 "Enzyme I" (PtsI) and PTSH-MONOMER "HPr" (PtsH), as well as the three domains of the Enzyme IICmt complex is: PEP → Enzyme I-Phis189 → HPr-Phis15 → Enzyme IIA-Phis67 → Enzyme IIB-Pcys377 - (Enzyme IIC) → sugar-P CmtBA, the "cryptic mannitol" PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its substrates in a process called group translocation (reviewed in ). cmtA and cmtB may encode a mannitol-like PTS permease. The two genes complement a mannitol-negative E. coli mutant when expressed using a heterologous promoter...

## Biological Role

Catalyzes D-mannitol PTS permease (reaction.ecocyc.TRANS-RXN-156).

## Annotation

CmtBA, the "cryptic mannitol" PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its substrates in a process called group translocation (reviewed in ). cmtA and cmtB may encode a mannitol-like PTS permease. The two genes complement a mannitol-negative E. coli mutant when expressed using a heterologous promoter . The cmt genes have a lower G+C content than the mtlA operon . The overall PTS-mediated phosphoryl transfer reaction, requiring the two general energy coupling proteins of the PTS, CPLX0-7938 "Enzyme I" (PtsI) and PTSH-MONOMER "HPr" (PtsH), as well as the three domains of the Enzyme IICmt complex is: PEP → Enzyme I-Phis189 → HPr-Phis15 → Enzyme IIA-Phis67 → Enzyme IIB-Pcys377 - (Enzyme IIC) → sugar-P

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-156|reaction.ecocyc.TRANS-RXN-156]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P69824|protein.P69824]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P69826|protein.P69826]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX-156`
- `QSPROTEOME:QS00049470`

## Notes

1*protein.P69824|1*protein.P69826
