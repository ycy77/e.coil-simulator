---
entity_id: "gene.b3746"
entity_type: "gene"
name: "ravA"
source_database: "NCBI RefSeq"
source_id: "gene-b3746"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3746"
  - "ravA"
---

# ravA

`gene.b3746`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3746`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ravA (gene.b3746) is a gene entity. It encodes ravA (protein.P31473). Encoded protein function: FUNCTION: Component of the RavA-ViaA chaperone complex, which may act on the membrane to optimize the function of some of the respiratory chains (PubMed:16301313, PubMed:24454883, PubMed:27979649, PubMed:36127320, PubMed:36625597). RavA functions as an ATPase (PubMed:16301313, PubMed:27979649, PubMed:31992852, PubMed:37660904). {ECO:0000269|PubMed:16301313, ECO:0000269|PubMed:24454883, ECO:0000269|PubMed:27979649, ECO:0000269|PubMed:31992852, ECO:0000269|PubMed:36127320, ECO:0000269|PubMed:36625597, ECO:0000269|PubMed:37660904}.; FUNCTION: The RavA-ViaA system is involved in the regulation of two respiratory complexes, the fumarate reductase (Frd) electron transport complex and the NADH-quinone oxidoreductase complex (NDH-1 or Nuo complex) (PubMed:24454883, PubMed:27979649). It modulates the activity of the Frd complex, signifying a potential regulatory function during bacterial anaerobic respiration with fumarate as the terminal electron acceptor (PubMed:27979649). Interaction of RavA-ViaA with FrdA results in a decrease in Frd activity (PubMed:27979649). It also interacts with the Nuo complex, known to be involved in both the aerobic and the anaerobic respiration (PubMed:24454883)...

## Biological Role

Activated by fnr (protein.P0A9E5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31473|protein.P31473]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ravA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012247,ECOCYC:EG11731,GeneID:948256`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3929597-3931093:-; feature_type=gene
