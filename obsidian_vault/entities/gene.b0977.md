---
entity_id: "gene.b0977"
entity_type: "gene"
name: "hyaF"
source_database: "NCBI RefSeq"
source_id: "gene-b0977"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0977"
  - "hyaF"
---

# hyaF

`gene.b0977`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0977`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hyaF (gene.b0977) is a gene entity. It encodes hyaF (protein.P19932). Encoded protein function: FUNCTION: Not known. Could enhance the incorporation of nickel to the hydrogenase. EcoCyc product frame: EG10473-MONOMER. Genomic coordinates: 1036749-1037606. EcoCyc protein note: The HyaF protein appeared to be required for the synthesis of active hydrogenase isoenzyme 1 (HYD1) . However, a hyaF in-frame deletion mutant does not show a serious defect in fumarate-dependent hydrogen oxidation, and hydrogenase 1 appears to be localized to the membrane correctly . Overexpression of hyaF increases the tolerance of E. coli to n-butanol .

## Biological Role

Repressed by iscR (protein.P0AGK8). Activated by ydeO (protein.P76135).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P19932|protein.P19932]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=hyaF; function=+
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=hyaF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003296,ECOCYC:EG10473,GeneID:945572`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1036749-1037606:+; feature_type=gene
