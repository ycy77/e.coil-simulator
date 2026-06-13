---
entity_id: "complex.ecocyc.CPLX0-7525"
entity_type: "complex"
name: "2-succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate synthase"
source_database: "EcoCyc"
source_id: "CPLX0-7525"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 2-succinyl-5-enolpyruvyl-6-hydroxy-3-cyclohexene-1-carboxylate synthase

`complex.ecocyc.CPLX0-7525`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7525`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P17109|protein.P17109]]

## Enriched Summary

The menD gene product catalyzes the first committed step in the biosynthesis of menaquinone. MenD was initially believed to generate CPD-9923 (SHCHC) from isochorismate and 2-oxoglutarate by concomitant decarboxylation of the latter and removal of a pyruvyl group . However, it was later shown that the real product of the enzyme is CPD-9924 (SEPHCHC) , and that a different enzyme, encoded by EG12438 menH, is responsible for the removal of pyruvate . MenD therefore catalyzes the Stetter-like 1,4-addition of 2-oxoglutarate to isochorismate. The substrate range of the enzyme has been investigated . It has been shown that CPD-9924 "SEPHCHC" also undergoes a spontaneous isomerization to CPD-26609 "iso-SEPHCHC", though it is still not known whether this isomer is also an acceptable substrate for MenH . The enzyme is a dimer in solution and shows cooperativity with respect to both substrates, isochorismate and 2-oxoglutarate . Dimer of dimers are formed in solution and are evident in the crystal structure, which also shows that two subunits contribute to each active site . Additional crystal structures of the enzyme in complex with oxoglutarate or ThDP have been solved . A two-stage reaction mechanism was proposed ; later it was shown that MenD follows a ping-pong bi-bi kinetic mechanism...

## Biological Role

Catalyzes 2.5.1.64-RXN (reaction.ecocyc.2.5.1.64-RXN). Bound by Thiamin diphosphate (molecule.C00068), Magnesium cation (molecule.C00305), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

The menD gene product catalyzes the first committed step in the biosynthesis of menaquinone. MenD was initially believed to generate CPD-9923 (SHCHC) from isochorismate and 2-oxoglutarate by concomitant decarboxylation of the latter and removal of a pyruvyl group . However, it was later shown that the real product of the enzyme is CPD-9924 (SEPHCHC) , and that a different enzyme, encoded by EG12438 menH, is responsible for the removal of pyruvate . MenD therefore catalyzes the Stetter-like 1,4-addition of 2-oxoglutarate to isochorismate. The substrate range of the enzyme has been investigated . It has been shown that CPD-9924 "SEPHCHC" also undergoes a spontaneous isomerization to CPD-26609 "iso-SEPHCHC", though it is still not known whether this isomer is also an acceptable substrate for MenH . The enzyme is a dimer in solution and shows cooperativity with respect to both substrates, isochorismate and 2-oxoglutarate . Dimer of dimers are formed in solution and are evident in the crystal structure, which also shows that two subunits contribute to each active site . Additional crystal structures of the enzyme in complex with oxoglutarate or ThDP have been solved . A two-stage reaction mechanism was proposed ; later it was shown that MenD follows a ping-pong bi-bi kinetic mechanism . During the reaction, a tetrahedral post-decarboxylation intermediate is formed; a mechanism for its formation has been proposed . Characterization of active site mutants further clarified their roles in substrate binding and catalysis . Glu55 is a strictly conserved residue; an E55Q mutant shows no detectable catalytic activity . Site-directed mutants in active site lysine and arginine residues as well as Ser32, Gln118 and Ile418 were generated and their catalytic properties were studied . St

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.5.1.64-RXN|reaction.ecocyc.2.5.1.64-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P17109|protein.P17109]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7525`
- `QSPROTEOME:QS00195623`

## Notes

2*protein.P17109
