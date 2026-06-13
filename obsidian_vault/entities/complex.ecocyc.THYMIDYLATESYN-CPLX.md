---
entity_id: "complex.ecocyc.THYMIDYLATESYN-CPLX"
entity_type: "complex"
name: "thymidylate synthase"
source_database: "EcoCyc"
source_id: "THYMIDYLATESYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# thymidylate synthase

`complex.ecocyc.THYMIDYLATESYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:THYMIDYLATESYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A884|protein.P0A884]]

## Enriched Summary

Thymidylate synthase plays a key role in DNA synthesis. The conversion of dUMP to dTMP is the main pathway of de novo dTMP synthesis in the cell. Thymidylate synthase catalyzes a complex multistep reaction, the reductive methylation of 2'-deoxyuridine-5'-monophosphate (dUMP) using the cosubstrate N5,N10-methylenetetrahydrofolate as a donor of both methylene and hydride, and producing dTMP and 7,8-dihydrofolate. Owing to this central metabolic function and thymidylate synthase's use as both an anticancer and antibacterial drug target, its reaction mechanism has been extensively investigated. The large number of structural and kinetic studies with wild type and mutant enzymes are only briefly summarized below. Many crystal structures of wild type and mutant thymidylate synthase in various quarternary complexes have been solved, enabling investigation of the reaction mechanism and inhibitors . The protein dynamics are being investigated by NMR . Thymidylate synthase is homodimeric; each of the subunits contributes to both active sites of the complex . Thymidylate synthase is a half-the-sites reactive enzyme (a type of negative cooperativity) . Initial studies found no allosteric effect at the level of substrate binding , but it was subsequently shown that binding of the second dUMP substrate causes perturbations in the first-bound active site...

## Biological Role

Catalyzes THYMIDYLATESYN-RXN (reaction.ecocyc.THYMIDYLATESYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Thymidylate synthase plays a key role in DNA synthesis. The conversion of dUMP to dTMP is the main pathway of de novo dTMP synthesis in the cell. Thymidylate synthase catalyzes a complex multistep reaction, the reductive methylation of 2'-deoxyuridine-5'-monophosphate (dUMP) using the cosubstrate N5,N10-methylenetetrahydrofolate as a donor of both methylene and hydride, and producing dTMP and 7,8-dihydrofolate. Owing to this central metabolic function and thymidylate synthase's use as both an anticancer and antibacterial drug target, its reaction mechanism has been extensively investigated. The large number of structural and kinetic studies with wild type and mutant enzymes are only briefly summarized below. Many crystal structures of wild type and mutant thymidylate synthase in various quarternary complexes have been solved, enabling investigation of the reaction mechanism and inhibitors . The protein dynamics are being investigated by NMR . Thymidylate synthase is homodimeric; each of the subunits contributes to both active sites of the complex . Thymidylate synthase is a half-the-sites reactive enzyme (a type of negative cooperativity) . Initial studies found no allosteric effect at the level of substrate binding , but it was subsequently shown that binding of the second dUMP substrate causes perturbations in the first-bound active site . Thymidylate synthase appears to be activated by an interaction with the ribosome . The enzyme undergoes conformational changes during the initial binding of dUMP, with even larger changes during the binding of the cosubstrate . Later results suggest that binding of the folate cosubstrate alone is responsible for the conformational transition to the catalytically competent structure . Newer structural data has led to reinterpretation

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.THYMIDYLATESYN-RXN|reaction.ecocyc.THYMIDYLATESYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A884|protein.P0A884]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:THYMIDYLATESYN-CPLX`
- `QSPROTEOME:QS00196889`

## Notes

2*protein.P0A884
