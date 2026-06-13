---
entity_id: "gene.b2421"
entity_type: "gene"
name: "cysM"
source_database: "NCBI RefSeq"
source_id: "gene-b2421"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2421"
  - "cysM"
---

# cysM

`gene.b2421`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2421`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysM (gene.b2421) is a gene entity. It encodes cysM (protein.P16703). Encoded protein function: FUNCTION: Two cysteine synthase enzymes are found. Both catalyze the same reaction. Cysteine synthase B can also use thiosulfate in place of sulfide to give cysteine thiosulfonate as a product. EcoCyc product frame: ACSERLYB-MONOMER. Genomic coordinates: 2538672-2539583. EcoCyc protein note: Cysteine synthase B (CysM) is one of two isozymes in E. coli that catalyze the formation of L-cysteine from O-acetyl-L-serine and sulfide . Unlike cysteine synthase A, cysteine synthase B does not form a complex with serine acetyltransferase . Cysteine synthase B can also use thiosulfate in place of sulfide, producing S-sulfocysteine . The broad substrate specificity of cysteine synthase was exploited for the synthesis of unnatural L-α-amino acids . Initial synthesis rates of nonproteinaceous amino acids have been determined . CysM provides one of the activities that is able to provide sulfur for Fe-S cluster biosynthesis in vitro . CysM is one of at least five enzymes that exhibit cysteine desulfhydrase activity (CD) in E. coli. Deletion of each of the cysM, metC, tnaA, cysK and malY genes individually decreases CD activity Crystal structures of CysM have been solved at 2.1, 2.7 and 1.33 Å resolution...

## Biological Role

Activated by rpoD (protein.P00579), cysB (protein.P0A9F3).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16703|protein.P16703]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cysM; function=+
- `activates` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=cysM; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007982,ECOCYC:EG10193,GeneID:946888`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2538672-2539583:-; feature_type=gene
