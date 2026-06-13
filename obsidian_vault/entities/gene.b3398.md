---
entity_id: "gene.b3398"
entity_type: "gene"
name: "igaA"
source_database: "NCBI RefSeq"
source_id: "gene-b3398"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3398"
  - "igaA"
---

# igaA

`gene.b3398`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3398`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

igaA (gene.b3398) is a gene entity. It encodes yrfF (protein.P45800). Encoded protein function: Putative membrane protein IgaA homolog EcoCyc product frame: G7741-MONOMER. EcoCyc synonyms: yrfF. Genomic coordinates: 3526469-3528604. EcoCyc protein note: IgaA is an essential inner membrane protein which inhibits the PWY0-1493; IgaA acts downstream of RcsF in the Rcs signaling pathway; current models suggest that IgaA interacts physically with either RcsC or RcsD to regulate kinase/phosphatase activity (see ). igaA is essential in E. coli K-12; an igaA deletion is viable when combined with deletions of rcsB, rcsC or rcsD; IgaA forms a complex with RcsF in vivo; depletion of IgaA activates the Rcs signaling pathway independently of RcsF; IgaA exerts an inhibitory effect on the Rcs signaling cascade . RcsF-IgaA complex levels increase in response to peptidoglycan stress (mecillinam treatment); under stress conditions RcsF interacts with the periplasmic domain of IgaA resulting in activation of the Rcs system . IgaA is an inner membrane protein predicted to contain 5 transmembrane domains with two cytosolic domains at the N-terminus and one large periplasmic domain close to the C-terminus...

## Biological Role

Activated by arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45800|protein.P45800]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=igaA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011090,ECOCYC:G7741,GeneID:947905`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3526469-3528604:+; feature_type=gene
