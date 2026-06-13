---
entity_id: "protein.P0AFU0"
entity_type: "protein"
name: "yejB"
source_database: "UniProt"
source_id: "P0AFU0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yejB b2178 JW2166"
---

# yejB

`protein.P0AFU0`

## Static

- Type: `protein`
- Source: `UniProt:P0AFU0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex YejABEF involved in the uptake of oligopeptides (PubMed:17873039, PubMed:21602342). The transporter is involved in the uptake of microcin C (McC), a natural peptide-nucleotide antibiotic that targets aspartyl-tRNA synthetase (PubMed:17873039). It can transport synthetic McC analogs containing a minimal peptide chain length of 6 amino acids and an N-terminal formyl-methionyl-arginyl sequence (PubMed:21602342). The preferred peptide length for YejABEF-mediated uptake is more than 7 but less than 13 amino acids (PubMed:21602342). This subunit is responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:17873039, ECO:0000269|PubMed:21602342, ECO:0000305}. YejB is one of two inner membrane subunits of a putative ATP-dependent oligopeptide uptake system .

## Biological Role

Component of putative oligopeptide ABC transporter (complex.ecocyc.ABC-41-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex YejABEF involved in the uptake of oligopeptides (PubMed:17873039, PubMed:21602342). The transporter is involved in the uptake of microcin C (McC), a natural peptide-nucleotide antibiotic that targets aspartyl-tRNA synthetase (PubMed:17873039). It can transport synthetic McC analogs containing a minimal peptide chain length of 6 amino acids and an N-terminal formyl-methionyl-arginyl sequence (PubMed:21602342). The preferred peptide length for YejABEF-mediated uptake is more than 7 but less than 13 amino acids (PubMed:21602342). This subunit is responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:17873039, ECO:0000269|PubMed:21602342, ECO:0000305}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-41-CPLX|complex.ecocyc.ABC-41-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2178|gene.b2178]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFU0`
- `KEGG:ecj:JW2166;eco:b2178;ecoc:C3026_12185;`
- `GeneID:86860353;946679;`
- `GO:GO:0005886; GO:0015833; GO:0016020; GO:0022857; GO:0035672; GO:0042884; GO:0055052`

## Notes

Oligopeptide transport system permease protein YejB
