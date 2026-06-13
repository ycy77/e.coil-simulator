---
entity_id: "gene.b1530"
entity_type: "gene"
name: "marR"
source_database: "NCBI RefSeq"
source_id: "gene-b1530"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1530"
  - "marR"
---

# marR

`gene.b1530`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1530`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

marR (gene.b1530) is a gene entity. It encodes marR (protein.P27245). Encoded protein function: FUNCTION: Repressor of the marRAB operon which is involved in the activation of both antibiotic resistance and oxidative stress genes. Binds to the marO operator/promoter site. EcoCyc product frame: PD00364. EcoCyc synonyms: cfxB, inaR, soxQ. Genomic coordinates: 1619120-1619554. EcoCyc protein note: MarR, "Multiple antibiotic resistance" , participates in controlling several genes involved in resistance to antibiotics , multidrug efflux , oxidative stress , organic solvents , biofilm formation , and heavy metals . The antibiotic resistance associated with MarR appears to involve the acidification of the cytoplasm . MarR is part of the marRAB operon and negatively autoregulates its own expression . The marA gene encodes a transcriptional activator that autoactivates expression of the marRAB operon and that regulates the expression of a global network of at least 80 chromosomal genes . Under laboratory conditions, the marRAB operon can be induced by tetracycline, chloramphenicol, or salicylate , plumbagin, dinitrophenol, and menadione , and other chemicals with phenolic rings . All these compounds attenuate the ability of MarR homodimers to bind their cognate DNA sequences . Cross talk between the mar and rob systems plays an important role in the response to salicylate...

## Biological Role

Repressed by cra (protein.P0ACP1), acrR (protein.P0ACS9), marR (protein.P27245). Activated by fis (protein.P0A6R3), soxS (protein.P0A9E2), marA (protein.P0ACH5), rob (protein.P0ACI0), cpxR (protein.P0AE88), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27245|protein.P27245]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=marR; function=+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=marR; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `C` - regulator=MarA; target=marR; function=+
- `activates` <-- [[protein.P0ACI0|protein.P0ACI0]] `RegulonDB` `C` - regulator=Rob; target=marR; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=marR; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=marR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=marR; function=-
- `represses` <-- [[protein.P0ACS9|protein.P0ACS9]] `RegulonDB` `S` - regulator=AcrR; target=marR; function=-
- `represses` <-- [[protein.P27245|protein.P27245]] `RegulonDB` `C` - regulator=MarR; target=marR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005110,ECOCYC:EG11435,GeneID:945825`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1619120-1619554:+; feature_type=gene
