---
entity_id: "protein.P33915"
entity_type: "protein"
name: "yejE"
source_database: "UniProt"
source_id: "P33915"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yejE b2179 JW2167"
---

# yejE

`protein.P33915`

## Static

- Type: `protein`
- Source: `UniProt:P33915`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex YejABEF involved in the uptake of oligopeptides (PubMed:17873039, PubMed:21602342). The transporter is involved in the uptake of microcin C (McC), a natural peptide-nucleotide antibiotic that targets aspartyl-tRNA synthetase (PubMed:17873039). It can transport synthetic McC analogs containing a minimal peptide chain length of 6 amino acids and an N-terminal formyl-methionyl-arginyl sequence (PubMed:21602342). The preferred peptide length for YejABEF-mediated uptake is more than 7 but less than 13 amino acids (PubMed:21602342). This subunit is responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:17873039, ECO:0000269|PubMed:21602342, ECO:0000305}. YejE is one of two inner membrane subunits of a putative ATP-dependent oligopeptide uptake system .

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

- `encodes` <-- [[gene.b2179|gene.b2179]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33915`
- `KEGG:ecj:JW2167;eco:b2179;ecoc:C3026_12190;`
- `GeneID:946683;`
- `GO:GO:0005886; GO:0015833; GO:0016020; GO:0035672; GO:0042884; GO:0055052`

## Notes

Oligopeptide transport system permease protein YejE
