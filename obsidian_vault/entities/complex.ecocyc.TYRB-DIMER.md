---
entity_id: "complex.ecocyc.TYRB-DIMER"
entity_type: "complex"
name: "tyrosine aminotransferase"
source_database: "EcoCyc"
source_id: "TYRB-DIMER"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "tyrosine aminotransferase,  tyrosine-repressible, PLP-dependent"
---

# tyrosine aminotransferase

`complex.ecocyc.TYRB-DIMER`

## Static

- Type: `complex`
- Source: `EcoCyc:TYRB-DIMER`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P04693|protein.P04693]]

## Enriched Summary

Tyrosine aminotransferase (TyrB), also known as aromatic-amino acid aminotransferase, is a broad-specificity enzyme that catalyzes the final step in tyrosine, leucine, and phenylalanine biosynthesis. TyrB catalyzes the transamination of 2-ketoisocaproate, p-hydroxyphenylpyruvate, and phenylpyruvate to yield leucine, tyrosine, and phenylalanine, respectively . TyrB overlaps with the catalytic activities of BRANCHED-CHAINAMINOTRANSFER-CPLX (IlvE), which also produces leucine, and ASPAMINOTRANS-DIMER (AspC), which also produces phenylalanine. A mutation in tyrB inactivates the tyrosine-repressible aromatic-amino acid aminotransferase activity, whereas a tyrB-ilvE-aspC triple mutant eliminates the aromatic-amino acid aminotransferase activity . TyrB is 1,000-fold more active toward aromatic substrates than AspC . TyrB is repressible by two of its products, leucine and tyrosine, and a precursor in the leucine biosynthesis pathway, keto-isovalerate . The last case has been shown to occur by direct inhibition of TyrB enzymatic function . The mechanism of action of TyrB has been examined, especially around the PLP-binding site . The nature of TyrB substrate specificity has also been studied . Aminotransferase redundancy of TyrB is demonstrated by it's ability to complement alanine, aspartate and diaminopimelate (DAP) synthesis . TyrB exists as a dimer...

## Biological Role

Catalyzes 2.6.1.57-RXN (reaction.ecocyc.2.6.1.57-RXN), BRANCHED-CHAINAMINOTRANSFERLEU-RXN (reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN), RXN-10814 (reaction.ecocyc.RXN-10814), TYROSINE-AMINOTRANSFERASE-RXN (reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Tyrosine aminotransferase (TyrB), also known as aromatic-amino acid aminotransferase, is a broad-specificity enzyme that catalyzes the final step in tyrosine, leucine, and phenylalanine biosynthesis. TyrB catalyzes the transamination of 2-ketoisocaproate, p-hydroxyphenylpyruvate, and phenylpyruvate to yield leucine, tyrosine, and phenylalanine, respectively . TyrB overlaps with the catalytic activities of BRANCHED-CHAINAMINOTRANSFER-CPLX (IlvE), which also produces leucine, and ASPAMINOTRANS-DIMER (AspC), which also produces phenylalanine. A mutation in tyrB inactivates the tyrosine-repressible aromatic-amino acid aminotransferase activity, whereas a tyrB-ilvE-aspC triple mutant eliminates the aromatic-amino acid aminotransferase activity . TyrB is 1,000-fold more active toward aromatic substrates than AspC . TyrB is repressible by two of its products, leucine and tyrosine, and a precursor in the leucine biosynthesis pathway, keto-isovalerate . The last case has been shown to occur by direct inhibition of TyrB enzymatic function . The mechanism of action of TyrB has been examined, especially around the PLP-binding site . The nature of TyrB substrate specificity has also been studied . Aminotransferase redundancy of TyrB is demonstrated by it's ability to complement alanine, aspartate and diaminopimelate (DAP) synthesis . TyrB exists as a dimer . A crystal structure of TyrB with bound PLP has been determined to 3.5 Å resolution . TyrB has been shown to be useful in the preparation of enantiomerically pure β-heterocylic D-alanine derivatives by a chemo-enzymatic synthesis method. Such derivatives are of potential use in the pharmaceutical industry .

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.2.6.1.57-RXN|reaction.ecocyc.2.6.1.57-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10814|reaction.ecocyc.RXN-10814]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P04693|protein.P04693]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:TYRB-DIMER`
- `QSPROTEOME:QS00188673`

## Notes

2*protein.P04693
