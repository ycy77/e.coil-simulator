---
entity_id: "gene.b3745"
entity_type: "gene"
name: "viaA"
source_database: "NCBI RefSeq"
source_id: "gene-b3745"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3745"
  - "viaA"
---

# viaA

`gene.b3745`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3745`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

viaA (gene.b3745) is a gene entity. It encodes viaA (protein.P0ADN0). Encoded protein function: FUNCTION: Component of the RavA-ViaA chaperone complex, which may act on the membrane to optimize the function of some of the respiratory chains (PubMed:16301313, PubMed:24454883, PubMed:27979649, PubMed:36127320, PubMed:36625597). ViaA stimulates the ATPase activity of RavA (PubMed:16301313, PubMed:27979649, PubMed:37660904). {ECO:0000269|PubMed:16301313, ECO:0000269|PubMed:24454883, ECO:0000269|PubMed:27979649, ECO:0000269|PubMed:36127320, ECO:0000269|PubMed:36625597, ECO:0000269|PubMed:37660904}.; FUNCTION: The RavA-ViaA system is involved in the regulation of two respiratory complexes, the fumarate reductase (Frd) electron transport complex and the NADH-quinone oxidoreductase complex (NDH-1 or Nuo complex) (PubMed:24454883, PubMed:27979649). It modulates the activity of the Frd complex, signifying a potential regulatory function during bacterial anaerobic respiration with fumarate as the terminal electron acceptor (PubMed:27979649). Interaction of RavA-ViaA with FrdA results in a decrease in Frd activity (PubMed:27979649). It also interacts with the Nuo complex, known to be involved in both the aerobic and the anaerobic respiration (PubMed:24454883)...

## Biological Role

Activated by fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADN0|protein.P0ADN0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=viaA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012244,ECOCYC:EG11730,GeneID:948257`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3928152-3929603:-; feature_type=gene
