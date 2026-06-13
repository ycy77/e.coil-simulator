---
entity_id: "gene.b0385"
entity_type: "gene"
name: "dgcC"
source_database: "NCBI RefSeq"
source_id: "gene-b0385"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0385"
  - "dgcC"
---

# dgcC

`gene.b0385`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0385`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgcC (gene.b0385) is a gene entity. It encodes dgcC (protein.P0AAP1). Encoded protein function: FUNCTION: A probable diguanylate cyclase. The last member of a cascade of expressed proteins, its expression requires DgcM. DgcC production induces biosynthesis of cellulose in some E.coli isolates, but not in K12 strains. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. {ECO:0000269|PubMed:11260463, ECO:0000269|PubMed:19707751}. EcoCyc product frame: EG11257-MONOMER. EcoCyc synonyms: yaiC, adrA. Genomic coordinates: 403703-404818.

## Biological Role

Activated by rpoS (protein.P13445), csgD (protein.P52106).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAP1|protein.P0AAP1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=dgcC; function=+
- `activates` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=dgcC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001336,ECOCYC:EG11257,GeneID:945037`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:403703-404818:+; feature_type=gene
