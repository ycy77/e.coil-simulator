---
entity_id: "complex.ecocyc.SAMDECARB-CPLX"
entity_type: "complex"
name: "S-adenosylmethionine decarboxylase"
source_database: "EcoCyc"
source_id: "SAMDECARB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# S-adenosylmethionine decarboxylase

`complex.ecocyc.SAMDECARB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SAMDECARB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A7F6|protein.P0A7F6]], [[protein.P0A7F6|protein.P0A7F6]]

## Enriched Summary

S-adenosylmethionine decarboxylase is an important enzyme of polyamine biosynthesis in all domains of life. It has been extensively studied in microorganisms, plants and animals. It catalyzes the removal of the carboxylate group of S-adenosyl-L-methionine, producing S-adenosyl-L-methioninamine. This compound then acts as the n-propylamine group donor for the synthesis of spermidine from putrescine by SPERMIDINESYN-CPLX. Spermidine is an important negative regulator of adenosylmethionine decarboxylase, affecting the entire polyamine biosynthesis pathway. This enzyme belongs to a small class of decarboxylating enzymes that utilize covalently bound pyruvate (pyruvoyl group). Class 1 enzymes are found in bacteria and archaea, while Class 2 are found in eukaryotes. These two classes show almost no detectable sequence homology with each other and do not show similarity to other known pyruvoyl-dependent amino acid decarboxylases. Class 1A is enzymes are found primarily in Gram-negative bacteria, including E. coli while Class 1B are found in some Gram-positive bacteria and archaea. These two classes show only low levels of amino acid sequence similarity. A homology model of the core structure of the E. coli enzyme based on the crystal structures of the human (Class 2) and Thermotoga maritima (Class 1B) enzymes has been proposed . E...

## Biological Role

Catalyzes SAMDECARB-RXN (reaction.ecocyc.SAMDECARB-RXN). Bound by Magnesium cation (molecule.C00305), a pyruvoyl cofactor (molecule.ecocyc.CPD0-2654).

## Annotation

S-adenosylmethionine decarboxylase is an important enzyme of polyamine biosynthesis in all domains of life. It has been extensively studied in microorganisms, plants and animals. It catalyzes the removal of the carboxylate group of S-adenosyl-L-methionine, producing S-adenosyl-L-methioninamine. This compound then acts as the n-propylamine group donor for the synthesis of spermidine from putrescine by SPERMIDINESYN-CPLX. Spermidine is an important negative regulator of adenosylmethionine decarboxylase, affecting the entire polyamine biosynthesis pathway. This enzyme belongs to a small class of decarboxylating enzymes that utilize covalently bound pyruvate (pyruvoyl group). Class 1 enzymes are found in bacteria and archaea, while Class 2 are found in eukaryotes. These two classes show almost no detectable sequence homology with each other and do not show similarity to other known pyruvoyl-dependent amino acid decarboxylases. Class 1A is enzymes are found primarily in Gram-negative bacteria, including E. coli while Class 1B are found in some Gram-positive bacteria and archaea. These two classes show only low levels of amino acid sequence similarity. A homology model of the core structure of the E. coli enzyme based on the crystal structures of the human (Class 2) and Thermotoga maritima (Class 1B) enzymes has been proposed . E. coli S- adenosylmethionine (AdoMet) decarboxylase, encoded by the speD gene, is a heterooctamer of four α and four β chains arranged as a tetramer of α/β heterodimers. It has 1 pyruvoyl residue for each αβ pair. The amino terminus of the larger α subunit has a pyruvoyl group while the smaller β subunit has a free amino terminus . The enzyme is first synthesized as a proenzyme of 30.4 kDa polypeptide, which then undergoes post-translational autocatal

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SAMDECARB-RXN|reaction.ecocyc.SAMDECARB-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD0-2654|molecule.ecocyc.CPD0-2654]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A7F6|protein.P0A7F6]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:SAMDECARB-CPLX`

## Notes

4*protein.P0A7F6|4*protein.P0A7F6
