---
entity_id: "protein.P15723"
entity_type: "protein"
name: "dgt"
source_database: "UniProt"
source_id: "P15723"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dgt b0160 JW0156"
---

# dgt

`protein.P15723`

## Static

- Type: `protein`
- Source: `UniProt:P15723`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: dGTPase preferentially hydrolyzes dGTP over the other canonical NTPs. {ECO:0000255|HAMAP-Rule:MF_00030, ECO:0000269|PubMed:2826481}. Deoxyguanosinetriphosphate triphosphohydrolase (dGTPase, Dgt) is a unique nucleoside triphosphatase which specifically hydrolyzes dGTP to deoxyguanosine and inorganic tripolyphosphate . Possible physiological roles of the enzyme have only recently been elucidated. Dgt may be involved in replication fidelity via its effect on the cellular pool of dGTP . The level of Dgt expression correlates with the ability of cells to salvage thymine in the absence of functional de novo biosynthesis in a thyA mutant, presumably due to its effect on the intracellular deoxyribose-1-phosphate pool . dGTPase is able to bind single-stranded DNA with relatively high affinity . Crystal structures of the enzyme have been solved . Although dGTPase was thought to be a homotetramer based on a prior measurement of its native molecular weight , the crystal structure showed a homohexameric conformation. Subunits with bound ssDNA show significant conformational changes, including in the active site. DNA binding activates the enzyme, lowering the Km for dGTP. An S34D G37E double mutant abolishes binding and stimulation of enzymatic activity by DNA...

## Biological Role

Component of dGTP triphosphohydrolase (complex.ecocyc.DGTPTRIPHYDRO-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: dGTPase preferentially hydrolyzes dGTP over the other canonical NTPs. {ECO:0000255|HAMAP-Rule:MF_00030, ECO:0000269|PubMed:2826481}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DGTPTRIPHYDRO-CPLX|complex.ecocyc.DGTPTRIPHYDRO-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0160|gene.b0160]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15723`
- `KEGG:ecj:JW0156;eco:b0160;ecoc:C3026_00730;`
- `GeneID:947177;`
- `GO:GO:0000287; GO:0003697; GO:0003924; GO:0006203; GO:0008832; GO:0015949; GO:0030145; GO:0042802; GO:0043099; GO:0050897`
- `EC:3.1.5.1`

## Notes

Deoxyguanosinetriphosphate triphosphohydrolase (dGTP triphosphohydrolase) (dGTPase) (EC 3.1.5.1)
