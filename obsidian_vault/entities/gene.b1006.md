---
entity_id: "gene.b1006"
entity_type: "gene"
name: "rutG"
source_database: "NCBI RefSeq"
source_id: "gene-b1006"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1006"
  - "rutG"
---

# rutG

`gene.b1006`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1006`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rutG (gene.b1006) is a gene entity. It encodes rutG (protein.P75892). Encoded protein function: FUNCTION: May function as a proton-driven pyrimidine uptake system. {ECO:0000269|PubMed:16540542}. EcoCyc product frame: B1006-MONOMER. EcoCyc synonyms: ycdG. Genomic coordinates: 1068511-1069839. EcoCyc protein note: RutG is a high-affinity pyrimidine transporter; RutG mediates the uptake of both uracil and thymidine; the uptake of labeled uracil is abolished by the protonophore carbonyl cyanide m-chlorophenyl hydrazone (CCCP) . RutG transports xanthine with low affinity and efficiency; it does not transport cytosine, adenine, guanine, hypoxanthine or uric acid . rutG is the last gene in a 7 gene operon (rutABCDEFG) that encodes proteins involved in the utilization of pyrimidines as a nitrogen source in E. coli K-12 . Expression of the rut operon is activated by the nitrogen regulatory protein C (NtrC) when nitrogen is limiting and repressed by the global regulator RutR . A rutG deletion mutant does not grow on uracil as the sole source of nitrogen at room temperature . Deletion of upp, encoding URACIL-PRIBOSYLTRANS-CPLX, prevents the uptake of uracil by RutG and by CPLX0-8247 UraA . E. coli cannot use pyrimidines as the sole nitrogen source at 37oC however the rut operon is highly expressed at this temperature under nitrogen limiting conditions...

## Biological Role

Repressed by rutR (protein.P0ACU2). Activated by arcA (protein.P0A9Q1), glnG (protein.P0AFB8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75892|protein.P75892]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=rutG; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=rutG; function=+
- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `C` - regulator=RutR; target=rutG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003401,ECOCYC:G6517,GeneID:946589`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1068511-1069839:-; feature_type=gene
