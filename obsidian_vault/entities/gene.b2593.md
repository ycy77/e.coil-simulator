---
entity_id: "gene.b2593"
entity_type: "gene"
name: "yfiH"
source_database: "NCBI RefSeq"
source_id: "gene-b2593"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2593"
  - "yfiH"
---

# yfiH

`gene.b2593`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2593`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfiH (gene.b2593) is a gene entity. It encodes yfiH (protein.P33644). Encoded protein function: FUNCTION: Purine nucleoside enzyme that catalyzes the phosphorolysis of adenosine and inosine nucleosides, yielding D-ribose 1-phosphate and the respective free bases, adenine and hypoxanthine (PubMed:31978345). Also catalyzes the phosphorolysis of S-methyl-5'-thioadenosine into adenine and S-methyl-5-thio-alpha-D-ribose 1-phosphate (PubMed:31978345). Also has adenosine deaminase activity (PubMed:31978345). May also act as a polyphenol oxidase: able to oxidize syringaldazine and 2,2'-azino-bis(3-ethylbenzthiazoline-6-sulfonic acid) (ABTS) in vitro (PubMed:16740638). {ECO:0000269|PubMed:16740638, ECO:0000269|PubMed:31978345}. EcoCyc product frame: EG12097-MONOMER. EcoCyc synonyms: yfiH. Genomic coordinates: 2734303-2735034. EcoCyc protein note: YfiH is a purine nucleoside phosphorylase; in vitro activity was tested with adenosine, S-methyl-5'-thioadenosine and inosine. The enzyme can also act as an adenosine deaminase . Earlier research showed that YfiH is a multicopper oxidase with polyphenol oxidase activity. Cyclic voltammetry measurements show that YfiH is a laccase with low redox potential . A yfiH deletion strain is more sensitive to ampicillin, cephradine and cephoxitin than wild type...

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33644|protein.P33644]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008530,ECOCYC:EG12097,GeneID:947089`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2734303-2735034:-; feature_type=gene
