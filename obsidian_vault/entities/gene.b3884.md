---
entity_id: "gene.b3884"
entity_type: "gene"
name: "csqR"
source_database: "NCBI RefSeq"
source_id: "gene-b3884"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3884"
  - "csqR"
---

# csqR

`gene.b3884`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3884`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csqR (gene.b3884) is a gene entity. It encodes csqR (protein.P32144). Encoded protein function: FUNCTION: Involved in the regulation of the sulfoquinovose operon (PubMed:24463506, PubMed:30372406). Represses the expression of the yihUTS operon and of the yihV and csqR genes. Binds DNA inside the spacer between the bidirectional transcription units comprising the yihUTS operon and the yihV gene, and upstream the csqR gene itself (PubMed:30372406). {ECO:0000269|PubMed:30372406, ECO:0000305|PubMed:24463506}. EcoCyc product frame: EG11849-MONOMER. EcoCyc synonyms: yihW. Genomic coordinates: 4074669-4075454. EcoCyc protein note: CsqR, formerly known as YihW and hypothesized to be a transcriptional regulator , functions as a repressor for genes of catabolism of sulfoquinovose (SQ), a hydrolysis product of sulfoquinovosyl diacylglycerol (SQDG) . CsqR belongs to the DeoR family of transcription factors and contains a helix-turn-helix motif to bind DNA in its N-terminal domain . It acts as a carbon source-dependent dual regulator involved in sustaining baseline growth in the absence of the lac operon . CsqR is likely involved in regulation of lactose metabolism and functions either in a complementary or opposite manner to a global regulator of carbohydrate metabolism, cAMP-CRP, and functions as a sugar-dependent dual regulator...

## Biological Role

Repressed by crp (protein.P0ACJ8), csqR (protein.P32144). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32144|protein.P32144]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=csqR; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=csqR; function=-+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=csqR; function=-+
- `represses` <-- [[protein.P32144|protein.P32144]] `RegulonDB` `S` - regulator=CsqR; target=csqR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012683,ECOCYC:EG11849,GeneID:948381`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4074669-4075454:+; feature_type=gene
