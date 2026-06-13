---
entity_id: "gene.b4351"
entity_type: "gene"
name: "mrr"
source_database: "NCBI RefSeq"
source_id: "gene-b4351"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4351"
  - "mrr"
---

# mrr

`gene.b4351`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4351`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mrr (gene.b4351) is a gene entity. It encodes mrr (protein.P24202). Encoded protein function: FUNCTION: Involved in the acceptance of foreign DNA which is modified. Restricts both adenine- and cytosine-methylated DNA. EcoCyc product frame: EG10612-MONOMER. Genomic coordinates: 4586949-4587863. EcoCyc protein note: Mrr is a type IV restriction endonuclease involved in restriction of N6-adenine-methylated DNA and C5-cytosine-methylated DNA . Studies in which Mrr led to the induction of the SOS response suggest Mrr is an endonuclease that creates SOS-inducing double strand breaks in DNA containing N6-adenine-methylated DNA . Mrr is involved in the RecB-dependent high pressure induction of the SOS stress response in E. coli. mrr mutants were unable to induce the SOS response when exposed to high pressure while the SOS response resulting from direct damage to DNA remained unaffected. Expression of mrr does not increase upon high pressure treatment. Overexpression of mrr resulted in an approximately 500-fold increase in high pressure sensitivity . Mrr colocalizes with the nucleoid. Exposure to increased hydrostatic pressure leads to nucleoid condensation and to cellular blebbing; expression of the HhaII methyltransferase leads to formation of a more stable Mrr-nucleoid complex. mrr mutants that respond differently to these two conditions have been isolated...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24202|protein.P24202]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0014271,ECOCYC:EG10612,GeneID:948898`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4586949-4587863:+; feature_type=gene
