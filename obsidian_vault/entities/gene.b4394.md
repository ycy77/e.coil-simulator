---
entity_id: "gene.b4394"
entity_type: "gene"
name: "yjjX"
source_database: "NCBI RefSeq"
source_id: "gene-b4394"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4394"
  - "yjjX"
---

# yjjX

`gene.b4394`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4394`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjjX (gene.b4394) is a gene entity. It encodes yjjX (protein.P39411). Encoded protein function: FUNCTION: Phosphatase that hydrolyzes non-canonical purine nucleotides such as XTP and ITP to their respective diphosphate derivatives. Probably excludes non-canonical purines from DNA/RNA precursor pool, thus preventing their incorporation into DNA/RNA and avoiding chromosomal lesions. ITP and XTP are the best substrates, followed by GDP and dITP. Is not active on dATP and dGTP, and exhibits no phosphatase activity toward pyrimidines (CTP, TTP, UTP, dCTP, and dTTP) (PubMed:16216582). Also seems to be implicated in the resistance against the thiamine metabolism inhibitors bacimethrin and CF3-HMP (PubMed:15292217). {ECO:0000269|PubMed:16216582, ECO:0000305|PubMed:15292217}. EcoCyc product frame: EG12600-MONOMER. Genomic coordinates: 4633233-4633745. EcoCyc protein note: YjjX is a phosphatase that preferentially hydrolyzes inosine triphosphate (ITP) and xanthosine triphosphate (XTP). Both ITP and XTP can be formed by oxidative deamination damage, converting an amino group of adenine or guanine to a keto group. By hydrolyzing these damaged nucleotides, YjjX may thus prevent their incorporation into RNA . A crystal structure of YjjX has been solved at 2.25 Å resolution; the protein forms a dimer in the crystal structure as well as in solution...

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39411|protein.P39411]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014411,ECOCYC:EG12600,GeneID:948919`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4633233-4633745:-; feature_type=gene
