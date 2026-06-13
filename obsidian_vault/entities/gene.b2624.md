---
entity_id: "gene.b2624"
entity_type: "gene"
name: "alpA"
source_database: "NCBI RefSeq"
source_id: "gene-b2624"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2624"
  - "alpA"
---

# alpA

`gene.b2624`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2624`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alpA (gene.b2624) is a gene entity. It encodes alpA (protein.P33997). Encoded protein function: FUNCTION: Positive regulator of the expression of the slpA gene (PubMed:7511582). When overexpressed, leads to suppression of the capsule overproduction and UV sensitivity phenotypes of cells mutant for the Lon ATP-dependent protease (PubMed:7511582). Part of the cryptic P4-like prophage CP4-57 (PubMed:7511583). Overexpression of AlpA leads to excision of the CP4-57 prophage by IntA. This inactivates ssrA (the gene upstream of the prophage) that encodes tmRNA which is required to rescue stalled ribosomes in a process known as trans-translation (PubMed:7511583). {ECO:0000269|PubMed:7511582, ECO:0000269|PubMed:7511583}. EcoCyc product frame: PD02850. Genomic coordinates: 2758644-2758856. EcoCyc protein note: AlpA is a transcriptional regulator of intA expression . It is part of the CP4-57 cryptic prophage that is similar to bacteriophage P4 . AlpA is also involved in the negative regulation of cell persister resuscitation . alpA was first identified as a multicopy suppressor of lon mutants that leads to the expression of an alternative Lon protease activity named Alp . AlpA expression leads to increased synthesis of IntA, which results in excision of the CP4-57 cryptic prophage. The excision inactivates the gene upstream of intA, ssrA, encoding SSRA-RNA...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33997|protein.P33997]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008636,ECOCYC:EG12112,GeneID:946758`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2758644-2758856:+; feature_type=gene
