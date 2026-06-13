---
entity_id: "gene.b0597"
entity_type: "gene"
name: "entH"
source_database: "NCBI RefSeq"
source_id: "gene-b0597"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0597"
  - "entH"
---

# entH

`gene.b0597`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0597`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

entH (gene.b0597) is a gene entity. It encodes entH (protein.P0A8Y8). Encoded protein function: FUNCTION: Required for optimal enterobactin synthesis. Acts as a proofreading enzyme that prevents EntB misacylation by hydrolyzing the thioester bound existing between EntB and wrongly charged molecules. Displays esterase activity toward a wide range of substrates, including acyl-CoAs and aryl-CoAs. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:17675380, ECO:0000269|PubMed:19119850, ECO:0000269|PubMed:19193103, ECO:0000269|PubMed:24992697}. EcoCyc product frame: EG11105-MONOMER. EcoCyc synonyms: ybdB. Genomic coordinates: 629300-629713. EcoCyc protein note: EntH is a thioesterase that is involved in the biosynthesis of enterobactin . It acts as a proofreading enzyme that hydrolyzes misacylated EntB aryl intermediates . reports that the catalytic activity of EntH is sensitive to the pattern of hydroxyl groups on the aryl-CoA substrates , while saw no such effect. Although EntH can utilize both CoA and holo-EntB as the substrate thioester, holo-ACP is a very poor substrate . While EntH is not required for enterobactin synthesis in vitro , it is required for optimal synthesis in vivo . EntH interacts with phosphopantetheine-modified ENTB-CPLX EntB in vivo . Esterase activity of EntH was first discovered in a high-throughput screen of purified proteins...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Enriched Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8Y8|protein.P0A8Y8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002057,ECOCYC:EG11105,GeneID:945215`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:629300-629713:+; feature_type=gene
