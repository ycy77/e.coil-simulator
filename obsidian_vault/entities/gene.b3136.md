---
entity_id: "gene.b3136"
entity_type: "gene"
name: "agaS"
source_database: "NCBI RefSeq"
source_id: "gene-b3136"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3136"
  - "agaS"
---

# agaS

`gene.b3136`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3136`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

agaS (gene.b3136) is a gene entity. It encodes agaS (protein.P42907). Encoded protein function: FUNCTION: Catalyzes the isomerization-deamination of galactosamine 6-phosphate to form tagatofuranose 6-phosphate and ammonium ion. {ECO:0000250|UniProtKB:Q9KIP9}. EcoCyc product frame: G7634-MONOMER. EcoCyc synonyms: yraB. Genomic coordinates: 3281976-3283130. EcoCyc protein note: AgaS has been predicted to be an isomerase involved in N-acetylgalactosamine (GalNAc) utilization in some strains of E. coli . Because E. coli K-12 contains a partial deletion of the aga gene cluster and does not utilize GalNAc, functional studies have been carried out in E. coli C. There, a ΔagaS mutant becomes unable to utilize GalNAc . Expression of the agaS operon is induced by galactosamine and N--acetylgalactosamine and repressed by AgaR .

## Biological Role

Repressed by agaR (protein.P0ACK2). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42907|protein.P42907]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=agaS; function=+
- `represses` <-- [[protein.P0ACK2|protein.P0ACK2]] `RegulonDB` `S` - regulator=AgaR; target=agaS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010305,ECOCYC:G7634,GeneID:947645`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3281976-3283130:+; feature_type=gene
