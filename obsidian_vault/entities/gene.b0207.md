---
entity_id: "gene.b0207"
entity_type: "gene"
name: "dkgB"
source_database: "NCBI RefSeq"
source_id: "gene-b0207"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0207"
  - "dkgB"
---

# dkgB

`gene.b0207`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0207`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dkgB (gene.b0207) is a gene entity. It encodes dkgB (protein.P30863). Encoded protein function: FUNCTION: Aldo-keto reductase that significantly contributes to cellular methylglyoxal detoxification by catalyzing the NADPH-dependent conversion of methylglyoxal to acetol (PubMed:16077126). It also exhibits fairly high activity with glyoxal and probably plays a significant role in detoxification of glyoxal in vivo (PubMed:23990306). Shows broad specificity and can use aromatic aldehydes such as 4-nitrobenzaldehyde, 3-nitrobenzaldehyde and benzaldehyde, and phenylglyoxal (PubMed:16077126). Also catalyzes the reduction of 2,5-diketo-D-gluconic acid (25DKG) to 2-keto-L-gulonic acid (2KLG) and could be involved in ketogluconate metabolism (PubMed:10427017). However, the specific activity of the enzyme toward 2,5-diketo-D-gluconate was reported to be almost 400-fold lower than its activity toward methylglyoxal (PubMed:16077126). {ECO:0000269|PubMed:10427017, ECO:0000269|PubMed:16077126, ECO:0000269|PubMed:23990306}. EcoCyc product frame: MONOMER0-149. EcoCyc synonyms: yafB. Genomic coordinates: 229167-229970. EcoCyc protein note: DkgB is a member of the aldo-keto reductase (AKR) subfamily 3F . DkgB was shown by different authors to have 2,5-diketo-D-gluconate reductase , methylglyoxal reductase and 4-nitrobenzaldehyde reductase activities...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30863|protein.P30863]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000692,ECOCYC:EG11648,GeneID:944901`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:229167-229970:+; feature_type=gene
