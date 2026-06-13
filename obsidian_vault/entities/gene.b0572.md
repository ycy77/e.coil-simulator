---
entity_id: "gene.b0572"
entity_type: "gene"
name: "cusC"
source_database: "NCBI RefSeq"
source_id: "gene-b0572"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0572"
  - "cusC"
---

# cusC

`gene.b0572`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0572`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cusC (gene.b0572) is a gene entity. It encodes cusC (protein.P77211). Encoded protein function: FUNCTION: Forms pores that allow passive diffusion of cations across the outer membrane. Part of a cation efflux system that mediates resistance to copper and silver. In pathogenic strains it allows the bacteria to invade brain microvascular endothelial cells (BMEC) thus allowing it to cross the blood-brain barrier and cause neonatal meningitis. {ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:12813074, ECO:0000269|PubMed:21249122}. EcoCyc product frame: G6320-MONOMER. EcoCyc synonyms: ibeB, ylcB. Genomic coordinates: 595600-596973. EcoCyc protein note: CusC is an outer membrane lipoprotein involved in the detoxification of copper and silver ions in E. coli as part of the CusCFBA copper/silver efflux system. A crystal structure of CusC has been solved to 2.3 Å. The CusC trimer forms a large continuous internal cavity with a cylindrical shape. Each monomer contributes 4 β strands to the outer membrane β barrel structure and 4 α helices to the periplasmic α barrel. The structure also suggests that CusC is triacylated at the N-terminal cysteine residue of each monomer . cusC exhibits mosaic evolution patterns in E. coli .

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), rpoD (protein.P00579), fur (protein.P0A9A9), cusR (protein.P0ACZ8), phoB (protein.P0AFJ5), hprR (protein.P76340).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77211|protein.P77211]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cusC; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=cusC; function=+
- `activates` <-- [[protein.P0ACZ8|protein.P0ACZ8]] `RegulonDB` `C` - regulator=CusR; target=cusC; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=cusC; function=+
- `activates` <-- [[protein.P76340|protein.P76340]] `RegulonDB` `S` - regulator=HprR; target=cusC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001958,ECOCYC:G6320,GeneID:946288`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:595600-596973:+; feature_type=gene
