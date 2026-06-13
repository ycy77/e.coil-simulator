---
entity_id: "complex.ecocyc.CPLX0-8013"
entity_type: "complex"
name: "UDP-N-acetyl-D-mannosamine dehydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-8013"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# UDP-N-acetyl-D-mannosamine dehydrogenase

`complex.ecocyc.CPLX0-8013`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8013`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P27829|protein.P27829]]

## Enriched Summary

UDP-N-acetyl-D-mannosamine dehydrogenase (WecC, RffD) is involved in the biosynthesis of enterobacterial common antigen (ECA) and catalyzes the second reaction in the synthesis of UDP-N-acetyl-mannosaminuronic acid (UDP-ManNAcA) . This reaction involves the oxidation of UDP-N-acetylmannosamine with concomitant reduction of 2 mol of NAD+/mol of UDP-ManNAcA produced; this activity was characterized in E. coli O14 K7 H- . Mutants defective in the synthesis of ECA were identified through transposon mutagenesis. The wecB and wecC genes are required for the synthesis of UDP-ManNAcA . The wec* mutation (an in-frame 6bp insertion) disrupts enzyme function and ECA is not detected in wecC* mutants; deletion of wecC partially restores the disrupted outer membrane function (and vancomycin resistance) of CPLX0-2201 tol-pal mutants; the accumulation of ECA intermediates (including novel diacylglycerol pyrophosphoryl (DAG-PP)-linked species) contributes to the rescue phenotype . Deletion of wecC enhances the motility defect of a pdeH ycgR double mutant . The Keio collection wecC mutant exhibits a 'low level' of resistance to lithium exposure . UDP-N-acetyl-D-mannosamine dehydrogenase (WecC, RffD) is involved in the biosynthesis of enterobacterial common antigen (ECA) and catalyzes the second reaction in the synthesis of UDP-N-acetyl-mannosaminuronic acid (UDP-ManNAcA)...

## Biological Role

Catalyzes UDPMANNACADEHYDROG-RXN (reaction.ecocyc.UDPMANNACADEHYDROG-RXN).

## Annotation

UDP-N-acetyl-D-mannosamine dehydrogenase (WecC, RffD) is involved in the biosynthesis of enterobacterial common antigen (ECA) and catalyzes the second reaction in the synthesis of UDP-N-acetyl-mannosaminuronic acid (UDP-ManNAcA) . This reaction involves the oxidation of UDP-N-acetylmannosamine with concomitant reduction of 2 mol of NAD+/mol of UDP-ManNAcA produced; this activity was characterized in E. coli O14 K7 H- . Mutants defective in the synthesis of ECA were identified through transposon mutagenesis. The wecB and wecC genes are required for the synthesis of UDP-ManNAcA . The wec* mutation (an in-frame 6bp insertion) disrupts enzyme function and ECA is not detected in wecC* mutants; deletion of wecC partially restores the disrupted outer membrane function (and vancomycin resistance) of CPLX0-2201 tol-pal mutants; the accumulation of ECA intermediates (including novel diacylglycerol pyrophosphoryl (DAG-PP)-linked species) contributes to the rescue phenotype . Deletion of wecC enhances the motility defect of a pdeH ycgR double mutant . The Keio collection wecC mutant exhibits a 'low level' of resistance to lithium exposure .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.UDPMANNACADEHYDROG-RXN|reaction.ecocyc.UDPMANNACADEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P27829|protein.P27829]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8013`
- `QSPROTEOME:QS00049561`

## Notes

2*protein.P27829
