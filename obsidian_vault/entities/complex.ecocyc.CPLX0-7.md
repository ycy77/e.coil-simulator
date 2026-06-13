---
entity_id: "complex.ecocyc.CPLX0-7"
entity_type: "complex"
name: "N-acetylmuramic acid-specific PTS enzyme II"
source_database: "EcoCyc"
source_id: "CPLX0-7"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Enzyme II<sup>NAcMur</sup>"
  - "EII<sup>NAcMur</sup>"
---

# N-acetylmuramic acid-specific PTS enzyme II

`complex.ecocyc.CPLX0-7`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77272|protein.P77272]], [[protein.P69783|protein.P69783]]

## Enriched Summary

MurP, the N-acetylmuramic acid PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in . murP encodes a protein containing Enyme IIB (EIIB) and Enzyme IIC (EIIC) domains. Strains lacking murP are unable to grown on N-acetylmuramic acid as the sole source of carbon. Strains lacking crr, which encodes an Enzyme IIA (EIIA) protein are also unable to grow on N-acetylmuramic acid indicating that MurP, which lacks an EIIA domain requires Crr for activity. Sequence analysis suggests that a conserved cysteine residue at position 29 is the site of phosphotransfer . MurP/Crr is a member of the PTS Glucose-Glucoside family of transporters . The product of MurP transport, N-acetyl-β-muramate 6-phosphate, is further degraded by the action of the CPLX0-7732 "MurQ etherase". The overall PTS-mediated phosphoryl transfer reaction, requiring the two general energy coupling proteins of the PTSsugar, CPLX0-7938 "PtsI" (Enzyme I) and PTSH-MONOMER "PtsH" (HPr), as well as the Crr protein and the two domains of the MurP protein can be represented as: PEP → Enzyme I-Phis189 → HPr-Phis15 → Enzyme IIAglc-Phis90 → Enzyme IIB-Pcys29 - (Enzyme IIC) → N-acetylmuramic acid-6-P...

## Biological Role

Catalyzes transport of N-acetyl-D-muramate (reaction.ecocyc.RXN0-17).

## Annotation

MurP, the N-acetylmuramic acid PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in . murP encodes a protein containing Enyme IIB (EIIB) and Enzyme IIC (EIIC) domains. Strains lacking murP are unable to grown on N-acetylmuramic acid as the sole source of carbon. Strains lacking crr, which encodes an Enzyme IIA (EIIA) protein are also unable to grow on N-acetylmuramic acid indicating that MurP, which lacks an EIIA domain requires Crr for activity. Sequence analysis suggests that a conserved cysteine residue at position 29 is the site of phosphotransfer . MurP/Crr is a member of the PTS Glucose-Glucoside family of transporters . The product of MurP transport, N-acetyl-β-muramate 6-phosphate, is further degraded by the action of the CPLX0-7732 "MurQ etherase". The overall PTS-mediated phosphoryl transfer reaction, requiring the two general energy coupling proteins of the PTSsugar, CPLX0-7938 "PtsI" (Enzyme I) and PTSH-MONOMER "PtsH" (HPr), as well as the Crr protein and the two domains of the MurP protein can be represented as: PEP → Enzyme I-Phis189 → HPr-Phis15 → Enzyme IIAglc-Phis90 → Enzyme IIB-Pcys29 - (Enzyme IIC) → N-acetylmuramic acid-6-P.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-17|reaction.ecocyc.RXN0-17]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P69783|protein.P69783]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P77272|protein.P77272]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-7`
- `QSPROTEOME:QS00049399`

## Notes

1*protein.P77272|1*protein.P69783
