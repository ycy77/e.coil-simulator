---
entity_id: "gene.b1297"
entity_type: "gene"
name: "puuA"
source_database: "NCBI RefSeq"
source_id: "gene-b1297"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1297"
  - "puuA"
---

# puuA

`gene.b1297`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1297`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

puuA (gene.b1297) is a gene entity. It encodes puuA (protein.P78061). Encoded protein function: FUNCTION: Involved in the breakdown of putrescine. Catalyzes the ATP-dependent gamma-glutamylation of putrescine, producing gamma-L-glutamylputrescine. Absolutely essential to utilize putrescine as both nitrogen and carbon sources and to decrease the toxicity of putrescine, which can lead to inhibition of cell growth and protein synthesis. In vitro is also able to use several diamines, and spermidine and spermine, instead of putrescine, but with a much lower activity, and cannot catalyze the gamma-glutamylation of ornithine or GABA (PubMed:18495664). {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:18495664}. EcoCyc product frame: G6644-MONOMER. EcoCyc synonyms: ycjK. Genomic coordinates: 1359490-1360908. EcoCyc protein note: Glutamate-putrescine ligase is the first enzyme in the primary putrescine utilization pathway of E. coli . It catalyzes the ATP-dependent γ-glutamylation of putrescine. The function of genes in the puu gene cluster was initially inferred by similarity with the ipuABCDEGFH operon in Pseudomonas sp. . PuuA has similarity to glutamine synthetase; based on this similarity, predicted active site residues were mutagenized, and the resulting enzymes show little activity . A puuA deletion mutant can not grow on putrescine as the sole source of carbon or nitrogen...

## Biological Role

Repressed by DNA-binding transcriptional regulator PtrR-L-glutamine (complex.ecocyc.CPLX0-10428), AcrR-3,6-diaminoacridine (complex.ecocyc.CPLX0-8952), arcA (protein.P0A9Q1), puuR (protein.P0A9U6).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P78061|protein.P78061]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `represses` <-- [[complex.ecocyc.CPLX0-10428|complex.ecocyc.CPLX0-10428]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-8952|complex.ecocyc.CPLX0-8952]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=puuA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9U6|protein.P0A9U6]] `RegulonDB` `C` - regulator=PuuR; target=puuA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004365,ECOCYC:G6644,GeneID:946202`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1359490-1360908:-; feature_type=gene
