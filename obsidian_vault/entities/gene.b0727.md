---
entity_id: "gene.b0727"
entity_type: "gene"
name: "sucB"
source_database: "NCBI RefSeq"
source_id: "gene-b0727"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0727"
  - "sucB"
---

# sucB

`gene.b0727`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0727`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sucB (gene.b0727) is a gene entity. It encodes sucB (protein.P0AFG6). Encoded protein function: FUNCTION: E2 component of the 2-oxoglutarate dehydrogenase (OGDH) complex which catalyzes the second step in the conversion of 2-oxoglutarate to succinyl-CoA and CO(2). {ECO:0000305|PubMed:17367808}. EcoCyc product frame: SUCB-DIHYDROLIPOATE. Genomic coordinates: 761522-762739.

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fur (protein.P0A9A9), arcA (protein.P0A9Q1), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFG6|protein.P0AFG6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sucB; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sucB; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sucB; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sucB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=sucB; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sucB; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002480,ECOCYC:EG10980,GeneID:945307`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:761522-762739:+; feature_type=gene
