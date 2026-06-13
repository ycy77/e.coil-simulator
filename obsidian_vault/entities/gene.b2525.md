---
entity_id: "gene.b2525"
entity_type: "gene"
name: "fdx"
source_database: "NCBI RefSeq"
source_id: "gene-b2525"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2525"
  - "fdx"
---

# fdx

`gene.b2525`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2525`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fdx (gene.b2525) is a gene entity. It encodes fdx (protein.P0A9R4). Encoded protein function: FUNCTION: Ferredoxin are iron-sulfur proteins that transfer electrons in a wide variety of metabolic reactions. Although the function of this ferredoxin is unknown it is probable that it has a role as a cellular electron transfer protein. Involved in the in vivo assembly of the Fe-S clusters in a wide variety of iron-sulfur proteins. EcoCyc product frame: OX-FERREDOXIN. Genomic coordinates: 2656748-2657083. EcoCyc protein note: Ferredoxin (Fdx) contains a [2Fe-2S] cluster and functions in Fe-S cluster assembly . Fdx interacts directly with G7325-MONOMER IscS and supplies one of the two electrons needed for reduction of S0 to IscS. Fdx and G7324-MONOMER IscU compete for overlapping binding sites on IscS . Holo-IscA , holo-GrxD, and the GrxD-BolA heterodimer can transfer an [2Fe-2S] cluster to apo-Fdx in vitro. A crystal structure of Fdx has been solved at 1.7 Å resolution. The [2Fe-2S] cluster is located near the surface of the protein and is coordinated by the Sγ atoms of Cys42, Cys48, Cys51, and Cys87; another cysteine residue, Cys46, is exposed on the surface near the Fe-S cluster . Fdx is synthesized under both aerobic and anaerobic growth conditions . An fdx null mutant strain grows with a significantly increased doubling time compared to wild type . Review: .

## Enriched Pathways

- `eco00362` Benzoate degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9R4|protein.P0A9R4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008311,ECOCYC:EG11328,GeneID:947160`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2656748-2657083:-; feature_type=gene
