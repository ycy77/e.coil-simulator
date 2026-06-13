---
entity_id: "gene.b1660"
entity_type: "gene"
name: "punC"
source_database: "NCBI RefSeq"
source_id: "gene-b1660"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1660"
  - "punC"
---

# punC

`gene.b1660`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1660`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

punC (gene.b1660) is a gene entity. It encodes punC (protein.P37597). Encoded protein function: FUNCTION: Transports purine nucleosides (PubMed:34413462). Shows a broad specificity for purine nuclesides, including adenosine, 2-deoxyadenosine, guanosine and inosine (PubMed:32994326, PubMed:34413462). Uptake of purine nucleosides may support growth under nitrogen-limiting conditions (PubMed:34413462). It also exhibits specificity for the uptake of certain sulfonamides, which are structural analogs of para-aminobenzoic acid (PABA) (PubMed:34413462). Was originally identified as a putative arabinose efflux transporter, however, overexpression of the gene has no effect on intracellular arabinose concentrations (PubMed:22952739). {ECO:0000269|PubMed:22952739, ECO:0000269|PubMed:32994326, ECO:0000269|PubMed:34413462}. EcoCyc product frame: YDHC-MONOMER. EcoCyc synonyms: ydhC. Genomic coordinates: 1739911-1741122. EcoCyc protein note: PunC is a purine nucleoside transporter that supports growth under nitrogen-limiting conditions; a punC deletion strain from the Keio collection is unable to grow with adenosine or 2-deoxyadenosine as the nitrogen source; the punC mutant also shows a growth defect with inosine or guanosine as nitrogen source . PunC is implicated in the uptake of some sulfonamide antibiotics...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639). Activated by punR (protein.P0ACR2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37597|protein.P37597]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACR2|protein.P0ACR2]] `RegulonDB|EcoCyc` `C` - regulator=PunR; target=punC; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005551,ECOCYC:EG12141,GeneID:946077`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1739911-1741122:+; feature_type=gene
