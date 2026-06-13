---
entity_id: "gene.b0774"
entity_type: "gene"
name: "bioA"
source_database: "NCBI RefSeq"
source_id: "gene-b0774"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0774"
  - "bioA"
---

# bioA

`gene.b0774`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0774`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bioA (gene.b0774) is a gene entity. It encodes bioA (protein.P12995). Encoded protein function: FUNCTION: Catalyzes the transfer of the alpha-amino group from S-adenosyl-L-methionine (SAM) to 7-keto-8-aminopelargonic acid (KAPA) to form 7,8-diaminopelargonic acid (DAPA) (PubMed:1092681, PubMed:1092682). It is the only animotransferase known to utilize SAM as an amino donor (PubMed:1092681, PubMed:1092682). Complements a bioU deletion in Synechocystis PCC 6803 (PubMed:32042199). {ECO:0000269|PubMed:1092681, ECO:0000269|PubMed:1092682, ECO:0000269|PubMed:32042199}. EcoCyc product frame: DAPASYN-MONOMER. Genomic coordinates: 807968-809257.

## Biological Role

Repressed by birA (protein.P06709).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P12995|protein.P12995]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P06709|protein.P06709]] `RegulonDB` `S` - regulator=BirA; target=bioA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002635,ECOCYC:EG10117,GeneID:945376`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:807968-809257:-; feature_type=gene
