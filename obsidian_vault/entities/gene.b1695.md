---
entity_id: "gene.b1695"
entity_type: "gene"
name: "ydiO"
source_database: "NCBI RefSeq"
source_id: "gene-b1695"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1695"
  - "ydiO"
---

# ydiO

`gene.b1695`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1695`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydiO (gene.b1695) is a gene entity. It encodes ydiO (protein.P0A9U8). Encoded protein function: Probable acyl-CoA dehydrogenase YdiO (EC 1.3.-.-) EcoCyc product frame: G6918-MONOMER. Genomic coordinates: 1777196-1778347. EcoCyc protein note: YdiO has sequence similarity to CROBETREDUCT-MONOMER and is much less similar to ACYLCOADEHYDROG-MONOMER "FadE", the acyl-CoA dehydrogenase involved in fatty acid oxidation. The nearby genes ydiQR encode a putative electron transfer flavoprotein-like heterodimer, while ydiST may form an ETF-quinone oxidoreductase and may be involved in an electron transfer pathway with YdiO, analogous to fixABCX and CaiA . An assay of unpurified YdiO showed a small amount of dehydrogenase activity with butyryl-CoA; no activity was detected with the purified protein, indicating that the enzyme may require auxiliary flavoproteins and an electron donor to function . Overexpression of YdiO did not result in a significant increase in butyryl-CoA dehydrogenase activity in crude extracts . YdiO was hypothesized to catalyze the reduction of enoyl-CoA to acyl-CoA, enabling the engineered one-turn reversal of the β-oxidation cycle to yield butanol. A ΔydiO mutation in the engineered strain led to increased yield of trans-2-butenoate and reduced butanol production...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9U8|protein.P0A9U8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydiO; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005658,ECOCYC:G6918,GeneID:945626`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1777196-1778347:+; feature_type=gene
