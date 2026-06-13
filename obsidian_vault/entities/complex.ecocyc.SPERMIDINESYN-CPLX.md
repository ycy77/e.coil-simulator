---
entity_id: "complex.ecocyc.SPERMIDINESYN-CPLX"
entity_type: "complex"
name: "spermidine synthase"
source_database: "EcoCyc"
source_id: "SPERMIDINESYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# spermidine synthase

`complex.ecocyc.SPERMIDINESYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SPERMIDINESYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P09158|protein.P09158]]

## Enriched Summary

Spermidine synthase (SpeE) catalyzes the final step in the biosynthesis of the polyamine spermidine. The crystal structure of SpeE has been determined at 2.9 Å resolution. The enzyme is a dimer both in solution and the crystal structure. Each SpeE monomer consists of two domains: a small N-terminal β-strand domain which includes 6 β-strands and a C-terminal catalytic core domain that adopts a canonical methyltransferase (MTase) fold. E. coli SpeE possesses a unique large substrate-binding pocket that is probably responsible for a broader substrate specificity of this enzyme, compared to its orthologs. Three aspartic acid residues, Asp88, Asp158, and Asp161 in SpeE play key roles in the aminopropyltransferase reaction. The carboxylate side chain of Asp158 plays a major role in the deprotonation of the substrate and is aided by Tyr63 and Tyr226 . Further site-directed mutagenesis confirmed the importance for catalysis of hydrophobic interactions contributed by residues in the gatekeeping loop . The enzyme was first purified from E. coli W and later subjected to kinetic analysis and substrate analog inhibition studies; a reaction mechanism was proposed . Experiments with the E. coli K-12 enzyme also suggest a ping-pong reaction mechanism . Only one enzyme with aminopropyltransferase activity has been found in E. coli...

## Biological Role

Catalyzes RXN0-5217 (reaction.ecocyc.RXN0-5217), SPERMIDINESYN-RXN (reaction.ecocyc.SPERMIDINESYN-RXN).

## Annotation

Spermidine synthase (SpeE) catalyzes the final step in the biosynthesis of the polyamine spermidine. The crystal structure of SpeE has been determined at 2.9 Å resolution. The enzyme is a dimer both in solution and the crystal structure. Each SpeE monomer consists of two domains: a small N-terminal β-strand domain which includes 6 β-strands and a C-terminal catalytic core domain that adopts a canonical methyltransferase (MTase) fold. E. coli SpeE possesses a unique large substrate-binding pocket that is probably responsible for a broader substrate specificity of this enzyme, compared to its orthologs. Three aspartic acid residues, Asp88, Asp158, and Asp161 in SpeE play key roles in the aminopropyltransferase reaction. The carboxylate side chain of Asp158 plays a major role in the deprotonation of the substrate and is aided by Tyr63 and Tyr226 . Further site-directed mutagenesis confirmed the importance for catalysis of hydrophobic interactions contributed by residues in the gatekeeping loop . The enzyme was first purified from E. coli W and later subjected to kinetic analysis and substrate analog inhibition studies; a reaction mechanism was proposed . Experiments with the E. coli K-12 enzyme also suggest a ping-pong reaction mechanism . Only one enzyme with aminopropyltransferase activity has been found in E. coli . Inhibition of spermidine synthase activity by dicyclohexylamine inhibits growth of E. coli . Strains lacking the ability to synthesize spermidine have near-normal growth rates , but are more sensitive to paraquat than wild type . speE belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5217|reaction.ecocyc.RXN0-5217]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SPERMIDINESYN-RXN|reaction.ecocyc.SPERMIDINESYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P09158|protein.P09158]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:SPERMIDINESYN-CPLX`
- `QSPROTEOME:QS00181545`

## Notes

2*protein.P09158
