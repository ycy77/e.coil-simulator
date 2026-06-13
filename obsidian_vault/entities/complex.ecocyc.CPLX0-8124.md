---
entity_id: "complex.ecocyc.CPLX0-8124"
entity_type: "complex"
name: "tRNA cytosine32 2-sulfurtransferase TtcA"
source_database: "EcoCyc"
source_id: "CPLX0-8124"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tRNA cytosine32 2-sulfurtransferase TtcA

`complex.ecocyc.CPLX0-8124`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8124`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P76055|protein.P76055]]

## Enriched Summary

TtcA catalyzes the post-transcriptional modification of certain tRNAs by attaching sulfur at the C32 nucleotide . Active enzyme contains an oxygen-sensitive [4Fe-4S] cluster; as-purified enzyme contains a [2Fe-2S] cluster and is not catalytically active. The Cys residues C122, C125 and C222 are required for activity and may be the ligands for the [4Fe-4S] cluster. A reaction mechanism involving the Fe-S cluster in the sulfur transfer has been proposed . tRNA from a ttcA mutant lacks a component suggested to be s2C32 . ttcA resides next to the Rac prophage in the E. coli genome; the phage attachment site (attL) is part of the TtcA coding region. Excision of the prophage cases some changes to the ttcA coding sequence due to sequence differences between attL and attR. The altered TtcA protein (TtcA') leads to decreased growth in the presence of carbenicillin . Also, in a Rac mutant strain, the biofilm formation and swimming motility are enhanced . The [4Fe-4S] cluster is not involved in the binding affinity of TtcA to tRNA . TtcA: "two-thiocytidine" TtcA catalyzes the post-transcriptional modification of certain tRNAs by attaching sulfur at the C32 nucleotide . Active enzyme contains an oxygen-sensitive [4Fe-4S] cluster; as-purified enzyme contains a [2Fe-2S] cluster and is not catalytically active...

## Biological Role

Catalyzes TRNA-S-TRANSFERASE-RXN (reaction.ecocyc.TRNA-S-TRANSFERASE-RXN). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

TtcA catalyzes the post-transcriptional modification of certain tRNAs by attaching sulfur at the C32 nucleotide . Active enzyme contains an oxygen-sensitive [4Fe-4S] cluster; as-purified enzyme contains a [2Fe-2S] cluster and is not catalytically active. The Cys residues C122, C125 and C222 are required for activity and may be the ligands for the [4Fe-4S] cluster. A reaction mechanism involving the Fe-S cluster in the sulfur transfer has been proposed . tRNA from a ttcA mutant lacks a component suggested to be s2C32 . ttcA resides next to the Rac prophage in the E. coli genome; the phage attachment site (attL) is part of the TtcA coding region. Excision of the prophage cases some changes to the ttcA coding sequence due to sequence differences between attL and attR. The altered TtcA protein (TtcA') leads to decreased growth in the presence of carbenicillin . Also, in a Rac mutant strain, the biofilm formation and swimming motility are enhanced . The [4Fe-4S] cluster is not involved in the binding affinity of TtcA to tRNA . TtcA: "two-thiocytidine"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRNA-S-TRANSFERASE-RXN|reaction.ecocyc.TRNA-S-TRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P76055|protein.P76055]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8124`
- `QSPROTEOME:QS00049563`

## Notes

2*protein.P76055
