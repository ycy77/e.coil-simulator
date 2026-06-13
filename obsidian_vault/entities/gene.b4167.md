---
entity_id: "gene.b4167"
entity_type: "gene"
name: "nnr"
source_database: "NCBI RefSeq"
source_id: "gene-b4167"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4167"
  - "nnr"
---

# nnr

`gene.b4167`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4167`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nnr (gene.b4167) is a gene entity. It encodes nnr (protein.P31806). Encoded protein function: FUNCTION: Bifunctional enzyme that catalyzes the epimerization of the S- and R-forms of NAD(P)HX and the dehydration of the S-form of NAD(P)HX at the expense of ADP, which is converted to AMP. This allows the repair of both epimers of NAD(P)HX, a damaged form of NAD(P)H that is a result of enzymatic or heat-dependent hydration. {ECO:0000269|PubMed:21994945}. EcoCyc product frame: EG11758-MONOMER. EcoCyc synonyms: yjeF. Genomic coordinates: 4394066-4395613. EcoCyc protein note: The Nnr protein is a bifunctional enzyme that catalyzes both the epimerization between the R and S forms of NAD(P)HX and the ADP-dependent repair of (S)-NAD(P)HX to NAD(P)H. The N-terminal domain appears to be responsible for the epimerase activity, while the C-terminal domain is responsible for the dehydratase activity . Comparative genomics and metabolomics experiments suggest that Nnr, and in particular the epimerase domain, may have a moonlighting function that involves pyridoxal phosphate metabolism . Studies in the 1950s have shown that eukaryotic GAPOXNPHOSPHN-RXN "glyceraldehyde 3-phosphate dehydrogenase" slowly catalyzes the formation of a hydrated form of NADH, called NADHX, from NADH...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31806|protein.P31806]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=nnr; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013644,ECOCYC:EG11758,GeneID:948685`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4394066-4395613:+; feature_type=gene
