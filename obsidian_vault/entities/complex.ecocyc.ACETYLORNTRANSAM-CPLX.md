---
entity_id: "complex.ecocyc.ACETYLORNTRANSAM-CPLX"
entity_type: "complex"
name: "N-acetylornithine aminotransferase / N-succinyldiaminopimelate aminotransferase"
source_database: "EcoCyc"
source_id: "ACETYLORNTRANSAM-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# N-acetylornithine aminotransferase / N-succinyldiaminopimelate aminotransferase

`complex.ecocyc.ACETYLORNTRANSAM-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACETYLORNTRANSAM-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P18335|protein.P18335]]

## Enriched Summary

N-acetylornithine aminotransferase / N-succinyldiaminopimelate aminotransferase (ArgD) is a bifunctional enzyme catalyzing amination steps in arginine and lysine biosynthesis. ArgD is able to catalyze the amination of N-acetyl-L-glutamate 5-semialdehyde to yield N-acetyl-L-ornithine and the amination of N-succinyl-2-amino-6-ketopimelate to yield N-succinyl-L,L-2,6-diaminopimelate . The two activities were originally identified separately as ArgD and DapC. ArgD was the name assigned to the acetylornithine transaminase activity that was identified both by mutation and via characterization of the enzyme . DapC was the name for the N-succinyldiaminopimelate aminotransferase activity that was purified and characterized from E. coli W but not cloned . Eventual purification from E. coli K-12 and sequencing of a protein with DapC activity showed it to be identical to ArgD . Additional experiments showed that at least two proteins can catalyze the N-succinyldiaminopimelate aminotransferase (SDAP-AT, DapC) reaction , and a ΔargD mutant of E. coli K-12 (W3110) still contains approximately 8% of wild type N-acetylornithine aminotransferase (ACOAT) activity , indicating redundancy and promiscuity among aminotransferase enzymes. Four enzymes, ArgD, AstC, GabT, and PuuE, show some level of ACOAT activity involved in arginine biosynthesis...

## Biological Role

Catalyzes ACETYLORNTRANSAM-RXN (reaction.ecocyc.ACETYLORNTRANSAM-RXN), SUCCINYLDIAMINOPIMTRANS-RXN (reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

N-acetylornithine aminotransferase / N-succinyldiaminopimelate aminotransferase (ArgD) is a bifunctional enzyme catalyzing amination steps in arginine and lysine biosynthesis. ArgD is able to catalyze the amination of N-acetyl-L-glutamate 5-semialdehyde to yield N-acetyl-L-ornithine and the amination of N-succinyl-2-amino-6-ketopimelate to yield N-succinyl-L,L-2,6-diaminopimelate . The two activities were originally identified separately as ArgD and DapC. ArgD was the name assigned to the acetylornithine transaminase activity that was identified both by mutation and via characterization of the enzyme . DapC was the name for the N-succinyldiaminopimelate aminotransferase activity that was purified and characterized from E. coli W but not cloned . Eventual purification from E. coli K-12 and sequencing of a protein with DapC activity showed it to be identical to ArgD . Additional experiments showed that at least two proteins can catalyze the N-succinyldiaminopimelate aminotransferase (SDAP-AT, DapC) reaction , and a ΔargD mutant of E. coli K-12 (W3110) still contains approximately 8% of wild type N-acetylornithine aminotransferase (ACOAT) activity , indicating redundancy and promiscuity among aminotransferase enzymes. Four enzymes, ArgD, AstC, GabT, and PuuE, show some level of ACOAT activity involved in arginine biosynthesis. On minimal medium lacking arginine, single argD or astC mutants have subtle growth defects, and an argD astC double mutant has a slower doubling time than wild type. An argD astC gabT triple mutant does not grow on medium lacking arginine. Accumulation of suppressor mutations eventually allows growth of the triple mutant; an additional deletion of puuE eliminates this effect . The normal activities of two enzymes, ArgD and SerC, are sufficient for su

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ACETYLORNTRANSAM-RXN|reaction.ecocyc.ACETYLORNTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN|reaction.ecocyc.SUCCINYLDIAMINOPIMTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P18335|protein.P18335]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ACETYLORNTRANSAM-CPLX`
- `QSPROTEOME:QS00182671`

## Notes

2*protein.P18335
