---
entity_id: "gene.b1301"
entity_type: "gene"
name: "puuB"
source_database: "NCBI RefSeq"
source_id: "gene-b1301"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1301"
  - "puuB"
---

# puuB

`gene.b1301`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1301`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

puuB (gene.b1301) is a gene entity. It encodes puuB (protein.P37906). Encoded protein function: FUNCTION: Involved in the breakdown of putrescine via the oxidation of L-glutamylputrescine. {ECO:0000269|PubMed:15590624}. EcoCyc product frame: EG11822-MONOMER. EcoCyc synonyms: ycjA, ordL. Genomic coordinates: 1364232-1365512. EcoCyc protein note: PuuB is probably the γ-glutamylputrescine oxidase in a putrescine utilization pathway; together with PuuC, γ-glutamyl-γ-aminobutyrate is produced from γ-glutamylputrescine . The function of genes in the puu gene cluster was initially inferred by similarity with the ipuABCDEGFH operon in Pseudomonas sp. . Loss of PuuB in a strain without PatA prevents putrescine utilization . The puuC, puuB, and puuE genes may form an operon .

## Biological Role

Repressed by puuR (protein.P0A9U6). Activated by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0), fimZ (protein.P0AEL8).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37906|protein.P37906]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=puuB; function=+
- `activates` <-- [[protein.P0AEL8|protein.P0AEL8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9U6|protein.P0A9U6]] `RegulonDB` `S` - regulator=PuuR; target=puuB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004378,ECOCYC:EG11822,GeneID:945072`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1364232-1365512:+; feature_type=gene
