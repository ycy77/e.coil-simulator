---
entity_id: "gene.b1920"
entity_type: "gene"
name: "tcyJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1920"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1920"
  - "tcyJ"
---

# tcyJ

`gene.b1920`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1920`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tcyJ (gene.b1920) is a gene entity. It encodes tcyJ (protein.P0AEM9). Encoded protein function: FUNCTION: Part of the ABC transporter complex TcyJLN involved in L-cystine import (PubMed:20351115, PubMed:25139244, PubMed:25837721, PubMed:26350134). This high affinity cystine transporter is involved in resistance to oxidative stress by forming a L-cysteine/L-cystine shuttle system with the EamA transporter, which exports L-cysteine as reducing equivalents to the periplasm to prevent the cells from oxidative stress. Exported L-cysteine can reduce the periplasmic hydrogen peroxide to water, and then generated L-cystine is imported back into the cytoplasm via the TcyJLN complex (PubMed:20351115, PubMed:25837721). Functions at low cystine concentrations (PubMed:26350134). The system can also transport L-cysteine, diaminopimelic acid (DAP), djenkolate, lanthionine, D-cystine, homocystine, and it mediates accumulation of the toxic compounds L-selenaproline (SCA) and L-selenocystine (SeCys) (PubMed:25139244, PubMed:26350134). Binds cystine and DAP (PubMed:4564569, PubMed:8450713). {ECO:0000269|PubMed:20351115, ECO:0000269|PubMed:25139244, ECO:0000269|PubMed:25837721, ECO:0000269|PubMed:26350134, ECO:0000269|PubMed:4564569, ECO:0000269|PubMed:8450713}. EcoCyc product frame: G7039-MONOMER. EcoCyc synonyms: yzzR, ssi7, fliY. Genomic coordinates: 1999585-2000385...

## Biological Role

Repressed by nsrR (protein.P0AF63), csgD (protein.P52106), ecpR (protein.P71301), sutR (protein.P77626). Activated by rpoD (protein.P00579), fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEM9|protein.P0AEM9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=tcyJ; function=+
- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=tcyJ; function=+
- `represses` <-- [[protein.P0AF63|protein.P0AF63]] `RegulonDB` `S` - regulator=NsrR; target=tcyJ; function=-
- `represses` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=tcyJ; function=-
- `represses` <-- [[protein.P71301|protein.P71301]] `RegulonDB` `S` - regulator=MatA; target=tcyJ; function=-
- `represses` <-- [[protein.P77626|protein.P77626]] `RegulonDB` `S` - regulator=SutR; target=tcyJ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006392,ECOCYC:G7039,GeneID:948833`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1999585-2000385:-; feature_type=gene
