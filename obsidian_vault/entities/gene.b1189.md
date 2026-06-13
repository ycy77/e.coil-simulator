---
entity_id: "gene.b1189"
entity_type: "gene"
name: "dadA"
source_database: "NCBI RefSeq"
source_id: "gene-b1189"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1189"
  - "dadA"
---

# dadA

`gene.b1189`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1189`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dadA (gene.b1189) is a gene entity. It encodes dadA (protein.P0A6J5). Encoded protein function: FUNCTION: Catalyzes the oxidative deamination of D-amino acids. Has broad substrate specificity; is mostly active on D-alanine, and to a lesser extent, on several other D-amino acids such as D-methionine, D-serine and D-proline, but not on L-alanine. Participates in the utilization of L-alanine and D-alanine as the sole source of carbon, nitrogen and energy for growth. Is also able to oxidize D-amino acid analogs such as 3,4-dehydro-D-proline, D-2-aminobutyrate, D-norvaline, D-norleucine, cis-4-hydroxy-D-proline, and DL-ethionine. {ECO:0000269|PubMed:13292, ECO:0000269|PubMed:15358424}. EcoCyc product frame: DALADEHYDROGA-MONOMER. EcoCyc synonyms: dadR. Genomic coordinates: 1237571-1238869.

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), crp (protein.P0ACJ8), nac (protein.Q47005).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6J5|protein.P0A6J5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dadA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=dadA; function=-+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=dadA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=dadA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0003995,ECOCYC:EG11407,GeneID:945752`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1237571-1238869:+; feature_type=gene
