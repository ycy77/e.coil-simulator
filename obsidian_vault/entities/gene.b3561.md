---
entity_id: "gene.b3561"
entity_type: "gene"
name: "wecH"
source_database: "NCBI RefSeq"
source_id: "gene-b3561"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3561"
  - "wecH"
---

# wecH

`gene.b3561`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3561`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wecH (gene.b3561) is a gene entity. It encodes wecH (protein.P37669). Encoded protein function: FUNCTION: Responsible for the incorporation of O-acetyl groups into the enterobacterial common antigen (ECA) trisaccharide repeat units. Catalyzes the acetylation of both cyclic ECA (ECA(CYC)) and phosphoglyceride-linked ECA (ECA(PG)). {ECO:0000269|PubMed:16936038}. EcoCyc product frame: EG12274-MONOMER. EcoCyc synonyms: yiaH. Genomic coordinates: 3725887-3726882. EcoCyc protein note: Based on its mutant phenotype, WecH is the O-acetyltransferase responsible for the nonstoichiometric addition of O-acetyl groups onto the 6-position of N-acetyl-D-glucosamine residues of the trisaccharide repeat unit of ECACYC and ECAPG. WecH is predicted to be an inner membrane protein with 10 transmembrane segments . Since it is not known at which stage of ECA biosynthesis acetylation occurs, it is not possible at this time to assign a specific reaction to this enzyme. The authors proposed that it is likely that acetylation occurs during the assembly of lipid III on the cytoplasmic face of the inner membrane, prior to the WzxE-mediated translocation of lipid III across the membrane . However, as of 2023 no experimental data exists to support this proposal. wecH is induced when FtsZ ring assembly is inhibited by expression of SulA, though this is not believed to be relevant to cell division .

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37669|protein.P37669]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=wecH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011630,ECOCYC:EG12274,GeneID:948077`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3725887-3726882:+; feature_type=gene
