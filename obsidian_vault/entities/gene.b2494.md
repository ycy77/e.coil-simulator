---
entity_id: "gene.b2494"
entity_type: "gene"
name: "bepA"
source_database: "NCBI RefSeq"
source_id: "gene-b2494"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2494"
  - "bepA"
---

# bepA

`gene.b2494`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2494`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bepA (gene.b2494) is a gene entity. It encodes bepA (protein.P66948). Encoded protein function: FUNCTION: Functions both as a chaperone and a metalloprotease. Maintains the integrity of the outer membrane by promoting either the assembly or the elimination of outer membrane proteins, depending on their folding state. Promotes disulfide rearrangement of LptD during its biogenesis, and proteolytic degradation of LptD and BamA when their proper assembly is compromised. May facilitate membrane attachment of LoiP under unfavorable conditions. {ECO:0000255|HAMAP-Rule:MF_00997, ECO:0000269|PubMed:22491786, ECO:0000269|PubMed:24003122}. EcoCyc product frame: G7311-MONOMER. EcoCyc synonyms: yfgC. Genomic coordinates: 2616094-2617557. EcoCyc protein note: BepA (formerly YfgC) is a periplasmic protein and a member of the M48 metalloprotease family ; BepA functions as a protease/chaperone with a role in maintaining outer membrane integrity . Purified BepA has low proteolytic activity in vitro which is absent in the presence of metal chelating reagents. BepA promotes the formation of correct disulfide bonds in EG11569-MONOMER "LptD". This activity is independent of its protease activity. The protease function of BepA serves to degrade LptD that fails to form an outer membrane translocon. BepA also cleaves BamA in a ΔsurA background...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P66948|protein.P66948]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=bepA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008212,ECOCYC:G7311,GeneID:947029`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2616094-2617557:+; feature_type=gene
