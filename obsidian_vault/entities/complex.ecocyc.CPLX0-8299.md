---
entity_id: "complex.ecocyc.CPLX0-8299"
entity_type: "complex"
name: "ribose-phosphate diphosphokinase"
source_database: "EcoCyc"
source_id: "CPLX0-8299"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "phosphoribosylpyrophosphate synthetase"
  - "PRPS"
---

# ribose-phosphate diphosphokinase

`complex.ecocyc.CPLX0-8299`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8299`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A717|protein.P0A717]]

## Enriched Summary

Ribose-phosphate diphosphokinase (Prs) transfers a pyrophosphoryl group from ATP to ribose 5-phosphate, synthesizing PRPP (PRPP). PRPP is a pivotal metabolite; a total of 10 enzymes in a variety of biosynthesis and salvage pathways utilize PRPP as substrate. Mg2+ is an activator that may serve as a bridge between PRPP synthetase and the α-phosphate residue of ATP and AMP . Potential active site residues have been identified . Site-directed mutagenesis of conserved aspartate residues was used to identify residues involved in catalysis and binding of ribose-5-phosphate . Kinetic analysis indicates a sequential reaction mechanism . Further experiments showed that the enzyme uses a steady state ordered mechanism, where Mg2+ binds first, followed by Mg·ATP and lastly, ribose 5-phosphate . Saturation of the enzyme with phosphate enables fast, ordered binding of Mg2+ and substrates. ADP inhibits Pi activation of the enzyme by competing for a single regulatory site . Using a method that distinguishes N-phosphorylation from O-phosphorylation, His206 residue was found to be phosphorylated in vitro . A crystal structure of the enzyme has been solved at 2.2 Å resolution. A trimer of dimers forms the homohexameric structure...

## Biological Role

Catalyzes PRPPSYN-RXN (reaction.ecocyc.PRPPSYN-RXN).

## Annotation

Ribose-phosphate diphosphokinase (Prs) transfers a pyrophosphoryl group from ATP to ribose 5-phosphate, synthesizing PRPP (PRPP). PRPP is a pivotal metabolite; a total of 10 enzymes in a variety of biosynthesis and salvage pathways utilize PRPP as substrate. Mg2+ is an activator that may serve as a bridge between PRPP synthetase and the α-phosphate residue of ATP and AMP . Potential active site residues have been identified . Site-directed mutagenesis of conserved aspartate residues was used to identify residues involved in catalysis and binding of ribose-5-phosphate . Kinetic analysis indicates a sequential reaction mechanism . Further experiments showed that the enzyme uses a steady state ordered mechanism, where Mg2+ binds first, followed by Mg·ATP and lastly, ribose 5-phosphate . Saturation of the enzyme with phosphate enables fast, ordered binding of Mg2+ and substrates. ADP inhibits Pi activation of the enzyme by competing for a single regulatory site . Using a method that distinguishes N-phosphorylation from O-phosphorylation, His206 residue was found to be phosphorylated in vitro . A crystal structure of the enzyme has been solved at 2.2 Å resolution. A trimer of dimers forms the homohexameric structure . Cryo-EM analysis of purified Prs in vitro and in vivo found the enzyme can form filaments, referred to as cytoophidium that has been observed in other organisms, including humans. Two types of filaments formed; additional analyses of type A filament observed a regulatory flexible (RF) loop that might influence their allosteric inhibition and allosteric binding site for AMP and ADP . A temperature-sensitive prs mutant is viable at the restrictive temperature if guanosine, uridine, histidine, tryptophan and nicotinamide mononucleotide are provided in the medium .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PRPPSYN-RXN|reaction.ecocyc.PRPPSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A717|protein.P0A717]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-8299`
- `QSPROTEOME:QS00181721`

## Notes

6*protein.P0A717
