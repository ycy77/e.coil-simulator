---
entity_id: "gene.b0798"
entity_type: "gene"
name: "ybiA"
source_database: "NCBI RefSeq"
source_id: "gene-b0798"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0798"
  - "ybiA"
---

# ybiA

`gene.b0798`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0798`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybiA (gene.b0798) is a gene entity. It encodes ybiA (protein.P30176). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of the N-glycosidic bond in the first two intermediates of riboflavin biosynthesis, which are highly reactive metabolites, yielding relatively innocuous products. Thus, can divert a surplus of harmful intermediates into relatively harmless products and pre-empt the damage these intermediates would otherwise do. Helps maintain flavin levels. May act on other substrates in vivo. Has no activity against GTP, nucleoside monophosphates or ADP-ribose (PubMed:25431972). Is Required for swarming motility (PubMed:17122336). {ECO:0000269|PubMed:17122336, ECO:0000269|PubMed:25431972}. EcoCyc product frame: EG11579-MONOMER. Genomic coordinates: 832468-832950. EcoCyc protein note: YbiA catalyzes the hydrolysis of the N-glycosidic bond in DIAMINO-OH-PHOSPHORIBOSYLAMINO-PYR and CPD-602, highly reactive metabolites which are the first two intermediates in the RIBOSYN2-PWY pathway . Comparative genomics suggests that the YbiA family of proteins may play a role in NAD metabolism . Site-directed mutagenesis of conserved residues resulted in reduced or abolished catalytic activity. A ΔybiA mutant contains reduced amounts of FAD and FMN . A ybiA mutant has a defect in swarming, but not swimming motility .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30176|protein.P30176]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002722,ECOCYC:EG11579,GeneID:945426`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:832468-832950:-; feature_type=gene
