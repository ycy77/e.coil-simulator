---
entity_id: "complex.ecocyc.ATPASE-1-CPLX"
entity_type: "complex"
name: "K+ transporting P-type ATPase"
source_database: "EcoCyc"
source_id: "ATPASE-1-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Kdp-ATPase"
---

# K+ transporting P-type ATPase

`complex.ecocyc.ATPASE-1-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ATPASE-1-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P36937|protein.P36937]], [[protein.P03959|protein.P03959]], [[protein.P03960|protein.P03960]], [[protein.P03961|protein.P03961]]

## Enriched Summary

The KdpFABC complex is a high affinity K+-uptake P-Type ATPase, induced when the availability of potassium ions becomes limiting . Purified, solubilised Kdp(F)ABC is a K+ dependent ATPase which has narrow specificity and high affinity for K+ and ATP; ATPase activity is inhibited by Tl+ when present in equimolar concentrations to K+; ATPase activity of the purified complex is inhibited by vanadate and a variety of other ATPase inhibitors . ATPase activity of the purified complex is stimulated 2.2 fold by NH4+; slightly stimulated by Rb+ and Na+ and inhibited by Cs+ and Li+ . Kdp-mediated K+ uptake can be observed in right-side-out membrane vesicles provided that ATP is generated inside . Purified, reconstituted Kdp-ATPase mediates electrogenic transport; during the reaction cycle positive charge is transported to the cytoplasmic side of the protein . KdpFABC purifies as a dimer; reconstituted, functional KdpFABC exists in a monomer/dimer equilibrium . Kdp mediated K+ uptake and KUP-MONOMER "Kup" mediated Cs+ uptake sustain cell growth under K+ limiting and Cs+ excess conditions . A crystal structure of KdpFA(G116R)BC in the nucleotide free state is available ; cryo-EM structures of the complex in varying states are also available . Different transport mechanisms have been proposed based on the structural features observed...

## Biological Role

Catalyzes TRANS-RXN-2 (reaction.ecocyc.TRANS-RXN-2). Transports Potassium cation (molecule.C00238), hν (molecule.ecocyc.Light).

## Annotation

The KdpFABC complex is a high affinity K+-uptake P-Type ATPase, induced when the availability of potassium ions becomes limiting . Purified, solubilised Kdp(F)ABC is a K+ dependent ATPase which has narrow specificity and high affinity for K+ and ATP; ATPase activity is inhibited by Tl+ when present in equimolar concentrations to K+; ATPase activity of the purified complex is inhibited by vanadate and a variety of other ATPase inhibitors . ATPase activity of the purified complex is stimulated 2.2 fold by NH4+; slightly stimulated by Rb+ and Na+ and inhibited by Cs+ and Li+ . Kdp-mediated K+ uptake can be observed in right-side-out membrane vesicles provided that ATP is generated inside . Purified, reconstituted Kdp-ATPase mediates electrogenic transport; during the reaction cycle positive charge is transported to the cytoplasmic side of the protein . KdpFABC purifies as a dimer; reconstituted, functional KdpFABC exists in a monomer/dimer equilibrium . Kdp mediated K+ uptake and KUP-MONOMER "Kup" mediated Cs+ uptake sustain cell growth under K+ limiting and Cs+ excess conditions . A crystal structure of KdpFA(G116R)BC in the nucleotide free state is available ; cryo-EM structures of the complex in varying states are also available . Different transport mechanisms have been proposed based on the structural features observed. Cardiolipin specifically stimulates the ATPase activity of the reconstituted transporter and a high-affinity binding site at the KdpA-KdpB interface has been identified . A decline in extracellular K+ concentration stimulates expression of kdpFABC and kdpFABC expression decreases with increasing extracellular K+ concentration . Kdp-mediated K+ uptake is inhibited by moderate (>2mM) concentrations of external K+ ; in K+ replete media phosphorylation of

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-2|reaction.ecocyc.TRANS-RXN-2]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P03959|protein.P03959]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P03960|protein.P03960]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P03961|protein.P03961]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P36937|protein.P36937]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ATPASE-1-CPLX`
- `PDB:5MRW`
- `PDB:6HRB`
- `PDB:6HRA`
- `PDB:7LC6`
- `PDB:7LC3`
- `PDB:7BH2`
- `PDB:7BH1`
- `PDB:7BGY`
- `QSPROTEOME:QS00138395`

## Notes

1*protein.P36937|1*protein.P03959|1*protein.P03960|1*protein.P03961
