---
entity_id: "gene.b1589"
entity_type: "gene"
name: "ynfG"
source_database: "NCBI RefSeq"
source_id: "gene-b1589"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1589"
  - "ynfG"
---

# ynfG

`gene.b1589`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1589`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynfG (gene.b1589) is a gene entity. It encodes ynfG (protein.P0AAJ1). Encoded protein function: FUNCTION: Electron transfer subunit of the terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. EcoCyc product frame: G6847-MONOMER. Genomic coordinates: 1662990-1663607. EcoCyc protein note: YnfG is highly similar to DmsB, the iron-sulfur cluster-containing subunit of the dimethyl sulfoxide reductase heterotrimer, and cross-reacts with an anti-DmsB antibody. It contains iron-sulfur clusters which are indistinguishable from DmsB by EPR spectroscopy. When expressed together with DmsA and YnfH in a plasmid expression system, YnfG can form a complex with DmsA and YnfH and support growth on DMSO .

## Biological Role

Repressed by narL (protein.P0AF28). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), rpoS (protein.P13445), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAJ1|protein.P0AAJ1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ynfG; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ynfG; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ynfG; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ynfG; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ynfG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005309,ECOCYC:G6847,GeneID:945638`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1662990-1663607:+; feature_type=gene
