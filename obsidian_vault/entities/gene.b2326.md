---
entity_id: "gene.b2326"
entity_type: "gene"
name: "epmC"
source_database: "NCBI RefSeq"
source_id: "gene-b2326"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2326"
  - "epmC"
---

# epmC

`gene.b2326`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2326`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

epmC (gene.b2326) is a gene entity. It encodes epmC (protein.P76938). Encoded protein function: FUNCTION: Is involved in the final hydroxylation step of the post-translational modification of translation elongation factor P (EF-P) on 'Lys-34'. Acts after beta-lysylation of 'Lys-34' by EpmA and EpmB. EpmC adds an oxygen atom to the C5 position of 'Lys-34' and does not modify the added beta-lysine. {ECO:0000269|PubMed:22706199}. EcoCyc product frame: G7201-MONOMER. EcoCyc synonyms: yfcM. Genomic coordinates: 2444203-2444751. EcoCyc protein note: EpmC catalyzes the hydroxylation of the γ (C4) or δ (C5) position of Lys34 in EG12099-MONOMER. The 5-hydroxyllysine form of EF-P appears to be present in vivo. EpmC is the final enzyme in the pathway generating the fully modified Lys34 residue . A crystal structure of EpmC has been solved at 1.45Å resolution . A metal-coordinating 2-His-1-carboxylate motif similar to that of non-heme iron enzymes forms the catalytic site . A catalytic mechanism has been proposed . EpmC: "EF-P post-translational modification C"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76938|protein.P76938]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007686,ECOCYC:G7201,GeneID:946807`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2444203-2444751:-; feature_type=gene
