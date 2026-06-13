---
entity_id: "gene.b1640"
entity_type: "gene"
name: "anmK"
source_database: "NCBI RefSeq"
source_id: "gene-b1640"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1640"
  - "anmK"
---

# anmK

`gene.b1640`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1640`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

anmK (gene.b1640) is a gene entity. It encodes anmK (protein.P77570). Encoded protein function: FUNCTION: Catalyzes the specific phosphorylation of 1,6-anhydro-N-acetylmuramic acid (anhMurNAc) with the simultaneous cleavage of the 1,6-anhydro ring, generating MurNAc-6-P. Is required for the utilization of anhMurNAc either imported from the medium or derived from its own cell wall murein, and thus plays a role in cell wall recycling. {ECO:0000269|PubMed:15901686, ECO:0000269|PubMed:16452451}. EcoCyc product frame: G6880-MONOMER. EcoCyc synonyms: ydhH. Genomic coordinates: 1718493-1719602. EcoCyc protein note: AnmK is one of the enzymes responsible for the recycling of murein. Anhydro-N-acetylmuramic acid (anhMurNAc) is produced by the cleavage of muropeptide by NagZ (between the GlcNAc and the anhMurNAc moieties) and AmpD (between the anhMurNAc and peptide moieties), and AnmK catalyzes the hydrolysis of the 1,6-anhydro bond and simultaneous phosphorylation of anhMurNAc to N-acetylmuramate 6-phosphate. An etherase then cleaves the ether bond between the GlcNAc and D-lactate moieties of N-acetylmuramate 6-phosphate . In an anmK null mutant, anhMurNAc does not accumulate inside the cell, although no other enzyme activity that is able to modify anhMurNAc can be detected. When anhMurNAc can not be phosphorylated, it is lost into the medium instead . Review:

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77570|protein.P77570]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005488,ECOCYC:G6880,GeneID:946810`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1718493-1719602:-; feature_type=gene
