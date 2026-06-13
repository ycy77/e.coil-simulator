---
entity_id: "gene.b4002"
entity_type: "gene"
name: "zraP"
source_database: "NCBI RefSeq"
source_id: "gene-b4002"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4002"
  - "zraP"
---

# zraP

`gene.b4002`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4002`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

zraP (gene.b4002) is a gene entity. It encodes zraP (protein.P0AAA9). Encoded protein function: FUNCTION: Part of the Zra signaling pathway, an envelope stress response (ESR) system composed of the periplasmic accessory protein ZraP, the histidine kinase ZraS and the transcriptional regulator ZraR (PubMed:26438879, PubMed:30389436, PubMed:33309686). The ZraPSR system contributes to antibiotic resistance and is important for membrane integrity in the presence of membrane-targeting biocides (PubMed:30389436). ZraP acts as a modulator which has both a regulatory and a chaperone function (PubMed:26438879, PubMed:30389436). The zinc-bound form of ZraP modulates the response of the ZraPSR system by inhibiting the expression of the zra genes, probably by interacting with ZraS (PubMed:26438879). Participation to the cell protection arises mainly from this repressor function (PubMed:30389436). Also displays chaperone properties in vitro and protects malate dehydrogenase (MDH) from thermal denaturation at 45 degrees Celsius (PubMed:26438879). Binds zinc, copper, nickel, cobalt but not cadmium or manganese (PubMed:22094925, PubMed:26438879, PubMed:30616070, PubMed:9694902). In vitro, has a higher affinity for copper than for zinc (PubMed:26438879, PubMed:30616070). Is the main zinc containing protein under zinc stress conditions (PubMed:22094925)...

## Biological Role

Activated by zraR (protein.P14375).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAA9|protein.P0AAA9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB` `C` - regulator=ZraR; target=zraP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013081,ECOCYC:EG11918,GeneID:948507`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4201263-4201688:-; feature_type=gene
