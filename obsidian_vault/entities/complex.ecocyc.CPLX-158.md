---
entity_id: "complex.ecocyc.CPLX-158"
entity_type: "complex"
name: "fructose-specific PTS enzyme II"
source_database: "EcoCyc"
source_id: "CPLX-158"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EII<sup>Fru</sup>"
  - "Enzyme II<sup>Fru</sup>"
  - "fructose PTS permease"
---

# fructose-specific PTS enzyme II

`complex.ecocyc.CPLX-158`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-158`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P69811|protein.P69811]], [[protein.P20966|protein.P20966]]

## Enriched Summary

FruAB, the fructose PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its substrates in a process called group translocation. FruAB takes up fructose, releasing the 1-phosphate ester into the cytoplasm in preparation for metabolism, primarily via glycolysis (reviewed in ). FruAB, also known as the Enzyme IIFru complex contains a unique combination of PTS domains with three domains in the FruA (IIB'-IIB-IIC) protein and three domains in the FruB protein (IIA-M-H). In the FruB protein, domain IIA contains the first phosphorylation site, M is a central domain of unknown function, and H (also known as pseudo HPr) substitutes for HPr in the phosphoryl transfer reaction . FruB is also known as the diphosphoryl transfer protein (DTP). The IIB and IIB' domains of the FruA protein are localized to the cytoplasmic side of the membrane. The IIB' domain may be required for binding of FruB to FruA . FruAB is a member of the PTS Fructose-Mannitol (Fru) family of transporters...

## Biological Role

Catalyzes TRANS-RXN-1567 (reaction.ecocyc.TRANS-RXN-1567), TRANS-RXN-158 (reaction.ecocyc.TRANS-RXN-158), Transport of D-fructopyranose (reaction.ecocyc.TRANS-RXN0-618). Transports D-Fructose (molecule.C00095), D-fructopyranose 1-phosphate (molecule.ecocyc.D-fructopyranose-1-phosphate), D-fructofuranose (molecule.ecocyc.Fructofuranose).

## Annotation

FruAB, the fructose PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its substrates in a process called group translocation. FruAB takes up fructose, releasing the 1-phosphate ester into the cytoplasm in preparation for metabolism, primarily via glycolysis (reviewed in ). FruAB, also known as the Enzyme IIFru complex contains a unique combination of PTS domains with three domains in the FruA (IIB'-IIB-IIC) protein and three domains in the FruB protein (IIA-M-H). In the FruB protein, domain IIA contains the first phosphorylation site, M is a central domain of unknown function, and H (also known as pseudo HPr) substitutes for HPr in the phosphoryl transfer reaction . FruB is also known as the diphosphoryl transfer protein (DTP). The IIB and IIB' domains of the FruA protein are localized to the cytoplasmic side of the membrane. The IIB' domain may be required for binding of FruB to FruA . FruAB is a member of the PTS Fructose-Mannitol (Fru) family of transporters . The overall PTS-mediated phosphoryl transfer reaction, requiring the general energy coupling protein of the PTS, CPLX0-7938 "Enzyme I" (PtsI) as well as the FruAB complex can be represented as: PEP → Enzyme I-Phis189 → Enzyme IIA-Phis299 → Enzyme IIA-Phis62 → Enzyme IIB-Pcys112 - (Enzyme IIC) → fructose-1-P. FruAB transports fructose with low micromolar affinity. FruAB transports mannose with low efficiency (Km > 5 mM). Mannose is taken up by the FruAB PTS to form mannose-6-phosphate . Overexpression of FruAB affects the uptake of other PTS sugars (mannitol, N-acetylglucosamine, methyl α-glucoside, 2-deoxyglucose, trehalose, and galactitol); this effect

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-1567|reaction.ecocyc.TRANS-RXN-1567]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-158|reaction.ecocyc.TRANS-RXN-158]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-618|reaction.ecocyc.TRANS-RXN0-618]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00095|molecule.C00095]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.D-fructopyranose-1-phosphate|molecule.ecocyc.D-fructopyranose-1-phosphate]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Fructofuranose|molecule.ecocyc.Fructofuranose]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P20966|protein.P20966]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P69811|protein.P69811]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX-158`
- `QSPROTEOME:QS00049472`

## Notes

1*protein.P69811|2*protein.P20966
