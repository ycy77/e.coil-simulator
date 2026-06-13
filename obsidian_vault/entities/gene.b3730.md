---
entity_id: "gene.b3730"
entity_type: "gene"
name: "glmU"
source_database: "NCBI RefSeq"
source_id: "gene-b3730"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3730"
  - "glmU"
---

# glmU

`gene.b3730`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3730`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glmU (gene.b3730) is a gene entity. It encodes glmU (protein.P0ACC7). Encoded protein function: FUNCTION: Catalyzes the last two sequential reactions in the de novo biosynthetic pathway for UDP-N-acetylglucosamine (UDP-GlcNAc). The C-terminal domain catalyzes the transfer of acetyl group from acetyl coenzyme A to glucosamine-1-phosphate (GlcN-1-P) to produce N-acetylglucosamine-1-phosphate (GlcNAc-1-P), which is converted into UDP-GlcNAc by the transfer of uridine 5-monophosphate (from uridine 5-triphosphate), a reaction catalyzed by the N-terminal domain. {ECO:0000255|HAMAP-Rule:MF_01631, ECO:0000269|PubMed:10428949, ECO:0000269|PubMed:21984832, ECO:0000269|PubMed:22297115, ECO:0000269|PubMed:8083170, ECO:0000269|PubMed:8555230}. EcoCyc product frame: NAG1P-URIDYLTRANS-MONOMER. EcoCyc synonyms: yieA. Genomic coordinates: 3913830-3915200. EcoCyc protein note: glmU encodes a fused enzyme with two enzymatic activities that catalyze sequential steps in the biosynthesis of UDP-N-acetyl-D-glucosamine (UDP-GlcNAc), an essential precursor of cell wall peptidoglycan, lipopolysaccharide and enterobacterial common antigen . The enzymatic activities of GlmU are present in two independently folding and functional domains...

## Biological Role

Repressed by nagC (protein.P0AF20). Activated by rpoD (protein.P00579), nagC (protein.P0AF20).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACC7|protein.P0ACC7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=glmU; function=+
- `activates` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=glmU; function=-+
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=glmU; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0012201,ECOCYC:EG11198,GeneID:948246`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3913830-3915200:-; feature_type=gene
