---
entity_id: "gene.b0678"
entity_type: "gene"
name: "nagB"
source_database: "NCBI RefSeq"
source_id: "gene-b0678"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0678"
  - "nagB"
---

# nagB

`gene.b0678`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0678`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nagB (gene.b0678) is a gene entity. It encodes nagB (protein.P0A759). Encoded protein function: FUNCTION: Catalyzes the reversible isomerization-deamination of glucosamine 6-phosphate (GlcN6P) to form fructose 6-phosphate (Fru6P) and ammonium ion. {ECO:0000269|PubMed:1734962, ECO:0000269|PubMed:2821923}. EcoCyc product frame: GLUCOSAMINE-6-P-DEAMIN-MONOMER. EcoCyc synonyms: glmD. Genomic coordinates: 702811-703611. EcoCyc protein note: Glucosamine-6-phosphate deaminase (NagB) catalyzes the second cytoplasmic reaction in the metabolism of N-acetyl-D-glucosamine. The deamination of glucosamine-6-phosphate generates ammonia and fructose-6-phosphate, which can enter glycolysis directly. Both N-acetylglucosamine and glucosamine can serve as the sole source of carbon for E. coli. Utilization of several amino sugars as carbon sources converges on NagB; additionally, NagB activity needs to be regulated to avoid a futile cycle with L-GLN-FRUCT-6-P-AMINOTRANS-MONOMER GlmS. It is therefore not surprising that a number of regulators have been identified to date. The first to be identified was the compound N-acetyl-D-glucosamine-6-phosphate (GlcNAc6P), which allosterically activates NagB . Both substrate binding and the allosteric transition are entropy-driven processes...

## Biological Role

Repressed by crp (protein.P0ACJ8), nagC (protein.P0AF20). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A759|protein.P0A759]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nagB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nagB; function=-+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nagB; function=-+
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=nagB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002304,ECOCYC:EG10633,GeneID:945290`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:702811-703611:-; feature_type=gene
