---
entity_id: "complex.ecocyc.NADH-DHI-CPLX"
entity_type: "complex"
name: "NADH:quinone oxidoreductase I"
source_database: "EcoCyc"
source_id: "NADH-DHI-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "NDH-1"
  - "NADH dhI"
  - "complex I"
  - "NADH dehydrogenase I"
---

# NADH:quinone oxidoreductase I

`complex.ecocyc.NADH-DHI-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:NADH-DHI-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AFC3|protein.P0AFC3]], [[protein.P0AFD4|protein.P0AFD4]], [[protein.P0AFE0|protein.P0AFE0]], [[protein.P0AFE4|protein.P0AFE4]], [[protein.P33607|protein.P33607]], [[protein.P0AFE8|protein.P0AFE8]], [[protein.P0AFF0|protein.P0AFF0]], [[complex.ecocyc.CPLX0-3361|complex.ecocyc.CPLX0-3361]]

## Enriched Summary

NADH:ubiquinone oxidoreductase I (NDH-1) is an NADH dehydrogenase that catalyzes the transfer of electrons from NADH to the quinone pool in the cytoplasmic membrane and is able to generate a proton electrochemical gradient. It is part of both the aerobic and anaerobic respiratory chain of the cell. The study of this enzyme is of great interest, because it is considered to be a structurally minimal form of a proton-pumping NADH:ubiquinone oxidoreductase and serves as a model for the more complex mitochondrial enzyme. NDH-1 is one of two distinct NADH dehydrogenases in E. coli. In contrast to NADH-DHII-MONOMER NDH-2 (encoded by ndh), NDH-1-catalyzed electron flow from NADH to ubiquinone generates an electrochemical gradient. Depending on the strain, NDH-2 utilizes NADH exclusively, while NDH-1 can utilize both NADH and d-NADH, which enables specific assays of the enzyme . NDH-1 appears to exist in a resting and an active form . A conformational change upon activation was mapped to the junction of the hydrophilic and membrane domains. A tightly bound ubiquinone is reduced in the resting form, and a loosely bound ubiquinol can be exchanged with pool quinones in the active form . Activation of NDH-1 appears to depend on conversion from a state where NADH dehydrogenation is decoupled from proton pumping to a coupled state where proton pumping occurs...

## Biological Role

Catalyzes NADH-DEHYDROG-A-RXN (reaction.ecocyc.NADH-DEHYDROG-A-RXN), RXN0-5388 (reaction.ecocyc.RXN0-5388). Bound by FMN (molecule.C00061), Magnesium cation (molecule.C00305), Ca2+ (molecule.ecocyc.CA_2), a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

NADH:ubiquinone oxidoreductase I (NDH-1) is an NADH dehydrogenase that catalyzes the transfer of electrons from NADH to the quinone pool in the cytoplasmic membrane and is able to generate a proton electrochemical gradient. It is part of both the aerobic and anaerobic respiratory chain of the cell. The study of this enzyme is of great interest, because it is considered to be a structurally minimal form of a proton-pumping NADH:ubiquinone oxidoreductase and serves as a model for the more complex mitochondrial enzyme. NDH-1 is one of two distinct NADH dehydrogenases in E. coli. In contrast to NADH-DHII-MONOMER NDH-2 (encoded by ndh), NDH-1-catalyzed electron flow from NADH to ubiquinone generates an electrochemical gradient. Depending on the strain, NDH-2 utilizes NADH exclusively, while NDH-1 can utilize both NADH and d-NADH, which enables specific assays of the enzyme . NDH-1 appears to exist in a resting and an active form . A conformational change upon activation was mapped to the junction of the hydrophilic and membrane domains. A tightly bound ubiquinone is reduced in the resting form, and a loosely bound ubiquinol can be exchanged with pool quinones in the active form . Activation of NDH-1 appears to depend on conversion from a state where NADH dehydrogenation is decoupled from proton pumping to a coupled state where proton pumping occurs . The mechanism that couples electron transfer with proton pumping involves a catalytically important quinol anion . The FMN binding constant is significantly lower for the oxidized NDH-1 (femto- to picomolar) than for the NADH-reduced enzyme (nanomolar). FMN's ability to reversibly dissociate from the enzyme is linked to the relatively high redox potential of the off-pathway N1a iron-sulfur cluster . The presence of the N1a clust

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.NADH-DEHYDROG-A-RXN|reaction.ecocyc.NADH-DEHYDROG-A-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5388|reaction.ecocyc.RXN0-5388]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (19)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.CPLX0-3361|complex.ecocyc.CPLX0-3361]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0AFC3|protein.P0AFC3]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AFC7|protein.P0AFC7]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AFD1|protein.P0AFD1]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AFD4|protein.P0AFD4]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AFD6|protein.P0AFD6]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AFE0|protein.P0AFE0]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AFE4|protein.P0AFE4]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AFE8|protein.P0AFE8]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AFF0|protein.P0AFF0]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P31979|protein.P31979]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P33599|protein.P33599]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P33602|protein.P33602]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P33607|protein.P33607]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:NADH-DHI-CPLX`
- `PDB:7NYV`
- `PDB:7NYU`
- `PDB:7NYR`
- `PDB:7NYH`
- `PDB:7NYV`
- `PDB:7NYU`
- `PDB:7NYR`
- `PDB:3M9C`
- `QSPROTEOME:QS00169131`

## Notes

1*protein.P0AFC3|1*protein.P0AFD4|1*protein.P0AFE0|1*protein.P0AFE4|1*protein.P33607|1*protein.P0AFE8|1*protein.P0AFF0|1*complex.ecocyc.CPLX0-3361
