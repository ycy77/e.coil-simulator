---
entity_id: "gene.b1922"
entity_type: "gene"
name: "fliA"
source_database: "NCBI RefSeq"
source_id: "gene-b1922"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1922"
  - "fliA"
---

# fliA

`gene.b1922`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1922`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliA (gene.b1922) is a gene entity. It encodes fliA (protein.P0AEM6). Encoded protein function: FUNCTION: Sigma factors are initiation factors that promote the attachment of RNA polymerase to specific initiation sites and are then released. This sigma factor controls the expression of flagella-related genes. {ECO:0000255|HAMAP-Rule:MF_00962, ECO:0000269|PubMed:2644646, ECO:0000269|PubMed:3536871, ECO:0000269|PubMed:7590326, ECO:0000269|PubMed:8866483}. EcoCyc product frame: EG11355-MONOMER. EcoCyc synonyms: rpoF, flaD. Genomic coordinates: 2001070-2001789. EcoCyc protein note: σ28 is a minor sigma factor that is responsible for initiation of transcription of a number of genes involved in motility and flagellar synthesis . σ28 competes with σ70 for APORNAP-CPLX, binding to it more tightly than σ70 . A distinguishing feature of σ28 promoters is a long -10 region (GCCGATAA); in addition, its upstream GC is highly conserved . Thus, σ28 not only uses extended -10 recognition but also requires three recognition regions, -35, extended -10, and -10, for successful utilization of the core σ28 promoter . Both GC and the CG motifs are functionally important in the -10 region of σ28, and this is a composite element...

## Biological Role

Repressed by lrp (protein.P0ACJ0), csgD (protein.P52106), ecpR (protein.P71301), sutR (protein.P77626). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), fliA (protein.P0AEM6), zraR (protein.P14375).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEM6|protein.P0AEM6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fliA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliA; function=+
- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=fliA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=fliA; function=-
- `represses` <-- [[protein.P71301|protein.P71301]] `RegulonDB` `S` - regulator=MatA; target=fliA; function=-
- `represses` <-- [[protein.P77626|protein.P77626]] `RegulonDB` `S` - regulator=SutR; target=fliA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006396,ECOCYC:EG11355,GeneID:948824`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2001070-2001789:-; feature_type=gene
