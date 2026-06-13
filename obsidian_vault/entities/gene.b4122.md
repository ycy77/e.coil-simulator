---
entity_id: "gene.b4122"
entity_type: "gene"
name: "fumB"
source_database: "NCBI RefSeq"
source_id: "gene-b4122"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4122"
  - "fumB"
---

# fumB

`gene.b4122`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4122`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fumB (gene.b4122) is a gene entity. It encodes fumB (protein.P14407). Encoded protein function: FUNCTION: Catalyzes the reversible hydration of fumarate to (S)-malate. Functions in the generation of fumarate for use as an anaerobic electron acceptor. To a lesser extent, also displays D-tartrate dehydratase activity, but is not able to convert (R)-malate, L-tartrate or meso-tartrate. Is required for anaerobic growth on D-tartrate. {ECO:0000269|PubMed:17643228, ECO:0000269|PubMed:23405168, ECO:0000269|PubMed:3282546, ECO:0000269|Ref.6}. EcoCyc product frame: FUMB-MONOMER. Genomic coordinates: 4345680-4347326. EcoCyc protein note: Fumarase B (FumB) is one of three characterized fumarase isozymes in E. coli (encoded by EG10356, EG10357, and EG10358), all of which participate in the TCA cycle. FumB belongs to the class I fumarases; like FumA, it is a homodimeric 4Fe-4S cluster-containing protein . Fumarase B is required for anaerobic growth on D-tartrate and appears to be involved in biofilm formation . The cell adapts to changing environmental oxygen conditions by utilizing different isozymes. Both FumA and FumB contain iron-sulfur centers; exposure to oxidative agents such as superoxide results in damage to the metal cofactor and loss of enzyme activity...

## Biological Role

Activated by dcuR (protein.P0AD01).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P14407|protein.P14407]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AD01|protein.P0AD01]] `RegulonDB` `S` - regulator=DcuR; target=fumB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013501,ECOCYC:EG10357,GeneID:948642`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4345680-4347326:-; feature_type=gene
