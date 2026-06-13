---
entity_id: "complex.ecocyc.CPLX0-7938"
entity_type: "complex"
name: "PTS enzyme I"
source_database: "EcoCyc"
source_id: "CPLX0-7938"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Enzyme I"
  - "Enzyme I<sup>sugar</sup>"
  - "EI<sup>sugar</sup>"
  - "phosphoenolpyruvate-protein phosphotransferase PtsI"
---

# PTS enzyme I

`complex.ecocyc.CPLX0-7938`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7938`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P08839|protein.P08839]]

## Enriched Summary

PtsI (Enzyme I) is a cytoplasmic protein that serves as the gateway for the phosphoenolpyruvate:sugar phosphotransferase system (PTSsugar). PtsI is one of two (PtsI and PtsH) sugar non-specific protein constituents of the PTSsugar which along with a sugar-specific inner membrane permease effect a phosphotransfer cascade that results in the coupled phosphorylation and transport of a variety of carbohydrate substrates. PtsI purifies as a monomer and a homodimer; PtsI accepts a phosphoryl group from phosphoenolpyruvate (PEP) - on histidine residue 189 - and transfers it to the low molecular weight phosphocarrier protein HPr (also known as PtsH); activity requires the homodimeric form of PtsI and the presence of a divalent metal ion (Mg2+) . A chemoproteomics analysis with a stable analogue of 3-pHis also found PtsI to be a phosphohistidine acceptor . The monomer/dimer transition may play a role in regulating PtsI activity . The PtsI dimer accepts one phosphoryl group per subunit; the rate of dimerization is slow compared to the rate of phosphorylation . The PtsI monomer consists of a protease resistant N-terminal domain (E1N) which contains the active histidine residue and the HPr binding domain, and a C-terminal domain (E1C) which binds PEP and is required for dimerization...

## Biological Role

Catalyzes 2.7.3.9-RXN (reaction.ecocyc.2.7.3.9-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

PtsI (Enzyme I) is a cytoplasmic protein that serves as the gateway for the phosphoenolpyruvate:sugar phosphotransferase system (PTSsugar). PtsI is one of two (PtsI and PtsH) sugar non-specific protein constituents of the PTSsugar which along with a sugar-specific inner membrane permease effect a phosphotransfer cascade that results in the coupled phosphorylation and transport of a variety of carbohydrate substrates. PtsI purifies as a monomer and a homodimer; PtsI accepts a phosphoryl group from phosphoenolpyruvate (PEP) - on histidine residue 189 - and transfers it to the low molecular weight phosphocarrier protein HPr (also known as PtsH); activity requires the homodimeric form of PtsI and the presence of a divalent metal ion (Mg2+) . A chemoproteomics analysis with a stable analogue of 3-pHis also found PtsI to be a phosphohistidine acceptor . The monomer/dimer transition may play a role in regulating PtsI activity . The PtsI dimer accepts one phosphoryl group per subunit; the rate of dimerization is slow compared to the rate of phosphorylation . The PtsI monomer consists of a protease resistant N-terminal domain (E1N) which contains the active histidine residue and the HPr binding domain, and a C-terminal domain (E1C) which binds PEP and is required for dimerization . Purified, crystallized E1N consists of a helical HPr binding subdomain and an αβ subdomain that contains the active histidine . Purified E1N does not dimerize; purified E1N is phosphorylated by phospho-HPr but not by PEP . Purified E1C is dimeric and hydrolyses PEP into pyruvate and Pi; purified E1C exists in a dynamic equilibrium between open and closed conformation (later referred to as expanded and compact forms); PEP binding stabilizes the compact conformation . The catalytic cycle of PtsI is acco

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.3.9-RXN|reaction.ecocyc.2.7.3.9-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P08839|protein.P08839]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7938`
- `QSPROTEOME:QS00188591`

## Notes

2*protein.P08839
