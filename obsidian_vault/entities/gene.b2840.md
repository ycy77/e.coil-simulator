---
entity_id: "gene.b2840"
entity_type: "gene"
name: "ygeA"
source_database: "NCBI RefSeq"
source_id: "gene-b2840"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2840"
  - "ygeA"
---

# ygeA

`gene.b2840`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2840`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygeA (gene.b2840) is a gene entity. It encodes ygeA (protein.P03813). Encoded protein function: FUNCTION: Amino-acid racemase able to utilize a broad range of substrates. Highest activity is observed with L-homoserine and D-homoserine. Has tenfold lower activity against L-methionine, L-leucine, L-valine and L-histidine. Has low activity with L-norvaline, L-asparagine, D-methionine, L-aminobutyric acid, L-isoleucine, L-serine, L-norleucine, L-alanine, L-glutamine, LL-diaminopimelic acid and L-phenylalanine. Has no activity against ten L-amino acids (Thr, Glu, Asp, Arg, Lys, Tyr, Trp, Orn, Cit and Aad) (PubMed:28894939). D-amino acids might be used as components of peptidoglycan and/or be involved in peptidoglycan metabolism and remodeling (PubMed:28894939). {ECO:0000269|PubMed:28894939}. EcoCyc product frame: EG11157-MONOMER. Genomic coordinates: 2979943-2980635.

## Biological Role

Activated by rpoD (protein.P00579), araC (protein.P0A9E0), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03813|protein.P03813]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ygeA; function=+
- `activates` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `S` - regulator=AraC; target=ygeA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ygeA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009315,ECOCYC:EG11157,GeneID:947348`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2979943-2980635:-; feature_type=gene
