---
entity_id: "gene.b0574"
entity_type: "gene"
name: "cusB"
source_database: "NCBI RefSeq"
source_id: "gene-b0574"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0574"
  - "cusB"
---

# cusB

`gene.b0574`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0574`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cusB (gene.b0574) is a gene entity. It encodes cusB (protein.P77239). Encoded protein function: FUNCTION: Part of a cation efflux system that mediates resistance to copper and silver. {ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:12813074}. EcoCyc product frame: G6322-MONOMER. EcoCyc synonyms: ylcD. Genomic coordinates: 597479-598702. EcoCyc protein note: CusB is a membrane fusion protein involved in the detoxification of copper and silver ions in E. coli as part of the CusCFBA copper/silver efflux system. CusB is monomeric in solution . Three methionine residues (M21, M36, M38) ligate the metal substrate in a 1:1 stoichiometry . Crystal structures of CusB in the absence and presence of silver and copper ions have been described; CusB consists of 4 major domains: 3 β-strand domains and one α-helical domain; two distinct conformations of CusB were found in single crystals suggesting that CusB exhibits conformational flexibility . The function of a membrane fusion protein like CusB may be to bring the outer membrane factor, CusC, closer to the resistance-nodulation-division permease, CusA, consistent with the 'funnel' model of efflux. Alternatively CusB may act as a switch whereby metal binding to CusB promotes opening of a CusA channel and docking of substrate-loaded CusF (reviewed in )...

## Biological Role

Activated by rpoD (protein.P00579), cusR (protein.P0ACZ8), phoB (protein.P0AFJ5), hprR (protein.P76340).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77239|protein.P77239]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cusB; function=+
- `activates` <-- [[protein.P0ACZ8|protein.P0ACZ8]] `RegulonDB` `C` - regulator=CusR; target=cusB; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=cusB; function=+
- `activates` <-- [[protein.P76340|protein.P76340]] `RegulonDB` `S` - regulator=HprR; target=cusB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001969,ECOCYC:G6322,GeneID:945189`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:597479-598702:+; feature_type=gene
