---
entity_id: "gene.b3727"
entity_type: "gene"
name: "pstC"
source_database: "NCBI RefSeq"
source_id: "gene-b3727"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3727"
  - "pstC"
---

# pstC

`gene.b3727`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3727`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pstC (gene.b3727) is a gene entity. It encodes pstC (protein.P0AGH8). Encoded protein function: FUNCTION: Part of the binding-protein-dependent transport system for phosphate; probably responsible for the translocation of the substrate across the membrane. EcoCyc product frame: PSTC-MONOMER. EcoCyc synonyms: phoW. Genomic coordinates: 3909439-3910398. EcoCyc protein note: PstC is one of two inner membrane subunits of an ATP-dependent high affinity phosphate uptake system. pstC belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGH8|protein.P0AGH8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pstC; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=pstC; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=pstC; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=pstC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012186,ECOCYC:EG10784,GeneID:948238`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3909439-3910398:-; feature_type=gene
