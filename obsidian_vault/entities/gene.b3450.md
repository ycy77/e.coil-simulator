---
entity_id: "gene.b3450"
entity_type: "gene"
name: "ugpC"
source_database: "NCBI RefSeq"
source_id: "gene-b3450"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3450"
  - "ugpC"
---

# ugpC

`gene.b3450`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3450`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ugpC (gene.b3450) is a gene entity. It encodes ugpC (protein.P10907). Encoded protein function: FUNCTION: Part of the ABC transporter complex UgpBAEC involved in sn-glycerol-3-phosphate (G3P) import (PubMed:23013274, PubMed:2842304, PubMed:363686, PubMed:7042685, PubMed:8282692). Responsible for energy coupling to the transport system (Probable). Can also transport glycerophosphoryl diesters, which are hydrolyzed to G3P and alcohol during transport (PubMed:2842304). The G3P moiety can be detected in the cytoplasm whereas the corresponding alcohol is usually found in the culture medium (PubMed:2842304). It was proposed by Yang et al that the complex could also transport glycerol-2-phosphate (G2P) in vivo, but it was shown later by Wuttge et al that UgpB does not bind G2P, questioning this transport activity (PubMed:19429609, PubMed:23013274). G2P might be converted in the periplasm to G3P before its transport (PubMed:23013274). {ECO:0000269|PubMed:19429609, ECO:0000269|PubMed:23013274, ECO:0000269|PubMed:2842304, ECO:0000269|PubMed:363686, ECO:0000269|PubMed:7042685, ECO:0000269|PubMed:8282692, ECO:0000305}. EcoCyc product frame: UGPC-MONOMER. Genomic coordinates: 3588110-3589180. EcoCyc protein note: UgpC is the predicted ATP binding subunit of an sn-glycerol 3-phosphate ABC importer . UgpC contains signature motifs conserved in ABC domains

## Biological Role

Repressed by phoB (protein.P0AFJ5). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10907|protein.P10907]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ugpC; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ugpC; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=ugpC; function=-+
- `represses` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=ugpC; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011266,ECOCYC:EG11048,GeneID:947953`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3588110-3589180:-; feature_type=gene
