---
entity_id: "gene.b1860"
entity_type: "gene"
name: "ruvB"
source_database: "NCBI RefSeq"
source_id: "gene-b1860"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1860"
  - "ruvB"
---

# ruvB

`gene.b1860`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1860`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ruvB (gene.b1860) is a gene entity. It encodes ruvB (protein.P0A812). Encoded protein function: FUNCTION: The RuvABC complex is involved in recombinational repair of UV or chemically damaged DNA (PubMed:6374379). The complex also plays an important role in the rescue of blocked DNA replication forks via replication fork reversal (RFR); RFR and homologous recombination required for UV light survival can be separated (PubMed:16424908, PubMed:18942176, PubMed:9814711). This subunit has a weak ATPase activity that is inhibited by its ADP product; binds ADP better than ATP (PubMed:2529252). Promotes Holliday junction (HJ) branch migration in conjunction with RuvA. Binds to HJ cruciform DNA; in the presence of RuvA, ATP and Mg(2+) the junction is dissociated. Hydrolyzable (d)NTPs can replace ATP but other analogs cannot (PubMed:1608954, PubMed:1617728, PubMed:6374379, PubMed:8393934). The RuvB hexamer acts as a pump, pulling DNA into and through the RuvAB complex (PubMed:9078376). Can bypass UV-induced lesions (PubMed:1617728) and physically cross-linked DNA strands (PubMed:10662672), suggesting RuvB does not unwind large sections of DNA. RuvA gives specificity by binding to cruciform junctions, while the RuvB ATPase provides the motor force for branch migration; excess RuvB can promote branch migration in the absence of RuvA (PubMed:10662672, PubMed:1617728)...

## Biological Role

Repressed by lexA (protein.P0A7C2).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A812|protein.P0A812]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=ruvB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006204,ECOCYC:RUVB,GeneID:946371`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1944346-1945356:-; feature_type=gene
