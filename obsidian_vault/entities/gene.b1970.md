---
entity_id: "gene.b1970"
entity_type: "gene"
name: "hiuH"
source_database: "NCBI RefSeq"
source_id: "gene-b1970"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1970"
  - "hiuH"
---

# hiuH

`gene.b1970`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1970`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hiuH (gene.b1970) is a gene entity. It encodes hiuH (protein.P76341). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of 5-hydroxyisourate (HIU) to 2-oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline (OHCU). {ECO:0000269|PubMed:16098976}. EcoCyc product frame: G7058-MONOMER. EcoCyc synonyms: yedX. Genomic coordinates: 2038956-2039369. EcoCyc protein note: YedX belongs to the family of transthyretin-related proteins (TRP). Transthyretin is a transport protein in extracellular fluids of vertebrates, where it distributes thyroid hormones . YedX is othologous with Bacillus subtilis PucM, which functions to facilitate the hydrolysis of 5-hydroxyisourate (HIU), the end product of the uricase reaction; purified YedX has 5-hydroxyisourate hydrolase (HIUH) activity The physiological significance of HIUH activity in E. coli is unclear. The source of HIU is not known; E. coli degrades purines to form uric acid (see PWY-6608 and SALVADEHYPOX-PWY), which is a good source of nitrogen in many organisms, but uricase activity has not been identified in E.coli. Alternatively, suggests that uric acid functions as an antioxidant in enterobacteria and that the oxidative (nonenzymatic) decomposition of uric acid would also generate HIU which can spontaneously decompose into, and react with, a variety of free radical compounds...

## Biological Role

Activated by cusR (protein.P0ACZ8), phoB (protein.P0AFJ5), hprR (protein.P76340).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76341|protein.P76341]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACZ8|protein.P0ACZ8]] `RegulonDB` `S` - regulator=CusR; target=hiuH; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=hiuH; function=+
- `activates` <-- [[protein.P76340|protein.P76340]] `RegulonDB` `C` - regulator=HprR; target=hiuH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006537,ECOCYC:G7058,GeneID:946485`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2038956-2039369:+; feature_type=gene
