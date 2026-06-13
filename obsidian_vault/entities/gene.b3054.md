---
entity_id: "gene.b3054"
entity_type: "gene"
name: "ygiF"
source_database: "NCBI RefSeq"
source_id: "gene-b3054"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3054"
  - "ygiF"
---

# ygiF

`gene.b3054`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3054`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygiF (gene.b3054) is a gene entity. It encodes ygiF (protein.P30871). Encoded protein function: FUNCTION: Involved in the hydrolysis of the beta-gamma-phosphoanhydride linkage of triphosphate-containing substrates (inorganic or nucleoside-linked). Catalyzes the hydrolysis of inorganic triphosphate (PPPi), which could be cytotoxic because of its high affinity for calcium ion, thereby interfering with calcium signaling. It also hydrolyzes slowly thiamine triphosphate (ThTP). YgiF is a specific PPPase, but it contributes only marginally to the total PPPase activity in E.coli, where the main enzyme responsible for hydrolysis of PPPi is inorganic pyrophosphatase (PPase). {ECO:0000269|PubMed:22984449}. EcoCyc product frame: EG11603-MONOMER. Genomic coordinates: 3199664-3200965. EcoCyc protein note: YgiF belongs to the CYTH (CyaB-Thiamine triphosphatase) family of proteins. The enzyme was shown to be a specific inorganic triphosphatase. However, the majority of inorganic triphosphatase activity in E. coli cells may be due to the activity of CPLX0-243 . The ygiF gene was amplified from E. coli Mach1TM cells (Thermo Fisher Scientific, derived from E. coli W, not K-12; the Mach1TM gene is 98% identical to the K-12 gene), and crystal structures of the protein were solved...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30871|protein.P30871]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ygiF; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010020,ECOCYC:EG11603,GeneID:947554`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3199664-3200965:-; feature_type=gene
