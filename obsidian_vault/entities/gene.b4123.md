---
entity_id: "gene.b4123"
entity_type: "gene"
name: "dcuB"
source_database: "NCBI RefSeq"
source_id: "gene-b4123"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4123"
  - "dcuB"
---

# dcuB

`gene.b4123`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4123`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dcuB (gene.b4123) is a gene entity. It encodes dcuB (protein.P0ABN9). Encoded protein function: FUNCTION: Bifunctional protein with a transport and a regulatory function (PubMed:18957436, PubMed:27318186). Responsible for the transport of C4-dicarboxylates during anaerobic growth (PubMed:17643228, PubMed:7961398, PubMed:8131924, PubMed:8955408). Catalyzes the uptake of fumarate, malate, aspartate or D-tartrate coupled to the export of succinate (PubMed:17643228, PubMed:7961398, PubMed:8955408). Can also catalyze the uptake (without exchange) of fumarate (PubMed:8955408). May function primarily as a C4-dicarboxylate transporter during fumarate respiration (PubMed:9852003). Required for anaerobic growth on D-tartrate (PubMed:17643228). {ECO:0000269|PubMed:17643228, ECO:0000269|PubMed:18957436, ECO:0000269|PubMed:27318186, ECO:0000269|PubMed:7961398, ECO:0000269|PubMed:8131924, ECO:0000269|PubMed:8955408, ECO:0000269|PubMed:9852003}.; FUNCTION: In addition, possesses a regulatory function, which is independent from the transport function, and is required for the response of the DcuS/DcuR two-component system to C4-dicarboxylates (PubMed:18957436, PubMed:27318186). DcuB interacts physically with DcuS and converts DcuS to the C4-dicarboxylate responsive form (PubMed:27318186)...

## Biological Role

Activated by arcA (protein.P0A9Q1), dcuR (protein.P0AD01).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABN9|protein.P0ABN9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=dcuB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AD01|protein.P0AD01]] `RegulonDB` `S` - regulator=DcuR; target=dcuB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013503,ECOCYC:EG10006,GeneID:948641`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4347404-4348744:-; feature_type=gene
