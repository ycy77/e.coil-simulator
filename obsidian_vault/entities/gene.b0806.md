---
entity_id: "gene.b0806"
entity_type: "gene"
name: "mcbA"
source_database: "NCBI RefSeq"
source_id: "gene-b0806"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0806"
  - "mcbA"
---

# mcbA

`gene.b0806`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0806`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mcbA (gene.b0806) is a gene entity. It encodes mcbA (protein.P0AAX6). Encoded protein function: FUNCTION: Affects biofilm formation and mucoidy. {ECO:0000269|PubMed:18309357}. EcoCyc product frame: G6415-MONOMER. EcoCyc synonyms: ybiM. Genomic coordinates: 841796-842056. EcoCyc protein note: McbA (YbiM) is a predicted periplasmic protein and a member of the YhcN family which has nine paralogous proteins in E. coli. This family of proteins is thought to be important in cell-cell contact or intercellular signaling . Expression of McbA is repressed by McbR. Deleting McbR allows expression which leads to overproduction of colanic acid, causing mucoidy, which prevents biofilm production in E. coli. Based on a microarray assay to identify genes relevant to the interaction between the bacterium and lettuce plant, the mcbA gene, involved in biofilm modulation, was found to be significantly upregulated . McbA: "regulated by MqsR-controlled colanic acid and biofilm regulator"

## Biological Role

Repressed by mcbR (protein.P76114), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAX6|protein.P0AAX6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P76114|protein.P76114]] `RegulonDB` `S` - regulator=McbR; target=mcbA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=mcbA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002753,ECOCYC:G6415,GeneID:947523`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:841796-842056:-; feature_type=gene
