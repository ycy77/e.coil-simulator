---
entity_id: "complex.ecocyc.IMP-DEHYDROG-CPLX"
entity_type: "complex"
name: "inosine 5'-monophosphate dehydrogenase"
source_database: "EcoCyc"
source_id: "IMP-DEHYDROG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# inosine 5'-monophosphate dehydrogenase

`complex.ecocyc.IMP-DEHYDROG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:IMP-DEHYDROG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ADG7|protein.P0ADG7]]

## Enriched Summary

IMP dehydrogenase (IMPDH) catalyzes the NAD+-dependent oxidation of IMP to XMP. This is the first committed, rate-limiting step in de novo guanine nucleotide biosynthesis in most organisms. Its importance has made it an enzyme of interest for the development of inhibitors, e.g. and reviewed in . IMPDH inhibition by nitric oxide (NO) and subsequent disruption of de novo purine biosynthesis is the underlying cause of NO's effects on cell division . IMPDH is a homotetrameric enzyme with four active sites per complex . The irreversible inhibitor EICARMP is covalently bound to Cys305 . Mutagenesis of conserved Asp and Glu residues enabled identification of functionally important carboxylates. A transition state analog, mizoribine 5'-monophosphate, was also identified . Residues important for monovalent cation activation were investigated by analysis of mutant enzymes . The IMP dehydrogenase reaction proceeds through formation of a covalent enzyme-substrate intermediate at the active site cysteine, which is hydrolyzed to produce XMP. An Asp338Ala mutant showed that Asp338 controls hydride transfer . IMPDH was identified as a phosphohistidine acceptor by using chemoproteomics analysis with a stable analogue of 3-pHis...

## Biological Role

Catalyzes IMP-DEHYDROG-RXN (reaction.ecocyc.IMP-DEHYDROG-RXN).

## Annotation

IMP dehydrogenase (IMPDH) catalyzes the NAD+-dependent oxidation of IMP to XMP. This is the first committed, rate-limiting step in de novo guanine nucleotide biosynthesis in most organisms. Its importance has made it an enzyme of interest for the development of inhibitors, e.g. and reviewed in . IMPDH inhibition by nitric oxide (NO) and subsequent disruption of de novo purine biosynthesis is the underlying cause of NO's effects on cell division . IMPDH is a homotetrameric enzyme with four active sites per complex . The irreversible inhibitor EICARMP is covalently bound to Cys305 . Mutagenesis of conserved Asp and Glu residues enabled identification of functionally important carboxylates. A transition state analog, mizoribine 5'-monophosphate, was also identified . Residues important for monovalent cation activation were investigated by analysis of mutant enzymes . The IMP dehydrogenase reaction proceeds through formation of a covalent enzyme-substrate intermediate at the active site cysteine, which is hydrolyzed to produce XMP. An Asp338Ala mutant showed that Asp338 controls hydride transfer . IMPDH was identified as a phosphohistidine acceptor by using chemoproteomics analysis with a stable analogue of 3-pHis . The evolutionarily conserved Bateman domain, consisting of a pair of cystathionine β-synthase (CBS) domains, is not required for catalytic function of IMPDH, but plays a role in the regulation of purine nucleotide metabolism. Deletion of the domain results in an increased ATP pool and changed ATP and GTP fluxes . The Bateman domain was subsequently concluded to be a negative trans-regulator of adenylate nucleotide synthesis, independent of IMPDH's catalytic role in the de novo synthesis of GMP . Evolved point mutations distant from the active site of IMPDH enabl

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.IMP-DEHYDROG-RXN|reaction.ecocyc.IMP-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ADG7|protein.P0ADG7]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:IMP-DEHYDROG-CPLX`
- `QSPROTEOME:QS00157893`

## Notes

4*protein.P0ADG7
