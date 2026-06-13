---
entity_id: "gene.b3230"
entity_type: "gene"
name: "rpsI"
source_database: "NCBI RefSeq"
source_id: "gene-b3230"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3230"
  - "rpsI"
---

# rpsI

`gene.b3230`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3230`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsI (gene.b3230) is a gene entity. It encodes rpsI (protein.P0A7X3). Encoded protein function: FUNCTION: The C-terminal tail plays a role in the affinity of the 30S P site for different tRNAs. Mutations that decrease this affinity are suppressed in the 70S ribosome. {ECO:0000269|PubMed:15308780}. EcoCyc product frame: EG10908-MONOMER. Genomic coordinates: 3377815-3378207. EcoCyc protein note: The S9 protein is a component of the 30S subunit of the ribosome. S9 was shown to crosslink to domains 3 and 4 of 16S rRNA and increases protection against ribunuclease digestion of the hairpin loop 41 near the 3' terminus of 16S rRNA by a mixture containing S7, S14, and S19 . The effect of S9 may be dependent on the presence of S14 . S7 is required for and accelerates binding of S9 to the 16S rRNA . S9 crosslinks to tRNA at the P site of the ribosome and weakly to tRNA at the A site . The assembly cofactors Era, RimM and RimP accelerate the binding rate of S9 during 30S assembly . Structural modelling suggested that the C-terminal region of S9 interacts with the P-site tRNA. Studies with rpsI mutants lacking this region show that the C-terminal tail is not essential for the function of S9, but such mutants have slower growth rates. In vitro, deletion of the C-terminal tail of S9 affects binding of tRNAs with anticodon stem sequences that are most divergent from initiator tRNAs...

## Biological Role

Repressed by rplM (protein.P0AA10), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7X3|protein.P0A7X3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0AA10|protein.P0AA10]] `RegulonDB` `S` - regulator=RplM; target=rpsI; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rpsI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010597,ECOCYC:EG10908,GeneID:949000`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3377815-3378207:-; feature_type=gene
