---
entity_id: "gene.b1771"
entity_type: "gene"
name: "ydjG"
source_database: "NCBI RefSeq"
source_id: "gene-b1771"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1771"
  - "ydjG"
---

# ydjG

`gene.b1771`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1771`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydjG (gene.b1771) is a gene entity. It encodes ydjG (protein.P77256). Encoded protein function: FUNCTION: Catalyzes the NADH-dependent reduction of methylglyoxal (2-oxopropanal) in vitro (PubMed:16813561). It is not known if this activity has physiological significance (PubMed:16813561). Cannot use NADPH as a cosubstrate (PubMed:16813561). Seems to play some role in intestinal colonization (PubMed:20562286). {ECO:0000269|PubMed:16813561, ECO:0000269|PubMed:20562286}. EcoCyc product frame: G6958-MONOMER. Genomic coordinates: 1854991-1855971. EcoCyc protein note: The YdjG protein belongs to subfamily 11 of the aldo-keto reductase superfamily. Members of this family generally use NADPH as the cosubstrate, although some are able to use both NADH and NADPH. YdjG is the first member of this family that is only able to use NADH. The crystal structure of the dual-specificity xylose reductase from Candida tenuis identified a conserved glutamic acid residue which appears to allow binding of both NAD+ and NADP+. Mutagenesis of the analogous residue in YdjG, D232A or D232E, converts YdjG into a dual-specificity enzyme . The purified enzyme was found to possess a relatively high activity with methylglyoxal as the substrate (Kcat = 15.7 s-1) . The physiological significance of this activity has not been investigated...

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77256|protein.P77256]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005901,ECOCYC:G6958,GeneID:946283`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1854991-1855971:-; feature_type=gene
