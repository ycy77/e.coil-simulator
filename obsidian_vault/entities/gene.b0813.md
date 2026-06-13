---
entity_id: "gene.b0813"
entity_type: "gene"
name: "rhtA"
source_database: "NCBI RefSeq"
source_id: "gene-b0813"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0813"
  - "rhtA"
---

# rhtA

`gene.b0813`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0813`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rhtA (gene.b0813) is a gene entity. It encodes rhtA (protein.P0AA67). Encoded protein function: FUNCTION: Involved in the efflux of threonine and homoserine. Can also export other amino acids such as proline, serine, histidine and cysteine. {ECO:0000269|PubMed:12648727}. EcoCyc product frame: EG12134-MONOMER. EcoCyc synonyms: ybiF. Genomic coordinates: 849210-850097. EcoCyc protein note: RhtA can mediate export of L-threonine and L-homoserine and likely operates as a substrate:proton antiporter; the physiological role of the transporter remains unclear. Increased expression of rhtA confers increased resistance to L-homoserine, L-threonine and some other amino acids (proline, serine, cysteine, histidine) and amino acid analogues . Increased expression of rhtA increases L-threonine production in a threonine producing strain and L-homoserine production in an L-homoserine producing strain; addition of the protonophore CPD-7970 results in a significant reduction in the rate of export . Heterologous expression of rhtA increases L-threonine and L-homoserine production in a Corynebacterium glutamicum threonine producing strain . RhtA is a membrane protein with 10 predicted transmembrane segments RhtA is a member of the 10 TMS Drug/Metabolite Exporter (DME) family of transporters within the Drug/Metabolite Transporter (DMT) superfamily . rht: resistance to homoserine and threonine

## Biological Role

Repressed by nac (protein.Q47005). Activated by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA67|protein.P0AA67]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=rhtA; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=rhtA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002779,ECOCYC:EG12134,GeneID:947045`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:849210-850097:-; feature_type=gene
