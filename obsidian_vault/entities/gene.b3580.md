---
entity_id: "gene.b3580"
entity_type: "gene"
name: "lyxK"
source_database: "NCBI RefSeq"
source_id: "gene-b3580"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3580"
  - "lyxK"
---

# lyxK

`gene.b3580`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3580`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lyxK (gene.b3580) is a gene entity. It encodes lyx (protein.P37677). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of L-xylulose and 3-keto-L-gulonate. Is involved in L-lyxose utilization via xylulose, and may also be involved in the utilization of 2,3-diketo-L-gulonate. {ECO:0000269|PubMed:11741871, ECO:0000269|PubMed:7961955}. EcoCyc product frame: LYXK-MONOMER. EcoCyc synonyms: lyx, xylK, sgbK, yiaP. Genomic coordinates: 3747084-3748580. EcoCyc protein note: L-xylulose kinase is the product of an apparently silent gene, lyxK. Once expression is activated through a mutation in the transcriptional repressor YiaJ , the kinase specifically phosphorylates L-xylulose. This allows E. coli to utilize the uncommon sugar, L-lyxose, using enzymes of the rhamnose degradation system. The product of the L-xylulose kinase reaction, L-xylulose 5-P, is further metabolized by the pentose phosphate pathway . LyxK is also able to catalyze the phosphorylation of 3-keto-L-gulonate .

## Biological Role

Repressed by plaR (protein.P37671). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37677|protein.P37677]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lyxK; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=lyxK; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=lyxK; function=+
- `represses` <-- [[protein.P37671|protein.P37671]] `RegulonDB` `C` - regulator=PlaR; target=lyxK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011696,ECOCYC:EG12284,GeneID:948101`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3747084-3748580:+; feature_type=gene
