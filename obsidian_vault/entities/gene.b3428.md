---
entity_id: "gene.b3428"
entity_type: "gene"
name: "glgP"
source_database: "NCBI RefSeq"
source_id: "gene-b3428"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3428"
  - "glgP"
---

# glgP

`gene.b3428`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3428`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glgP (gene.b3428) is a gene entity. It encodes glgP (protein.P0AC86). Encoded protein function: FUNCTION: Phosphorylase is an important allosteric enzyme in carbohydrate metabolism. Enzymes from different sources differ in their regulatory mechanisms and in their natural substrates. However, all known phosphorylases share catalytic and structural properties. EcoCyc product frame: GLYCOPHOSPHORYL-MONOMER. EcoCyc synonyms: glgY. Genomic coordinates: 3564134-3566581.

## Biological Role

Repressed by csrA (protein.P69913). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC86|protein.P0AC86]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=glgP; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=glgP; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=glgP; function=+
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `S` - regulator=carbon storage regulator CsrA; target=glgP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011198,ECOCYC:EG10380,GeneID:947931`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3564134-3566581:-; feature_type=gene
