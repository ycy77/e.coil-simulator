---
entity_id: "complex.ecocyc.FUMARATE-REDUCTASE"
entity_type: "complex"
name: "fumarate reductase"
source_database: "EcoCyc"
source_id: "FUMARATE-REDUCTASE"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "menaquinol:fumarate oxidoreductase"
  - "FRD"
  - "QFR"
  - "fumarate reductase"
  - "quinol:fumarate oxidoreductase"
---

# fumarate reductase

`complex.ecocyc.FUMARATE-REDUCTASE`

## Static

- Type: `complex`
- Source: `EcoCyc:FUMARATE-REDUCTASE`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P00363|protein.P00363]], [[protein.P0AC47|protein.P0AC47]], [[protein.P0A8Q0|protein.P0A8Q0]], [[protein.P0A8Q3|protein.P0A8Q3]]

## Enriched Summary

Quinol:fumarate oxidoreductase (QFR) or fumarate reductase is a membrane bound flavoprotein that catalyses the reduction of fumarate to succinate under anaerobic conditions . QFR is a respiratory enzyme - it is one of a number of reductases that function as terminal electron acceptors during anaerobic respiration in E. coli K-12 (reviewed by ). Functional QFR is essential for anaerobic growth on glycerol, lactate or formate when fumarate serves as the terminal electron acceptor. It is also essential for anaerobic H2 dependent growth with fumarate. Menaquinol is the obligatory electron donor . Anaerobic growth of E. coli K-12 with fumarate operates preferentially with NADH dehydrogenase I . Fumarate reductase is composed of 4 subunits; the complex contains a cytoplasmic catalytic domain, FrdAB, containing bound flavin cofactor and three iron-sulfur clusters, and a membrane anchor domain, FrdCD, which contains the quinol binding site(s) . All 4 subunits are essential for anaerobic growth on glycerol and fumarate . The crystal structure of purified fumarate reductase contains two menaquinol molecules (Qp and Qd) bound on opposite sides of the membrane-spanning region; Qp is proximal to the site of fumarate reduction, Qd is distal. It is not clear whether both of the quinol-binding sites are functionally relevant...

## Biological Role

Catalyzes R601-RXN (reaction.ecocyc.R601-RXN). Bound by FAD (molecule.C00016), a [3Fe-4S] iron-sulfur cluster (molecule.ecocyc.3FE-4S), a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

Quinol:fumarate oxidoreductase (QFR) or fumarate reductase is a membrane bound flavoprotein that catalyses the reduction of fumarate to succinate under anaerobic conditions . QFR is a respiratory enzyme - it is one of a number of reductases that function as terminal electron acceptors during anaerobic respiration in E. coli K-12 (reviewed by ). Functional QFR is essential for anaerobic growth on glycerol, lactate or formate when fumarate serves as the terminal electron acceptor. It is also essential for anaerobic H2 dependent growth with fumarate. Menaquinol is the obligatory electron donor . Anaerobic growth of E. coli K-12 with fumarate operates preferentially with NADH dehydrogenase I . Fumarate reductase is composed of 4 subunits; the complex contains a cytoplasmic catalytic domain, FrdAB, containing bound flavin cofactor and three iron-sulfur clusters, and a membrane anchor domain, FrdCD, which contains the quinol binding site(s) . All 4 subunits are essential for anaerobic growth on glycerol and fumarate . The crystal structure of purified fumarate reductase contains two menaquinol molecules (Qp and Qd) bound on opposite sides of the membrane-spanning region; Qp is proximal to the site of fumarate reduction, Qd is distal. It is not clear whether both of the quinol-binding sites are functionally relevant . The 6 redox cofactors are organised in a chain with the sequence FAD - 2Fe:2S - 4Fe:4S - 3Fe:4S - Qp - Qd . QFR is structurally and functionally homologous to SUCC-DEHASE "succinate dehydrogenase" (SQR) which catalyses the oxidation of succinate to fumarate under aerobic conditions. The functions of QFR and SQR are partially interchangeable - a plasmid containing the frd genes is able to compensate for the growth deficiency of an sdh mutant while anaerobic expres

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.R601-RXN|reaction.ecocyc.R601-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (8)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.3FE-4S|molecule.ecocyc.3FE-4S]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P00363|protein.P00363]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A8Q0|protein.P0A8Q0]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A8Q3|protein.P0A8Q3]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AC47|protein.P0AC47]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:FUMARATE-REDUCTASE`
- `PDB:3P4S`
- `PDB:3P4R`
- `PDB:3P4Q`
- `PDB:3P4P`
- `PDB:3CIR`
- `PDB:2B76`
- `PDB:4KX6`
- `PDB:5VPN`
- `QSPROTEOME:QS00181281`

## Notes

1*protein.P00363|1*protein.P0AC47|1*protein.P0A8Q0|1*protein.P0A8Q3
