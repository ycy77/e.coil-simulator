---
entity_id: "gene.b3611"
entity_type: "gene"
name: "yibN"
source_database: "NCBI RefSeq"
source_id: "gene-b3611"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3611"
  - "yibN"
---

# yibN

`gene.b3611`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3611`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yibN (gene.b3611) is a gene entity. It encodes yibN (protein.P0AG27). Encoded protein function: Uncharacterized protein YibN EcoCyc product frame: EG12295-MONOMER. Genomic coordinates: 3784584-3785015. EcoCyc protein note: No information about this protein was found by a literature search conducted on March 15, 2017.

## Biological Role

Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), rpoD (protein.P00579), fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG27|protein.P0AG27]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yibN; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=yibN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011805,ECOCYC:EG12295,GeneID:948131`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3784584-3785015:-; feature_type=gene
