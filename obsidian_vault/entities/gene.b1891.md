---
entity_id: "gene.b1891"
entity_type: "gene"
name: "flhC"
source_database: "NCBI RefSeq"
source_id: "gene-b1891"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1891"
  - "flhC"
---

# flhC

`gene.b1891`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1891`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

flhC (gene.b1891) is a gene entity. It encodes flhC (protein.P0ABY7). Encoded protein function: FUNCTION: Functions in complex with FlhD as a master transcriptional regulator that regulates transcription of several flagellar and non-flagellar operons by binding to their promoter region. Activates expression of class 2 flagellar genes, including fliA, which is a flagellum-specific sigma factor that turns on the class 3 genes. Also regulates genes whose products function in a variety of physiological pathways. {ECO:0000269|PubMed:11169100, ECO:0000269|PubMed:15941987, ECO:0000269|PubMed:7961507}. EcoCyc product frame: MONOMER0-2488. EcoCyc synonyms: flaI. Genomic coordinates: 1977266-1977844.

## Biological Role

Repressed by omrA (gene.b4444), omrB (gene.b4445), arcZ (gene.b4450), oxyS (gene.b4458), hdfR (protein.P0A8R9), yjjQ (protein.P0ADD7), lrhA (protein.P36771), fliZ (protein.P52627), and 1 more. Activated by mcaS (gene.b4426), rpoD (protein.P00579), hns (protein.P0ACF8), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABY7|protein.P0ABY7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (13)

- `activates` <-- [[gene.b4426|gene.b4426]] `RegulonDB` `S` - regulator=McaS; target=flhC; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=flhC; function=+
- `activates` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=flhC; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=flhC; function=+
- `represses` <-- [[gene.b4444|gene.b4444]] `RegulonDB` `S` - regulator=OmrA; target=flhC; function=-
- `represses` <-- [[gene.b4445|gene.b4445]] `RegulonDB` `S` - regulator=OmrB; target=flhC; function=-
- `represses` <-- [[gene.b4450|gene.b4450]] `RegulonDB` `S` - regulator=ArcZ; target=flhC; function=-
- `represses` <-- [[gene.b4458|gene.b4458]] `RegulonDB` `S` - regulator=OxyS; target=flhC; function=-
- `represses` <-- [[protein.P0A8R9|protein.P0A8R9]] `RegulonDB` `S` - regulator=HdfR; target=flhC; function=-
- `represses` <-- [[protein.P0ADD7|protein.P0ADD7]] `RegulonDB` `S` - regulator=YjjQ; target=flhC; function=-
- `represses` <-- [[protein.P36771|protein.P36771]] `RegulonDB` `S` - regulator=LrhA; target=flhC; function=-
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `S` - regulator=FliZ; target=flhC; function=-
- `represses` <-- [[protein.P71301|protein.P71301]] `RegulonDB` `S` - regulator=MatA; target=flhC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006301,ECOCYC:EG10319,GeneID:947280`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1977266-1977844:-; feature_type=gene
