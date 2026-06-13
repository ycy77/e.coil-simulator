---
entity_id: "gene.b2541"
entity_type: "gene"
name: "hcaB"
source_database: "NCBI RefSeq"
source_id: "gene-b2541"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2541"
  - "hcaB"
---

# hcaB

`gene.b2541`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2541`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hcaB (gene.b2541) is a gene entity. It encodes hcaB (protein.P0CI31). Encoded protein function: FUNCTION: Converts 3-phenylpropionate-dihydrodiol (PP-dihydrodiol) and cinnamic acid-dihydrodiol (CI-dihydrodiol) into 3-(2,3-dihydroxylphenyl)propanoic acid (DHPP) and 2,3-dihydroxicinnamic acid (DHCI), respectively. {ECO:0000250, ECO:0000269|PubMed:9603882}. EcoCyc product frame: PHENPRODIOLDEHYDROG-MONOMER. EcoCyc synonyms: yfhX, phdD. Genomic coordinates: 2671225-2672037. EcoCyc protein note: Based on sequence similarity, HcaB is thought to encode 2,3-dihydroxy-2,3-dihydrophenylpropionate dehydrogenase . The HcaB enzyme has not been biochemically characterized. E. coli is able to utilize certain aromatic acids as carbon and energy sources. A meta-cleavage pathway involving HcaB is used for the catabolism of 3-phenylpropionate . An hcaB mutant does not grow on m-hydroxyphenylpropionate (MHP) as the sole source of carbon . HcaB: "hydroxycinnamic acid"

## Biological Role

Activated by hcaR (protein.Q47141).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CI31|protein.P0CI31]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47141|protein.Q47141]] `RegulonDB` `S` - regulator=HcaR; target=hcaB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008361,ECOCYC:G7335,GeneID:945346`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2671225-2672037:+; feature_type=gene
