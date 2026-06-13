---
entity_id: "gene.b1357"
entity_type: "gene"
name: "ydaS"
source_database: "NCBI RefSeq"
source_id: "gene-b1357"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1357"
  - "ydaS"
---

# ydaS

`gene.b1357`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1357`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydaS (gene.b1357) is a gene entity. It encodes ydaS (protein.P76063). Encoded protein function: FUNCTION: When overexpressed, it induces Rac prophage excision, possibly to counteract the lethal toxicity of YdaT (PubMed:38153127). Overexpression of ydaS or ydaST reduces growth and leads to loss of cell viability (PubMed:29205228). May contribute to toxicity and morphological defects (PubMed:29205229). {ECO:0000269|PubMed:29205228, ECO:0000269|PubMed:29205229, ECO:0000269|PubMed:38153127}. EcoCyc product frame: G6681-MONOMER. Genomic coordinates: 1420365-1420661. EcoCyc protein note: This Rac prophage gene was first identified in TAX-562 K-12 as a putative homolog of the λ phage cro gene that codes for a lytic regulator, and thus was indicated as a putative DNA-binding transcriptional regulator in the Rac prophage. G6681 is immediately upstream of G6682, coding for a putative lysogenic regulator and downstream of the divergently transcribed G6680, coding a transcriptional repressor . YdaS is involved in the excision of the Rac prophage, in which it is contained . The ydaST locus was computationally predicted to encode a toxin/antitoxin (TA) pair . However, no evidence for this function was found in a study aimed at validating and characterizing new TA loci in E. coli K-12 . The homologous YdaS protein from E...

## Biological Role

Repressed by racR (protein.P76062).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76063|protein.P76063]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P76062|protein.P76062]] `RegulonDB` `S` - regulator=RacR; target=ydaS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004552,ECOCYC:G6681,GeneID:945923`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1420365-1420661:+; feature_type=gene
