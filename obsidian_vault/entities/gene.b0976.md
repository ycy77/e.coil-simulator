---
entity_id: "gene.b0976"
entity_type: "gene"
name: "hyaE"
source_database: "NCBI RefSeq"
source_id: "gene-b0976"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0976"
  - "hyaE"
---

# hyaE

`gene.b0976`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0976`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyaE (gene.b0976) is a gene entity. It encodes hyaE (protein.P19931). Encoded protein function: FUNCTION: Not known. Could form, along with HyaD, a complex involved in the processing of the hydrogenase 1 structural operon. EcoCyc product frame: EG10472-MONOMER. Genomic coordinates: 1036354-1036752. EcoCyc protein note: HyaE appears to be a non-essential chaperone that is specific for the β subunit of hydrogenase isoenzyme 1 (HYD1), HyaA. In a bacterial two-hybrid assay, HyaE was shown to interact with the Tat signal peptide-containing precursor of HyaA, but not the mature HyaA protein . A solution structure of HyaE has been determined, showing a thioredoxin-like fold. However, HyaE is not expected to have thioredoxin-like catalytic activity, because it does not contain the Cys-X-X-Cys catalytic motif . Some of the most highly conserved residues among HyaE-like proteins are negatively charged residues that map to a surface region and might interact with the positively charged Tat signal peptide of HyaA . The HyaE protein appeared to be required for the synthesis of active HYD1 . However, a hyaE in-frame deletion mutant does not show a serious defect in fumarate-dependent hydrogen oxidation, and HYD1 appears to be localized to the membrane correctly . Overexpression of hyaE from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hypochlorous acid . Review:

## Biological Role

Repressed by iscR (protein.P0AGK8). Activated by ydeO (protein.P76135).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19931|protein.P19931]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=hyaE; function=+
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=hyaE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003294,ECOCYC:EG10472,GeneID:945573`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1036354-1036752:+; feature_type=gene
