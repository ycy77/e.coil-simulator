---
entity_id: "gene.b2964"
entity_type: "gene"
name: "nupG"
source_database: "NCBI RefSeq"
source_id: "gene-b2964"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2964"
  - "nupG"
---

# nupG

`gene.b2964`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2964`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nupG (gene.b2964) is a gene entity. It encodes nupG (protein.P0AFF4). Encoded protein function: FUNCTION: Broad-specificity transporter of purine and pyrimidine nucleosides (PubMed:11466294, PubMed:15513740, PubMed:15678184, PubMed:3311747, PubMed:374403). Can transport adenosine, uridine, thymidine, cytidine, deoxycytidine, guanosine and inosine (PubMed:11466294, PubMed:15513740, PubMed:15678184, PubMed:3311747, PubMed:374403). Can also transport xanthosine, but with a very low affinity (PubMed:11466294). Transport is driven by a proton motive force (PubMed:15513740, PubMed:374403). {ECO:0000269|PubMed:11466294, ECO:0000269|PubMed:15513740, ECO:0000269|PubMed:15678184, ECO:0000269|PubMed:3311747, ECO:0000269|PubMed:374403}. EcoCyc product frame: NUPG-MONOMER. EcoCyc synonyms: gru. Genomic coordinates: 3105714-3106970. EcoCyc protein note: Early studies in E. coli K-12 reported the presence of two different nucleoside transport systems, one of which (gru/nupG) transports all nucleosides and is not affected by the nucleoside antibiotic, showdomycin, and the other (cru/NUPC-MONOMER nupC) which transports pyrimidine and adenine nucleosides and is inhibited by showdomycin . NupG is a broad specificity nucleoside transporter; it mediates uptake of all 6 natural purine/pyrimidine nucleosides...

## Biological Role

Repressed by crp (protein.P0ACJ8), cytR (protein.P0ACN7). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFF4|protein.P0AFF4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nupG; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=nupG; function=-+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=nupG; function=-+
- `represses` <-- [[protein.P0ACN7|protein.P0ACN7]] `RegulonDB` `S` - regulator=CytR; target=nupG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009728,ECOCYC:EG10664,GeneID:946282`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3105714-3106970:+; feature_type=gene
