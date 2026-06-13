---
entity_id: "gene.b1023"
entity_type: "gene"
name: "pgaB"
source_database: "NCBI RefSeq"
source_id: "gene-b1023"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1023"
  - "pgaB"
---

# pgaB

`gene.b1023`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1023`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pgaB (gene.b1023) is a gene entity. It encodes pgaB (protein.P75906). Encoded protein function: FUNCTION: Catalyzes the N-deacetylation of poly-beta-1,6-N-acetyl-D-glucosamine (PGA), a biofilm adhesin polysaccharide. N-deacetylation promotes PGA export through the PgaA porin. {ECO:0000269|PubMed:15090514, ECO:0000269|PubMed:18359807}. EcoCyc product frame: G6530-MONOMER. EcoCyc synonyms: hmsF, ycdR. Genomic coordinates: 1087839-1089857. EcoCyc protein note: PgaB is an outer membrane lipoprotein that is required for the partial de-N-acetylation and hydrolysis of poly-β-1,6-N-acetyl-D-glucosamine (known as PGA or PNAG) - an exopolysaccharide that is a key component of the biofilm matrix of many pathogenic bacteria . PgaB interacts with the outer membrane porin G6531-MONOMER PgaA and this interaction is implicated in the export of deacetylated PNAG . PgaB consists of an N-terminal deacetylase domain that has a distorted (β/α)7 barrel fold and belongs to the class 4 carbohydrate esterases and a C-terminal glycoside hydrolase (GH) domain that has a (β/α)8 barrel fold and belongs to a newly defined GH family - GH153 . Both domains are necessary for de-N-acetylation of PNAG; a cleft formed between the N and C-terminal domains is proposed to bind PNAG in an extended conformation during deacetylation...

## Biological Role

Repressed by ompR (protein.P0AA16), csrA (protein.P69913). Activated by nhaR (protein.P0A9G2).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75906|protein.P75906]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9G2|protein.P0A9G2]] `RegulonDB` `S` - regulator=NhaR; target=pgaB; function=+
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=pgaB; function=-
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `C` - regulator=carbon storage regulator CsrA; target=pgaB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003467,ECOCYC:G6530,GeneID:945604`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1087839-1089857:-; feature_type=gene
