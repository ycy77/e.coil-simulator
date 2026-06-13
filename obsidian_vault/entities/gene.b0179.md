---
entity_id: "gene.b0179"
entity_type: "gene"
name: "lpxD"
source_database: "NCBI RefSeq"
source_id: "gene-b0179"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0179"
  - "lpxD"
---

# lpxD

`gene.b0179`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0179`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lpxD (gene.b0179) is a gene entity. It encodes lpxD (protein.P21645). Encoded protein function: FUNCTION: Catalyzes the N-acylation of UDP-3-O-(hydroxytetradecanoyl)glucosamine using 3-hydroxytetradecanoyl-ACP as the acyl donor. Is involved in the biosynthesis of lipid A, a phosphorylated glycolipid that anchors the lipopolysaccharide to the outer membrane of the cell. Prefers (3R)-3-hydroxytetradecanoyl-ACP over (3R)-3-hydroxyhexadecanoyl-ACP as the acyl donor in vitro, which is consistent with the structure of E.coli lipid A that contains over 95% (R)-3-hydroxytetradecanoate at the 2 and 2' positions. {ECO:0000269|PubMed:19655786, ECO:0000269|PubMed:8444173}. EcoCyc product frame: UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-MONO. EcoCyc synonyms: omsA, firA. Genomic coordinates: 200971-201996.

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21645|protein.P21645]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=lpxD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000610,ECOCYC:EG10316,GeneID:944882`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:200971-201996:+; feature_type=gene
