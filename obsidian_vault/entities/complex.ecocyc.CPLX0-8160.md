---
entity_id: "complex.ecocyc.CPLX0-8160"
entity_type: "complex"
name: "succinate:quinone oxidoreductase"
source_database: "EcoCyc"
source_id: "CPLX0-8160"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "complex II"
  - "succinate-ubiquinone oxidoreductase"
  - "SQR"
  - "SdhCDAB"
  - "succinate dehydrogenase"
  - "succinate-Q reductase"
---

# succinate:quinone oxidoreductase

`complex.ecocyc.CPLX0-8160`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8160`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.SUCC-DEHASE|complex.ecocyc.SUCC-DEHASE]]

## Enriched Summary

Succinate dehydrogenase or succinate:quinone oxidoreductase (SQR) catalyses the oxidation of succinate to fumarate concomitant with the reduction of ubiquinone to ubiquinol. SQR plays an important role in cellular metabolism and directly connects the the TCA-VARIANTS with the respiratory electron transport chain. As part of the TCA cycle succinate is oxidized to fumarate by SQR and electrons are transferred to the membrane quinone pool for entry into the electron transport chain. SQR does not contribute to the proton motive force (pmf); the sites of quinol reduction and succinate oxidation are both located on the cytoplasmic side of the membrane and there is no separation of charge across the membrane during catalysis (see ). E.coli SQR (SdhCDAB) is a membrane bound heterotetramer . Subunits SdhA and SdhB are hydrophilic and attached to the cytoplasmic surface of the plasma membrane via interactions with the two hydrophobic integral membrane subunits, SdhC and SdhD. SdhA contains the FAD cofactor and the dicarboxylic acid binding site . Electrons from the oxidation of succinate are transferred through the iron-sulphur protein, SdhB, to a quinone binding site located at the interface of the SdhB, SdhC and SdhD subunits . The SdhC and SdhD subunits each contain three transmembrane helices and anchor the complex to the membrane...

## Biological Role

Catalyzes SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN (reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN). Bound by FAD (molecule.C00016), Heme (molecule.C00032), a [3Fe-4S] iron-sulfur cluster (molecule.ecocyc.3FE-4S), a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

Succinate dehydrogenase or succinate:quinone oxidoreductase (SQR) catalyses the oxidation of succinate to fumarate concomitant with the reduction of ubiquinone to ubiquinol. SQR plays an important role in cellular metabolism and directly connects the the TCA-VARIANTS with the respiratory electron transport chain. As part of the TCA cycle succinate is oxidized to fumarate by SQR and electrons are transferred to the membrane quinone pool for entry into the electron transport chain. SQR does not contribute to the proton motive force (pmf); the sites of quinol reduction and succinate oxidation are both located on the cytoplasmic side of the membrane and there is no separation of charge across the membrane during catalysis (see ). E.coli SQR (SdhCDAB) is a membrane bound heterotetramer . Subunits SdhA and SdhB are hydrophilic and attached to the cytoplasmic surface of the plasma membrane via interactions with the two hydrophobic integral membrane subunits, SdhC and SdhD. SdhA contains the FAD cofactor and the dicarboxylic acid binding site . Electrons from the oxidation of succinate are transferred through the iron-sulphur protein, SdhB, to a quinone binding site located at the interface of the SdhB, SdhC and SdhD subunits . The SdhC and SdhD subunits each contain three transmembrane helices and anchor the complex to the membrane. A single heme b556 cofactor bridges the SdhC and SdhD subunits . Crystal structures and electrophoretic and spectrometric analyses indicate that E. coli SQR is organised into a trimeric supercomplex . SQR is structurally and functionally related to FUMARATE-REDUCTASE or menaquinol:fumarate reductase (QFR) which catalyses the reduction of fumarate to succinate under anaerobic conditions. The functions of SQR and QFR are partially interchangeable - a

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN|reaction.ecocyc.SUCCINATE-DEHYDROGENASE-UBIQUINONE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (10)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00032|molecule.C00032]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.3FE-4S|molecule.ecocyc.3FE-4S]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.SUCC-DEHASE|complex.ecocyc.SUCC-DEHASE]] `EcoCyc` `database` - EcoCyc component coefficient=3
- `is_component_of` <-- [[protein.P07014|protein.P07014]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` <-- [[protein.P0AC41|protein.P0AC41]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` <-- [[protein.P0AC44|protein.P0AC44]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3
- `is_component_of` <-- [[protein.P69054|protein.P69054]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-8160`
- `PDB:1NEN`
- `PDB:2WU5`
- `PDB:2WU2`
- `PDB:2WS3`
- `PDB:2WP9`
- `PDB:2WDV`
- `PDB:2WDR`
- `PDB:2WDQ`
- `QSPROTEOME:QS00175203`

## Notes

3*complex.ecocyc.SUCC-DEHASE
