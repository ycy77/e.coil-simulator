---
entity_id: "gene.b3429"
entity_type: "gene"
name: "glgA"
source_database: "NCBI RefSeq"
source_id: "gene-b3429"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3429"
  - "glgA"
---

# glgA

`gene.b3429`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3429`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glgA (gene.b3429) is a gene entity. It encodes glgA (protein.P0A6U8). Encoded protein function: FUNCTION: Synthesizes alpha-1,4-glucan chains using ADP-glucose. EcoCyc product frame: GLYCOGENSYN-MONOMER. Genomic coordinates: 3566600-3568033. EcoCyc protein note: Glycogen synthase is a glycosyltransferase, the second enzyme in the glycogen biosynthesis pathway. It catalyzes the addition of a glucosyl unit from ADP-glucose to the non-reducing end of glycogen. Lys15 may be involved in binding of ADP-glucose . A conserved region around Cys379 is predicted to form a loop structure and is involved in the interaction with ADP-glucose . Lys277 may be required for catalysis . Further site-directed mutagenesis identified residues essential for catalytic activity and ADP-glucose binding . Crystal structures of the wild-type and mutant GlgA in various conformations have been solved, suggesting the location of catalytic residues . A structure of GlgA with bound oligosaccharide indicates that long-chain glycans only bind to the N-terminal domain, ensuring unencumbered interdomain movement and efficient catalysis . Native glycogen synthase binds to metal affinity columns and may thus bind Mg2+, like its human homolog . Glycogen synthase from E. coli B can exist in homodimeric, -trimeric and -tetrameric form . However, all crystal structures obtained of the K-12 enzyme show a monomeric form...

## Biological Role

Repressed by csrA (protein.P69913). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6U8|protein.P0A6U8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=glgA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=glgA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=glgA; function=+
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `S` - regulator=carbon storage regulator CsrA; target=glgA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011200,ECOCYC:EG10377,GeneID:947932`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3566600-3568033:-; feature_type=gene
