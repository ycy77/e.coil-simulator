---
entity_id: "gene.b3453"
entity_type: "gene"
name: "ugpB"
source_database: "NCBI RefSeq"
source_id: "gene-b3453"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3453"
  - "ugpB"
---

# ugpB

`gene.b3453`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3453`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ugpB (gene.b3453) is a gene entity. It encodes ugpB (protein.P0AG80). Encoded protein function: FUNCTION: Part of the ABC transporter complex UgpBAEC involved in sn-glycerol-3-phosphate (G3P) import (PubMed:23013274, PubMed:2842304). Can also transport glycerophosphoryl diesters, which are hydrolyzed to G3P and alcohol during transport (PubMed:2842304). The G3P moiety can be detected in the cytoplasm whereas the corresponding alcohol is usually found in the culture medium (PubMed:2842304). Binds G3P and glycerophosphocholine, but not glycerol-2-phosphate (PubMed:23013274). It was proposed by Yang et al that the complex could also transport glycerol-2-phosphate (G2P) in vivo, but as it was shown later by Wuttge et al that UgpB does not bind G2P, this transport activity is questioned (PubMed:19429609, PubMed:23013274). G2P might be converted in the periplasm to G3P before its transport (PubMed:23013274). {ECO:0000269|PubMed:19429609, ECO:0000269|PubMed:23013274, ECO:0000269|PubMed:2842304}.; FUNCTION: In the absence of G3P, UgpB can serve as a potent molecular chaperone that exhibits anti-aggregation activity against bile salt-induced protein aggregation (PubMed:32882062)...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), phoB (protein.P0AFJ5). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG80|protein.P0AG80]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ugpB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ugpB; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB|EcoCyc` `C` - regulator=PhoB; target=ugpB; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=ugpB; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011274,ECOCYC:EG11047,GeneID:947962`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3591009-3592325:-; feature_type=gene
