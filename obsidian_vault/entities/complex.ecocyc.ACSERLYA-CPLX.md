---
entity_id: "complex.ecocyc.ACSERLYA-CPLX"
entity_type: "complex"
name: "cysteine synthase A"
source_database: "EcoCyc"
source_id: "ACSERLYA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cysteine synthase A

`complex.ecocyc.ACSERLYA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACSERLYA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ABK5|protein.P0ABK5]]

## Enriched Summary

Cysteine synthase A (CysK), also known as O-acetylserine sulfhydrylase A, carries out the second step in the pathway of cysteine biosynthesis. In a PLP-dependent β elimination reaction, acetate is displaced from O-acetyl-L-serine by hydrogen sulfide to form L-cysteine . In the absence of a sulfur source, CysK can also catalyze the slow conversion of O-acetyl-L-serine into pyruvate, acetate, and ammonia, or the conversion of O-acetyl-L-serine into serine . The enzyme uses a ping-pong bi-bi mechanism of catalysis . Serine acetyltransferase (SAT), the first enzyme in the cysteine biosynthesis pathway, copurifies with CysK in a "cysteine synthase" complex . Formation of the cysteine synthase complex appears to protect against cold inactivation and proteolysis . Residues in CysK that are important for the interaction have been identified . Experiments suggest that complex formation involves an initial non-allosteric interaction between the C terminus of SAT and CysK, followed by at least two energetically favorable isomerizations that stabilize the complex and lead to inhibition of CysK . In the uropathogenic E. coli strain 536, the latent tRNase CdiA-CT (a contact-dependent growth inhibitor) binds to and is activated by CysK. Activation is not dependent on the O-acetylserine sulfhydrylase activity of CysK...

## Biological Role

Catalyzes ACSERLY-RXN (reaction.ecocyc.ACSERLY-RXN), LCYSDESULF-RXN (reaction.ecocyc.LCYSDESULF-RXN). Component of cysteine synthase complex (complex.ecocyc.CYSSYNMULTI-CPLX). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Cysteine synthase A (CysK), also known as O-acetylserine sulfhydrylase A, carries out the second step in the pathway of cysteine biosynthesis. In a PLP-dependent β elimination reaction, acetate is displaced from O-acetyl-L-serine by hydrogen sulfide to form L-cysteine . In the absence of a sulfur source, CysK can also catalyze the slow conversion of O-acetyl-L-serine into pyruvate, acetate, and ammonia, or the conversion of O-acetyl-L-serine into serine . The enzyme uses a ping-pong bi-bi mechanism of catalysis . Serine acetyltransferase (SAT), the first enzyme in the cysteine biosynthesis pathway, copurifies with CysK in a "cysteine synthase" complex . Formation of the cysteine synthase complex appears to protect against cold inactivation and proteolysis . Residues in CysK that are important for the interaction have been identified . Experiments suggest that complex formation involves an initial non-allosteric interaction between the C terminus of SAT and CysK, followed by at least two energetically favorable isomerizations that stabilize the complex and lead to inhibition of CysK . In the uropathogenic E. coli strain 536, the latent tRNase CdiA-CT (a contact-dependent growth inhibitor) binds to and is activated by CysK. Activation is not dependent on the O-acetylserine sulfhydrylase activity of CysK . A serendipidous observation led to the discovery that CysK strongly stimulates the synthesis of APS by SULFATE-ADENYLYLTRANS-CPLX by coupling the reaction to ATP hydrolysis . CysK provides one of the activities that is able to provide sulfur for Fe-S cluster biosynthesis in vitro, although the cysteine synthase reaction is catalyzed at a >100-fold greater rate than sulfur mobilization . CysK is one of at least five enzymes that exhibit cysteine desulfhydrase activity (CD

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ACSERLY-RXN|reaction.ecocyc.ACSERLY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.LCYSDESULF-RXN|reaction.ecocyc.LCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CYSSYNMULTI-CPLX|complex.ecocyc.CYSSYNMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ABK5|protein.P0ABK5]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ACSERLYA-CPLX`
- `QSPROTEOME:QS00150775`

## Notes

2*protein.P0ABK5
