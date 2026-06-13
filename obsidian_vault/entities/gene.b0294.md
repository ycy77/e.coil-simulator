---
entity_id: "gene.b0294"
entity_type: "gene"
name: "matA"
source_database: "NCBI RefSeq"
source_id: "gene-b0294"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0294"
  - "matA"
---

# matA

`gene.b0294`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0294`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

matA (gene.b0294) is a gene entity. It encodes ecpR (protein.P71301). Encoded protein function: FUNCTION: Part of the ecpRABCDE operon, which encodes the E.coli common pilus (ECP). ECP is found in both commensal and pathogenic strains and plays a dual role in early-stage biofilm development and host cell recognition. Positively regulates the expression of the ecp operon (By similarity). Also represses expression of the flagellar master operon flhDC, and consequently prevents flagellum biosynthesis and motility. Acts by binding to the regulatory region of the flhDC operon (Probable). {ECO:0000250, ECO:0000269|PubMed:22422754, ECO:0000305}. EcoCyc product frame: G6165-MONOMER. EcoCyc synonyms: ykgK, ecpR. Genomic coordinates: 310746-311336. EcoCyc protein note: MatA is a LuxR-type transcription factor that is directly involved, as a positive regulator acting at transcriptional and posttranscriptional levels, in the expression of the mat operon in meningitis isolate strain IHE 3034 (T. A. Lehti, P. Bauchart, M. Kukkonen, U. Dobrindt, T. K. Korhonen, B. Westerlund-Wikstrom, unpublished results) . On the other hand, MatA controls the expression of the flhDC operon, with higher affinity to flhDp, repressing flagellum biosynthesis, motility, and taxis . The opposite regulatory actions of MatA on mat and on flhDC promoters advance the adaptation of E...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748). Activated by ecpR (protein.P71301).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P71301|protein.P71301]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P71301|protein.P71301]] `RegulonDB` `S` - regulator=MatA; target=matA; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001011,ECOCYC:G6165,GeneID:944966`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:310746-311336:-; feature_type=gene
