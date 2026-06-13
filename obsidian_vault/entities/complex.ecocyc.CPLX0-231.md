---
entity_id: "complex.ecocyc.CPLX0-231"
entity_type: "complex"
name: "galactitol-specific PTS enzyme II"
source_database: "EcoCyc"
source_id: "CPLX0-231"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EII<sup>Gat</sup>"
  - "Enzyme II <sup>Gat</sup>"
---

# galactitol-specific PTS enzyme II

`complex.ecocyc.CPLX0-231`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-231`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P69831|protein.P69831]], [[protein.P37188|protein.P37188]], [[protein.P69828|protein.P69828]]

## Enriched Summary

GatABC, the galactitol PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in ). GatABC takes up exogenous galactitol, releasing the phosphate ester into the cell cytoplasm in preparation for oxidation and further metabolism, primarily via a modified glycolytic pathway, the tagatose-6-P glycolytic pathway (GALACTITOLCAT-PWY). GatABC, the Enzyme IIGat complex, possesses three polypeptide chains, GatA (IIAGat), GatB (IIBGat) and GatC (IICGat). GatB is homologous to IIBSga and IIBSgc and shows limited sequence similarity to the IIB proteins of the lactose and cellobiose permeases (IIBLac and IIBCel) . gatC is predicted to encode a hydrophobic protein homologous to the SgcC (IICSgc) and shows limited sequence similarity to IICFru . gatA and gatB encode two small hydrophilic peptides . GatABC is a member of the PTS galactitol (Gat) family of transporters...

## Biological Role

Catalyzes TRANS-RXN-161 (reaction.ecocyc.TRANS-RXN-161), TRANS-RXN-169 (reaction.ecocyc.TRANS-RXN-169).

## Annotation

GatABC, the galactitol PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation (reviewed in ). GatABC takes up exogenous galactitol, releasing the phosphate ester into the cell cytoplasm in preparation for oxidation and further metabolism, primarily via a modified glycolytic pathway, the tagatose-6-P glycolytic pathway (GALACTITOLCAT-PWY). GatABC, the Enzyme IIGat complex, possesses three polypeptide chains, GatA (IIAGat), GatB (IIBGat) and GatC (IICGat). GatB is homologous to IIBSga and IIBSgc and shows limited sequence similarity to the IIB proteins of the lactose and cellobiose permeases (IIBLac and IIBCel) . gatC is predicted to encode a hydrophobic protein homologous to the SgcC (IICSgc) and shows limited sequence similarity to IICFru . gatA and gatB encode two small hydrophilic peptides . GatABC is a member of the PTS galactitol (Gat) family of transporters . The overall PTS-mediated phosphoryl transfer reaction, requiring the two general energy coupling proteins of the PTS, CPLX0-7938 "Enzyme I" (PtsI) and PTSH-MONOMER "HPr" (PtsH), as well as the three domains of the Enzyme II gat complex can be represented as: PEP → Enzyme I-Phis189 → HPr-Phis15 → Enzyme IIA-Phis62 → Enzyme IIB-Pcys9-(IIC) → galactitol-1-P GatABC transports galactitol with micromolar affinity. GatABC transports D-sorbitol with low affinity . The gat operon - gatYZABCDR - sequenced from a wild-type isolate of E. coli, strain EC3132, contains the gatY gene encoding tagatose 1,6-bis-P aldolase and the gatZ gene encoding tagatose 6-P kinase as well as gatD, the NAD-dependent galactitol

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-161|reaction.ecocyc.TRANS-RXN-161]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-169|reaction.ecocyc.TRANS-RXN-169]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P37188|protein.P37188]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P69828|protein.P69828]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P69831|protein.P69831]] `EcoCyc` `database` - EcoCyc component coefficient=2

## External IDs

- `EcoCyc:CPLX0-231`
- `QSPROTEOME:QS00219768`

## Notes

2*protein.P69831|1*protein.P37188|1*protein.P69828
