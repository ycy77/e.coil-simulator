---
entity_id: "gene.b3994"
entity_type: "gene"
name: "thiC"
source_database: "NCBI RefSeq"
source_id: "gene-b3994"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3994"
  - "thiC"
---

# thiC

`gene.b3994`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3994`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiC (gene.b3994) is a gene entity. It encodes thiC (protein.P30136). Encoded protein function: FUNCTION: Catalyzes the synthesis of the hydroxymethylpyrimidine phosphate (HMP-P) moiety of thiamine from aminoimidazole ribotide (AIR) in a radical S-adenosyl-L-methionine (SAM)-dependent reaction. {ECO:0000305|PubMed:15292217, ECO:0000305|PubMed:15326535}. EcoCyc product frame: THIC-MONOMER. Genomic coordinates: 4194204-4196099. EcoCyc protein note: HMP-P synthase (ThiC) catalyzes the conversion of 5-aminoimidazole (AIR) into 4-amino-hydroxymethyl-2-methylpyrimidine phosphate (HMP-P) . ThiC was demonstrated to be a novel member of the radical S-adenosylmethionine (SAM) superfamily, also known as AdoMet superfamily . The role of the radical SAM proteins in the ThiC-catalyzed complex rearrangement reaction has been investigated . The labelling pattern of the conversion of AIR to HMP-P has been studied in detail, and potential reaction mechanisms were proposed. ThiC activity was enhanced by SAM and nicotinamide cofactors. SAM is neither used as a methyl donor, nor is it cleaved to the adenosyl radical; its role in the reaction is thus unclear. The reaction is dependent on the presence of an additional protein, which has not been identified yet . ThiC has been extensively studied in Salmonella enterica...

## Biological Role

Repressed by arcA (protein.P0A9Q1), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30136|protein.P30136]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=thiC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013057,ECOCYC:EG11585,GeneID:948492`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4194204-4196099:-; feature_type=gene
