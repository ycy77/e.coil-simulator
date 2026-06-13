---
entity_id: "gene.b3199"
entity_type: "gene"
name: "lptC"
source_database: "NCBI RefSeq"
source_id: "gene-b3199"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3199"
  - "lptC"
---

# lptC

`gene.b3199`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3199`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lptC (gene.b3199) is a gene entity. It encodes lptC (protein.P0ADV9). Encoded protein function: FUNCTION: Involved in the assembly of lipopolysaccharide (LPS). Required for the translocation of LPS from the inner membrane to the outer membrane. Facilitates the transfer of LPS from the inner membrane to the periplasmic protein LptA. Could be a docking site for LptA. {ECO:0000255|HAMAP-Rule:MF_01915, ECO:0000269|PubMed:16765569, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:20720015, ECO:0000269|PubMed:21169485, ECO:0000269|PubMed:21195693}. EcoCyc product frame: G7664-MONOMER. EcoCyc synonyms: yrbK. Genomic coordinates: 3342836-3343411. EcoCyc protein note: LptC is a component of the Lpt lipopolysaccharide (LPS) transport system in E. coli K-12. lptC is essential for growth . Depletion of lptC leads to growth arrest and irreversible cell damage; sensitivity to SDS and bile salts indicates a defective outer membrane . LptC contains a single N-terminal membrane spanning domain and a large soluble periplasmic domain . LptC forms a complex with LptF, LptG and LptB ; LptC interacts with LptA . LptC lacking the transmembrane (TM) region is functional and can bind the LptBFG inner membrane complex . LptC binds rough and smooth LPS in vitro (see also ). LptA can displace LPS from the purified periplasmic domain of LptC in vitro but not vice versa...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADV9|protein.P0ADV9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lptC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010508,ECOCYC:G7664,GeneID:947722`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3342836-3343411:+; feature_type=gene
