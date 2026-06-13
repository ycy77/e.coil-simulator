---
entity_id: "gene.b1611"
entity_type: "gene"
name: "fumC"
source_database: "NCBI RefSeq"
source_id: "gene-b1611"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1611"
  - "fumC"
---

# fumC

`gene.b1611`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1611`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fumC (gene.b1611) is a gene entity. It encodes fumC (protein.P05042). Encoded protein function: FUNCTION: Involved in the TCA cycle. FumC seems to be a backup enzyme for FumA under conditions of iron limitation and oxidative stress (PubMed:7592392). Catalyzes the stereospecific interconversion of fumarate to L-malate (PubMed:1917897, PubMed:3282546). {ECO:0000269|PubMed:1917897, ECO:0000269|PubMed:3282546, ECO:0000269|PubMed:7592392, ECO:0000305|PubMed:8496960}. EcoCyc product frame: FUMC-MONOMER. Genomic coordinates: 1685185-1686588. EcoCyc protein note: Fumarase C (FumC) is one of three characterized fumarase isozymes in E. coli (encoded by EG10356, EG10357, and EG10358), all of which participate in the TCA cycle. FumC is a tetrameric protein and belongs to the class II, iron-independent fumarases . The cell adapts to changing environmental oxygen conditions by utilizing different isozymes. Both FumA and FumB contain iron-sulfur centers; exposure to oxidative agents such as superoxide results in damage to the metal cofactor and loss of enzyme activity . In contrast, FumC is an iron-independent enzyme and is insensitive to oxidative damage . FumC is made by the cells primarily as a backup enzyme if the FumA or FumB enzymes are damaged by reactive oxygen species. Crystal structures of fumarase C have been solved, allowing identification of the active site...

## Biological Role

Activated by soxS (protein.P0A9E2), marA (protein.P0ACH5), rob (protein.P0ACI0), soxR (protein.P0ACS2), rpoS (protein.P13445).

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

- `encodes` --> [[protein.P05042|protein.P05042]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=fumC; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=fumC; function=+
- `activates` <-- [[protein.P0ACI0|protein.P0ACI0]] `RegulonDB` `S` - regulator=Rob; target=fumC; function=+
- `activates` <-- [[protein.P0ACS2|protein.P0ACS2]] `RegulonDB` `S` - regulator=SoxR; target=fumC; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=fumC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005380,ECOCYC:EG10358,GeneID:946147`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1685185-1686588:-; feature_type=gene
