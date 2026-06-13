---
entity_id: "gene.b0726"
entity_type: "gene"
name: "sucA"
source_database: "NCBI RefSeq"
source_id: "gene-b0726"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0726"
  - "sucA"
---

# sucA

`gene.b0726`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0726`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sucA (gene.b0726) is a gene entity. It encodes sucA (protein.P0AFG3). Encoded protein function: FUNCTION: E1 component of the 2-oxoglutarate dehydrogenase (OGDH) complex which catalyzes the decarboxylation of 2-oxoglutarate, the first step in the conversion of 2-oxoglutarate to succinyl-CoA and CO(2). {ECO:0000269|PubMed:17367808}. EcoCyc product frame: E1O-MONOMER. EcoCyc synonyms: lys+met. Genomic coordinates: 758706-761507.

## Biological Role

Repressed by glnZ (gene.b4836), arcA (protein.P0A9Q1), nac (protein.Q47005). Activated by rpoD (protein.P00579), fur (protein.P0A9A9), arcA (protein.P0A9Q1), crp (protein.P0ACJ8), rpoS (protein.P13445), nac (protein.Q47005).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFG3|protein.P0AFG3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sucA; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sucA; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sucA; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sucA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=sucA; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=sucA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4836|gene.b4836]] `RegulonDB` `S` - regulator=GlnZ; target=sucA; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sucA; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=sucA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002478,ECOCYC:EG10979,GeneID:945303`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:758706-761507:+; feature_type=gene
