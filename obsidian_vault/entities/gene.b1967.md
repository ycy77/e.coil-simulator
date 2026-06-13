---
entity_id: "gene.b1967"
entity_type: "gene"
name: "hchA"
source_database: "NCBI RefSeq"
source_id: "gene-b1967"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1967"
  - "hchA"
---

# hchA

`gene.b1967`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1967`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hchA (gene.b1967) is a gene entity. It encodes hchA (protein.P31658). Encoded protein function: FUNCTION: Protein and nucleotide deglycase that catalyzes the deglycation of the Maillard adducts formed between amino groups of proteins or nucleotides and reactive carbonyl groups of glyoxals (PubMed:26102038, PubMed:26774339, PubMed:28596309). Thus, functions as a protein deglycase that repairs methylglyoxal- and glyoxal-glycated proteins, and releases repaired proteins and lactate or glycolate, respectively. Deglycates cysteine, arginine and lysine residues in proteins, and thus reactivates these proteins by reversing glycation by glyoxals. Is able to repair glycated serum albumin, aspartate aminotransferase, glyceraldehyde-3-phosphate dehydrogenase, and fructose biphosphate aldolase. Acts on early glycation intermediates (hemithioacetals and aminocarbinols), preventing the formation of Schiff bases and advanced glycation endproducts (AGE) that cause irreversible damage (PubMed:26102038, PubMed:26774339). Also functions as a nucleotide deglycase able to repair glycated guanine in the free nucleotide pool (GTP, GDP, GMP, dGTP) and in DNA and RNA. Is thus involved in a major nucleotide repair system named guanine glycation repair (GG repair), dedicated to reversing methylglyoxal and glyoxal damage via nucleotide sanitization and direct nucleic acid repair (PubMed:28596309)...

## Biological Role

Repressed by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), argR (protein.P0A6D0), hns (protein.P0ACF8), nac (protein.Q47005). Activated by rpoS (protein.P13445).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31658|protein.P31658]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=hchA; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=hchA; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=hchA; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=hchA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006529,ECOCYC:G7055,GeneID:946481`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2035835-2036686:+; feature_type=gene
