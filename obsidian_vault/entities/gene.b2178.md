---
entity_id: "gene.b2178"
entity_type: "gene"
name: "yejB"
source_database: "NCBI RefSeq"
source_id: "gene-b2178"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2178"
  - "yejB"
---

# yejB

`gene.b2178`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2178`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yejB (gene.b2178) is a gene entity. It encodes yejB (protein.P0AFU0). Encoded protein function: FUNCTION: Part of the ABC transporter complex YejABEF involved in the uptake of oligopeptides (PubMed:17873039, PubMed:21602342). The transporter is involved in the uptake of microcin C (McC), a natural peptide-nucleotide antibiotic that targets aspartyl-tRNA synthetase (PubMed:17873039). It can transport synthetic McC analogs containing a minimal peptide chain length of 6 amino acids and an N-terminal formyl-methionyl-arginyl sequence (PubMed:21602342). The preferred peptide length for YejABEF-mediated uptake is more than 7 but less than 13 amino acids (PubMed:21602342). This subunit is responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:17873039, ECO:0000269|PubMed:21602342, ECO:0000305}. EcoCyc product frame: YEJB-MONOMER. Genomic coordinates: 2274179-2275273. EcoCyc protein note: YejB is one of two inner membrane subunits of a putative ATP-dependent oligopeptide uptake system .

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFU0|protein.P0AFU0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yejB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007208,ECOCYC:EG12038,GeneID:946679`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2274179-2275273:+; feature_type=gene
