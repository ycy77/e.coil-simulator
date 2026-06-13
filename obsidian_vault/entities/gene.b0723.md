---
entity_id: "gene.b0723"
entity_type: "gene"
name: "sdhA"
source_database: "NCBI RefSeq"
source_id: "gene-b0723"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0723"
  - "sdhA"
---

# sdhA

`gene.b0723`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0723`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sdhA (gene.b0723) is a gene entity. It encodes sdhA (protein.P0AC41). Encoded protein function: FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; the fumarate reductase is used in anaerobic growth, and the succinate dehydrogenase is used in aerobic growth. {ECO:0000269|PubMed:24374335, ECO:0000305|PubMed:12560550, ECO:0000305|PubMed:16407191, ECO:0000305|PubMed:19710024}. EcoCyc product frame: SDH-FLAVO. EcoCyc synonyms: dhsA. Genomic coordinates: 755907-757673. EcoCyc protein note: This is one of two catalytic subunits in the four subunit succinate dehydrogenase (SQR) enzyme. This subunit contains the FAD cofactor and the substrate-binding site . The redox potential of SdhA-bound FAD cofactor is -55.5 mV . Succinate, fumarate, citrate, and isocitrate appear to cause increased flavinylation of overproduced SdhA in cell extracts, indicating the existence of an activation mechanism involving TCA cycle intermediates . This protein has similarity to the FrdA subunit of fumarate reductase . A 2.2 Å crystal structure of L-aspartate oxidase suggests that an unusual tertiary structure is shared by L-aspartate oxidase, the SdhA subunit of succinate dehydrogenase, and the FrdA subunit of fumarate reductase . SdhA may play a role in bacteriophage T4 infection .

## Biological Role

Repressed by fur (protein.P0A9A9), arcA (protein.P0A9Q1). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), arcA (protein.P0A9Q1), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC41|protein.P0AC41]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sdhA; function=-+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sdhA; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sdhA; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sdhA; function=-+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sdhA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002466,ECOCYC:EG10931,GeneID:945402`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:755907-757673:+; feature_type=gene
