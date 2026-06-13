---
entity_id: "gene.b1107"
entity_type: "gene"
name: "nagZ"
source_database: "NCBI RefSeq"
source_id: "gene-b1107"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1107"
  - "nagZ"
---

# nagZ

`gene.b1107`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1107`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nagZ (gene.b1107) is a gene entity. It encodes nagZ (protein.P75949). Encoded protein function: FUNCTION: Plays a role in peptidoglycan recycling by cleaving the terminal beta-1,4-linked N-acetylglucosamine (GlcNAc) from peptide-linked peptidoglycan fragments, giving rise to free GlcNAc, anhydro-N-acetylmuramic acid and anhydro-N-acetylmuramic acid-linked peptides. Cleaves GlcNAc linked beta-1,4 to MurNAc tripeptides. EcoCyc product frame: G6567-MONOMER. EcoCyc synonyms: ycfO. Genomic coordinates: 1164095-1165120. EcoCyc protein note: β-N-acetylglucosaminidase (NagZ) is a cytoplasmic enzyme involved in murein recycling. NagZ is specific for hydrolysis of the β-1,4 glycosidic bond, generating monosaccharides from the disaccharides released during muropeptide recycling. The enzyme cleaves anhydromuropeptides and is also active with muropeptides . A mutant strain lacking more than 99% of NagZ activity shows no apparent growth defect . A nagZ insertion mutant contains much increased amounts of the GlcNAc-β-1,4-anhydro-MurNAc disaccharide . The nagZ mRNA was predicted to be a regulatory hub for post-transcriptional regulation by small RNAs. Overexpression of RyhB and FnrS represses translation . NagZ: "β-N-acetylglucosaminidase" Reviews:

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01501` beta-Lactam resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75949|protein.P75949]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003737,ECOCYC:G6567,GeneID:945671`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1164095-1165120:+; feature_type=gene
