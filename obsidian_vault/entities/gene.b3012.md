---
entity_id: "gene.b3012"
entity_type: "gene"
name: "dkgA"
source_database: "NCBI RefSeq"
source_id: "gene-b3012"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3012"
  - "dkgA"
---

# dkgA

`gene.b3012`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3012`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dkgA (gene.b3012) is a gene entity. It encodes dkgA (protein.Q46857). Encoded protein function: FUNCTION: Aldo-keto reductase that significantly contributes to cellular methylglyoxal detoxification by catalyzing the NADPH-dependent conversion of methylglyoxal to acetol (PubMed:16077126, PubMed:16284956). It also exhibits fairly high activity with glyoxal (PubMed:23990306). Shows broad specificity and can use aromatic aldehydes such as 4-nitrobenzaldehyde, 3-nitrobenzaldehyde and benzaldehyde, and phenylglyoxal (PubMed:16077126). Shows beta-keto ester reductase activity toward ethyl acetoacetate and a variety of 2-substituted derivatives (PubMed:11934293). Also catalyzes the reduction of 2,5-diketo-D-gluconic acid (25DKG) to 2-keto-L-gulonic acid (2KLG) and could be involved in ketogluconate metabolism (PubMed:10427017). However, the specific activity of the enzyme toward 2,5-diketo-D-gluconate was reported to be almost 400-fold lower than its activity toward methylglyoxal (PubMed:16077126). Can catalyze in vitro the NADPH-dependent reduction of furfural, a natural product of lignocellulosic decomposition, to the less toxic product, furfuryl alcohol (PubMed:19429550). However, it is unlikely that furfural is a physiological substrate (PubMed:19429550)...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), fur (protein.P0A9A9), yqhC (protein.Q46855).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46857|protein.Q46857]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dkgA; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=dkgA; function=+
- `activates` <-- [[protein.Q46855|protein.Q46855]] `RegulonDB` `S` - regulator=YqhC; target=dkgA; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=dkgA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009892,ECOCYC:G7565,GeneID:947495`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3156623-3157450:+; feature_type=gene
