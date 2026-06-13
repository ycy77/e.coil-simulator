---
entity_id: "complex.ecocyc.CPLX-165"
entity_type: "complex"
name: "mannose-specific PTS enzyme II"
source_database: "EcoCyc"
source_id: "CPLX-165"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "EII<sup>man</sup>"
  - "Enzyme II <sup>mannose</sup>"
---

# mannose-specific PTS enzyme II

`complex.ecocyc.CPLX-165`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX-165`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P69805|protein.P69805]], [[protein.P69801|protein.P69801]], [[protein.P69797|protein.P69797]]

## Enriched Summary

ManXYZ, the mannose PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation. ManXYZ takes up exogenous hexoses (mannose, glucose, glucosamine, fructose, N-acetylglucosamine, etc.), releasing the phosphate esters into the cell cytoplasm in preparation for metabolism, primarily via glycolysis (reviewed in ). The mannose transporter also transports and phosphorylates the non-metabolizable analogues 2-deoxyglucose and mannosamine . The mannose transporter acts as a host factor required for the infection of E. coli by λ phage . ManY and ManZ alone are sufficient for λ phage infection . ManXYZ, also known as the Enzyme IIMan complex, possesses four domains in three polypeptide chains, ManX=IIABMan, ManY=IICMan and ManZ=IIDMan. They are members of the PTS Mannose-Fructose-Sorbose Family (Man Family), the "splinter group", which is not homologous to most other PTS permeases . ManY and ManZ are integral membrane proteins which together constitute the transmembrane channel ; ManX is a cytoplasmic protein that associates with the ManYZ permease and mediates phosphoryl group transfer from HPr to the incoming sugar...

## Biological Role

Catalyzes transport of β-D-glucose by PTS (reaction.ecocyc.TRANS-RXN-157), TRANS-RXN-158A (reaction.ecocyc.TRANS-RXN-158A), TRANS-RXN-165 (reaction.ecocyc.TRANS-RXN-165), TRANS-RXN-167 (reaction.ecocyc.TRANS-RXN-167), TRANS-RXN-167A (reaction.ecocyc.TRANS-RXN-167A), TRANS-RXN0-446 (reaction.ecocyc.TRANS-RXN0-446), TRANS-RXN0-540 (reaction.ecocyc.TRANS-RXN0-540). Transports D-Fructose (molecule.C00095), N-Acetyl-D-glucosamine 6-phosphate (molecule.C00357), N-Acetyl-D-mannosamine (molecule.C00645), 2-deoxy-D-glucose 6-phosphate (molecule.ecocyc.2-DEOXY-D-GLUCOSE-6-PHOSPHATE).

## Annotation

ManXYZ, the mannose PTS permease, belongs to the functional superfamily of the phosphoenolpyruvate (PEP)-dependent, sugar transporting phosphotransferase system (PTSsugar). The PTSsugar transports and simultaneously phosphorylates its sugar substrates in a process called group translocation. ManXYZ takes up exogenous hexoses (mannose, glucose, glucosamine, fructose, N-acetylglucosamine, etc.), releasing the phosphate esters into the cell cytoplasm in preparation for metabolism, primarily via glycolysis (reviewed in ). The mannose transporter also transports and phosphorylates the non-metabolizable analogues 2-deoxyglucose and mannosamine . The mannose transporter acts as a host factor required for the infection of E. coli by λ phage . ManY and ManZ alone are sufficient for λ phage infection . ManXYZ, also known as the Enzyme IIMan complex, possesses four domains in three polypeptide chains, ManX=IIABMan, ManY=IICMan and ManZ=IIDMan. They are members of the PTS Mannose-Fructose-Sorbose Family (Man Family), the "splinter group", which is not homologous to most other PTS permeases . ManY and ManZ are integral membrane proteins which together constitute the transmembrane channel ; ManX is a cytoplasmic protein that associates with the ManYZ permease and mediates phosphoryl group transfer from HPr to the incoming sugar . The cryo-electron microscopic structure of purified ManYZ is a trimer of ManYZ protomers; ManY and ManZ structures each onsist of core, arm and V-motif domains; the two core domains in each protomer form the substrate binding site; ManYZ structure is consistent with an 'elevator mechanism' for sugar transport . The inner membrane components of the mannose PTS permease also catalyse sugar phosphate:sugar transphosphorylation (group exchange translocation) . T

## Outgoing Edges (11)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-157|reaction.ecocyc.TRANS-RXN-157]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-158A|reaction.ecocyc.TRANS-RXN-158A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-165|reaction.ecocyc.TRANS-RXN-165]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-167|reaction.ecocyc.TRANS-RXN-167]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-167A|reaction.ecocyc.TRANS-RXN-167A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-446|reaction.ecocyc.TRANS-RXN0-446]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-540|reaction.ecocyc.TRANS-RXN0-540]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00095|molecule.C00095]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00357|molecule.C00357]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00645|molecule.C00645]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.2-DEOXY-D-GLUCOSE-6-PHOSPHATE|molecule.ecocyc.2-DEOXY-D-GLUCOSE-6-PHOSPHATE]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P69797|protein.P69797]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P69801|protein.P69801]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` <-- [[protein.P69805|protein.P69805]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## External IDs

- `EcoCyc:CPLX-165`
- `PDB:6K1H`
- `PDB:7DYR`
- `QSPROTEOME:QS00049475`

## Notes

3*protein.P69805|3*protein.P69801|1*protein.P69797
