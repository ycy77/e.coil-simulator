---
entity_id: "gene.b0174"
entity_type: "gene"
name: "ispU"
source_database: "NCBI RefSeq"
source_id: "gene-b0174"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0174"
  - "ispU"
---

# ispU

`gene.b0174`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0174`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ispU (gene.b0174) is a gene entity. It encodes ispU (protein.P60472). Encoded protein function: FUNCTION: Generates ditrans,octacis-undecaprenyl pyrophosphate (UPP) from isopentenyl pyrophosphate (IPP) and farnesyl diphosphate (FPP). UPP is the precursor of glycosyl carrier lipid in the biosynthesis of bacterial cell wall polysaccharide components such as peptidoglycan and lipopolysaccharide. {ECO:0000269|PubMed:12756244}. EcoCyc product frame: UPPSYN-MONOMER. EcoCyc synonyms: uppS, rth, yaeS. Genomic coordinates: 194903-195664. EcoCyc protein note: Undecaprenyl pyrophosphate (UPP) synthase (IspU) catalyzes the condensation reactions resulting in the formation of UPP, a di-trans,poly-cis-undecaprenyl pyrophosphate that functions as the lipid carrier for bacterial cell wall carbohydrates. To generate UPP, eight isopentenyl diphosphate molecules are sequentially added to farnesyl diphosphate with cis stereochemistry . Under various reaction conditions, the enzyme can produce C50 intermediates as well as larger C60-C75 products in addition to UPP. Triton X-100 activates the reaction by accelerating a step after the rate-limiting IPP condensation reactions . Site-directed mutagenesis of conserved residues identified amino acids that are required for catalysis and/or play a role in binding of IPP , and play a role in product chain length determination...

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60472|protein.P60472]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000595,ECOCYC:G6092,GeneID:944874`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:194903-195664:+; feature_type=gene
